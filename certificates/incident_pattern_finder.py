"""
ServiceNow Incident Pattern Finder
====================================
Finds patterns in closed incidents using:
  - Rule-based keyword/regex classification
  - TF-IDF scoring for short note extraction
  - No AI/ML libraries required (only stdlib + optional pandas/csv)
"""

import re
import csv
import json
import math
import sys
from collections import defaultdict, Counter
from typing import Optional


# ──────────────────────────────────────────────
#  1.  CATEGORY RULES  (keyword → category)
#      Add / edit rules freely to fit your env.
# ──────────────────────────────────────────────
CATEGORY_RULES: list[dict] = [
    {
        "category": "Database Error",
        "keywords": [
            "database", "db", "sql", "oracle", "mysql", "postgres", "mongodb",
            "connection pool", "deadlock", "query timeout", "table lock",
            "ora-", "db2", "jdbc", "odbc", "stored procedure", "transaction",
            "constraint violation", "foreign key", "primary key", "index",
            "tablespace", "schema", "cursor", "rollback", "commit failed",
        ],
        "patterns": [
            r"ORA-\d+",
            r"SQL(State|Exception|Error)",
            r"db\s*(connection|timeout|error|failure)",
            r"(table|database)\s*(not found|unavailable|locked)",
        ],
        "weight": 1.0,
    },
    {
        "category": "Submodule / Dependency Missing",
        "keywords": [
            "submodule", "module not found", "missing module", "import error",
            "dependency", "package not found", "library missing", "dll",
            "cannot find module", "no module named", "classnotfoundexception",
            "nosuchbeanexception", "artifact", "jar missing", "npm install",
            "pip install", "requirements", "missing dependency",
        ],
        "patterns": [
            r"(cannot|can't|could not)\s+find\s+(module|package|library|class)",
            r"No module named ['\"]\w+",
            r"ModuleNotFoundError",
            r"ClassNotFoundException",
            r"ImportError",
            r"missing\s+(dependency|submodule|module|package)",
        ],
        "weight": 1.0,
    },
    {
        "category": "Authentication / Authorization Error",
        "keywords": [
            "authentication", "authorization", "unauthorized", "forbidden",
            "401", "403", "access denied", "permission denied", "invalid token",
            "jwt", "oauth", "sso", "ldap", "password expired", "login failed",
            "credentials", "certificate", "ssl handshake", "tls",
        ],
        "patterns": [
            r"HTTP\s*40[13]",
            r"(access|permission)\s*denied",
            r"(invalid|expired)\s*(token|credential|certificate|password)",
            r"(authentication|authorization)\s*(failed|error|issue)",
        ],
        "weight": 1.0,
    },
    {
        "category": "Network / Connectivity Issue",
        "keywords": [
            "network", "connectivity", "timeout", "connection refused",
            "unreachable", "dns", "firewall", "proxy", "vpn", "latency",
            "packet loss", "bandwidth", "socket", "port", "ping", "traceroute",
            "connection reset", "host not found", "no route to host",
        ],
        "patterns": [
            r"(connection|network)\s*(timeout|refused|reset|failed)",
            r"(host|server|endpoint)\s*(unreachable|not found|unavailable)",
            r"(socket|port)\s*(error|closed|timeout)",
            r"\b(DNS|TCP|UDP|HTTP|HTTPS)\s*(failure|error|timeout)",
        ],
        "weight": 1.0,
    },
    {
        "category": "Application / Service Crash",
        "keywords": [
            "crash", "exception", "stack trace", "null pointer", "segfault",
            "out of memory", "oom", "heap", "core dump", "unhandled exception",
            "fatal error", "application stopped", "process killed", "restart",
            "jvm crash", "service down", "pod crash", "oom killer",
        ],
        "patterns": [
            r"(null\s*pointer|nullpointer)\s*exception",
            r"out\s*of\s*memory",
            r"(stack|heap)\s*overflow",
            r"(fatal|critical|unhandled)\s*(error|exception|crash)",
            r"(service|application|process|pod)\s*(crash|down|failed|stopped)",
        ],
        "weight": 1.0,
    },
    {
        "category": "Configuration / Environment Issue",
        "keywords": [
            "configuration", "config", "environment variable", "env var",
            "property", "yml", "yaml", "properties file", "settings",
            "misconfigured", "wrong value", "invalid config", "missing config",
            "deployment", "infrastructure", "kubernetes", "docker", "helm chart",
        ],
        "patterns": [
            r"(missing|invalid|wrong|bad)\s*(config|configuration|property|setting)",
            r"environment\s*variable\s*(not set|missing|undefined)",
            r"(yaml|yml|json|properties)\s*(parse|syntax)\s*error",
        ],
        "weight": 1.0,
    },
    {
        "category": "Performance / Slow Response",
        "keywords": [
            "slow", "performance", "high cpu", "high memory", "bottleneck",
            "throughput", "response time", "latency", "degraded", "throttling",
            "rate limit", "queue full", "backlog", "spike", "load", "overload",
        ],
        "patterns": [
            r"(slow|high)\s*(response|query|api|cpu|memory|load)",
            r"(performance|latency)\s*(issue|degraded|problem)",
            r"(queue|thread|pool)\s*(full|exhausted|blocked)",
        ],
        "weight": 1.0,
    },
    {
        "category": "Data / File Issue",
        "keywords": [
            "file not found", "corrupt", "data mismatch", "data loss",
            "missing data", "invalid data", "parsing error", "encoding",
            "csv", "json parse", "xml parse", "bad format", "duplicate",
            "data integrity", "checksum", "backup", "restore failed",
        ],
        "patterns": [
            r"file\s*(not found|missing|corrupt|unavailable)",
            r"(data|record)\s*(mismatch|corrupt|lost|missing)",
            r"(parse|parsing)\s*(error|failed|exception)",
            r"(invalid|bad|malformed)\s*(data|format|input|file)",
        ],
        "weight": 1.0,
    },
    {
        "category": "Deployment / Release Issue",
        "keywords": [
            "deployment", "release", "rollback", "pipeline", "ci/cd",
            "build failed", "artifact", "migration", "upgrade", "patch",
            "version mismatch", "incompatible", "breaking change",
        ],
        "patterns": [
            r"(deployment|release|build)\s*(failed|error|issue|broke)",
            r"(rollback|revert)\s*(triggered|required|failed)",
            r"(version|schema)\s*mismatch",
        ],
        "weight": 1.0,
    },
    {
        "category": "Third-Party / Integration Error",
        "keywords": [
            "third party", "vendor", "api error", "external service",
            "integration", "webhook", "rest api", "soap", "sftp",
            "payment gateway", "email service", "sms", "notification",
            "downstream", "upstream", "external dependency",
        ],
        "patterns": [
            r"(external|third.party|vendor)\s*(service|api|system)\s*(down|error|failed)",
            r"(webhook|callback)\s*(failed|error|timeout)",
            r"(integration|api)\s*(error|failure|issue)",
        ],
        "weight": 1.0,
    },
]


# ──────────────────────────────────────────────
#  2.  TEXT UTILITIES
# ──────────────────────────────────────────────

def normalize(text: str) -> str:
    """Lowercase and remove special characters for matching."""
    return re.sub(r"[^\w\s\-]", " ", text.lower())


def tokenize(text: str) -> list[str]:
    """Split into words, remove short tokens."""
    return [w for w in re.split(r"\W+", text.lower()) if len(w) > 2]


STOP_WORDS = {
    "the", "and", "for", "are", "was", "were", "has", "have", "had",
    "with", "from", "that", "this", "not", "but", "its", "also",
    "been", "into", "than", "when", "what", "after", "user", "team",
    "please", "note", "issue", "error", "problem", "ticket", "incident",
    "resolved", "closed", "fix", "fixed", "due", "found", "caused",
    "service", "system", "server", "application", "app", "done",
}


def clean_tokens(tokens: list[str]) -> list[str]:
    return [t for t in tokens if t not in STOP_WORDS and not t.isdigit()]


# ──────────────────────────────────────────────
#  3.  CATEGORY CLASSIFIER
# ──────────────────────────────────────────────

def classify(description: str, close_notes: str) -> tuple[str, float]:
    """
    Returns (category_name, confidence_score).
    Scores each category by keyword hits + regex matches.
    """
    combined = f"{description} {close_notes}"
    norm = normalize(combined)
    tokens = set(tokenize(combined))

    scores: dict[str, float] = {}

    for rule in CATEGORY_RULES:
        score = 0.0
        cat = rule["category"]

        # Keyword matching
        for kw in rule["keywords"]:
            if kw.lower() in norm:
                # Multi-word keywords score higher
                score += 1.5 if " " in kw else 1.0

        # Regex matching (higher weight)
        for pat in rule["patterns"]:
            if re.search(pat, combined, re.IGNORECASE):
                score += 2.5

        if score > 0:
            scores[cat] = score * rule["weight"]

    if not scores:
        return "Uncategorized", 0.0

    best_cat = max(scores, key=lambda c: scores[c])
    # Normalize confidence to 0–100%
    total = sum(scores.values())
    confidence = round((scores[best_cat] / total) * 100, 1) if total else 0.0
    return best_cat, confidence


# ──────────────────────────────────────────────
#  4.  SHORT NOTE GENERATOR  (TF-IDF based)
# ──────────────────────────────────────────────

def build_tfidf_summary(text: str, corpus: list[str], top_n: int = 8) -> str:
    """
    Picks the most 'unique' words in this document vs. the corpus,
    then selects the sentence with the highest term score as the summary.
    """
    doc_tokens = clean_tokens(tokenize(text))
    if not doc_tokens:
        return text[:150]

    # Term frequency in this doc
    tf: Counter = Counter(doc_tokens)
    total_terms = len(doc_tokens)

    # Document frequency across corpus
    df: Counter = Counter()
    for doc in corpus:
        doc_words = set(clean_tokens(tokenize(doc)))
        for w in doc_words:
            df[w] += 1

    N = len(corpus) or 1

    # TF-IDF score per term
    tfidf: dict[str, float] = {}
    for term, freq in tf.items():
        tf_score = freq / total_terms
        idf_score = math.log((N + 1) / (df.get(term, 0) + 1)) + 1
        tfidf[term] = tf_score * idf_score

    # Score each sentence by sum of its term TF-IDF values
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    sentences = [s.strip() for s in sentences if len(s.strip()) > 15]

    if not sentences:
        top_words = sorted(tfidf, key=lambda w: tfidf[w], reverse=True)[:top_n]
        return "Key terms: " + ", ".join(top_words)

    best_sent = max(
        sentences,
        key=lambda s: sum(tfidf.get(w, 0) for w in clean_tokens(tokenize(s))),
    )

    # Also append top keywords not already in the best sentence
    sent_words = set(tokenize(best_sent))
    extra = [
        w for w in sorted(tfidf, key=lambda x: tfidf[x], reverse=True)
        if w not in sent_words
    ][:5]

    note = best_sent
    if extra:
        note += f"  [Key terms: {', '.join(extra)}]"
    return note[:300]


# ──────────────────────────────────────────────
#  5.  MAIN PROCESSOR
# ──────────────────────────────────────────────

def process_incidents(incidents: list[dict]) -> list[dict]:
    """
    incidents: list of dicts with keys:
        incident_no, description, close_notes
    Returns enriched list with category, confidence, short_note.
    """
    # Build corpus for TF-IDF (combine description + close_notes)
    corpus = [f"{i.get('description', '')} {i.get('close_notes', '')}" for i in incidents]

    results = []
    for idx, inc in enumerate(incidents):
        desc = inc.get("description", "")
        notes = inc.get("close_notes", "")
        full_text = f"{desc} {notes}"

        category, confidence = classify(desc, notes)
        short_note = build_tfidf_summary(full_text, corpus)

        results.append({
            "incident_no":  inc.get("incident_no", f"INC{idx+1:04d}"),
            "category":     category,
            "confidence":   f"{confidence}%",
            "short_note":   short_note,
            "description":  desc,
            "close_notes":  notes,
        })

    return results


# ──────────────────────────────────────────────
#  6.  PATTERN SUMMARY  (aggregate view)
# ──────────────────────────────────────────────

def summarize_patterns(results: list[dict]) -> dict:
    """Returns category frequency and most common incidents per category."""
    cat_counter: Counter = Counter(r["category"] for r in results)
    cat_incidents: dict[str, list[str]] = defaultdict(list)

    for r in results:
        cat_incidents[r["category"]].append(r["incident_no"])

    return {
        "total_incidents": len(results),
        "categories": {
            cat: {
                "count": count,
                "percentage": f"{round(count / len(results) * 100, 1)}%",
                "incident_nos": cat_incidents[cat],
            }
            for cat, count in cat_counter.most_common()
        },
    }


# ──────────────────────────────────────────────
#  7.  I/O  HELPERS
# ──────────────────────────────────────────────

def load_from_csv(filepath: str) -> list[dict]:
    """
    CSV must have columns (case-insensitive):
        incident_no, description, close_notes
    """
    incidents = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Normalize key names
            norm_row = {k.strip().lower().replace(" ", "_"): v for k, v in row.items()}
            incidents.append({
                "incident_no":  norm_row.get("incident_no") or norm_row.get("number", ""),
                "description":  norm_row.get("description", ""),
                "close_notes":  norm_row.get("close_notes") or norm_row.get("closed_notes", ""),
            })
    return incidents


def load_from_json(filepath: str) -> list[dict]:
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


def print_results(results: list[dict], summary: dict) -> None:
    """Pretty-print to console."""
    sep = "─" * 80

    print("\n" + "═" * 80)
    print("  SERVICENOW INCIDENT PATTERN FINDER")
    print("═" * 80)

    for r in results:
        print(f"\n{sep}")
        print(f"  Incident  : {r['incident_no']}")
        print(f"  Category  : {r['category']}  (confidence: {r['confidence']})")
        print(f"  Short Note: {r['short_note']}")
        if r.get("description"):
            print(f"  Desc      : {r['description'][:120]}{'…' if len(r['description']) > 120 else ''}")

    print(f"\n{'═' * 80}")
    print("  PATTERN SUMMARY")
    print(f"{'═' * 80}")
    print(f"  Total incidents analysed : {summary['total_incidents']}\n")
    for cat, info in summary["categories"].items():
        bar_len = int(info["count"] / summary["total_incidents"] * 40)
        bar = "█" * bar_len
        print(f"  {cat:<38}  {info['count']:>3} ({info['percentage']:>6})  {bar}")
    print()


def export_csv(results: list[dict], out_path: str) -> None:
    fields = ["incident_no", "category", "confidence", "short_note", "description", "close_notes"]
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(results)
    print(f"  ✔  Results exported → {out_path}")


# ──────────────────────────────────────────────
#  8.  DEMO / ENTRY POINT
# ──────────────────────────────────────────────

DEMO_INCIDENTS = [
    {
        "incident_no": "INC0012301",
        "description": "Users unable to login. Authentication service returning 401 Unauthorized.",
        "close_notes": "Root cause: JWT token signing key was rotated without updating the auth service config. "
                       "Fixed by updating the OAUTH_SECRET environment variable and restarting the auth pod.",
    },
    {
        "incident_no": "INC0012302",
        "description": "Payment service crashes intermittently with OOM error in production.",
        "close_notes": "Java heap space exhausted due to memory leak in the transaction caching module. "
                       "Increased JVM heap size to 4GB and fixed the cache eviction policy. Deployed hotfix v2.3.1.",
    },
    {
        "incident_no": "INC0012303",
        "description": "Data pipeline failing. ORA-01017: invalid username/password when connecting to Oracle DB.",
        "close_notes": "Database password was rotated as part of quarterly policy but not updated in the JDBC "
                       "connection pool config. Updated the db.password property in application.yml and restarted service.",
    },
    {
        "incident_no": "INC0012304",
        "description": "Report generation module throws ModuleNotFoundError: No module named 'pdfkit'.",
        "close_notes": "Dependency 'pdfkit' was accidentally removed from requirements.txt during the last PR merge. "
                       "Added the missing dependency back and redeployed. CI pipeline updated to run pip check.",
    },
    {
        "incident_no": "INC0012305",
        "description": "Slow API response times on /search endpoint. P95 latency spiked to 12 seconds.",
        "close_notes": "Missing index on the product_catalog table caused full table scans. "
                       "Added composite index on (category_id, status). Query time reduced from 8s to 50ms.",
    },
    {
        "incident_no": "INC0012306",
        "description": "Microservice cannot connect to downstream inventory API. Connection timeout after 30s.",
        "close_notes": "Firewall rule was accidentally removed during network infrastructure change. "
                       "Restored the egress rule for port 8443 on the inventory service subnet.",
    },
    {
        "incident_no": "INC0012307",
        "description": "CSV import fails with 'invalid data format' for records uploaded after 3 PM.",
        "close_notes": "Date fields in afternoon exports used MM/DD/YYYY but parser expected YYYY-MM-DD. "
                       "Fixed the date parsing regex in the import service and added format validation.",
    },
    {
        "incident_no": "INC0012308",
        "description": "Post-deployment: notification emails not being sent. SMTP service unreachable.",
        "close_notes": "New deployment overrode SMTP_HOST environment variable to localhost instead of the mail relay. "
                       "Corrected the Helm chart values.yaml and redeployed. Email delivery confirmed.",
    },
]


def main():
    # ── Allow passing a CSV or JSON file as argument ──
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        print(f"\nLoading incidents from: {filepath}")
        if filepath.endswith(".csv"):
            incidents = load_from_csv(filepath)
        elif filepath.endswith(".json"):
            incidents = load_from_json(filepath)
        else:
            print("Unsupported file type. Use .csv or .json")
            sys.exit(1)
    else:
        print("\n[No file provided – running with demo incidents]\n")
        incidents = DEMO_INCIDENTS

    results = process_incidents(incidents)
    summary = summarize_patterns(results)
    print_results(results, summary)

    # Export enriched CSV
    export_csv(results, "incident_results.csv")


if __name__ == "__main__":
    main()
