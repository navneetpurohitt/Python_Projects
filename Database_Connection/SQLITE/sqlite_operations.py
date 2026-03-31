import sqlite3

# Database connection
def connect_to_db(db_name="example.db"):
    return sqlite3.connect(db_name)

# Create table
def create_table():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Insert data
def insert_user(name, age, email):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", (name, age, email))
    conn.commit()
    conn.close()

# Read data
def fetch_users():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Update data
def update_user(user_id, name=None, age=None, email=None):
    conn = connect_to_db()
    cursor = conn.cursor()
    if name:
        cursor.execute("UPDATE users SET name = ? WHERE id = ?", (name, user_id))
    if age:
        cursor.execute("UPDATE users SET age = ? WHERE id = ?", (age, user_id))
    if email:
        cursor.execute("UPDATE users SET email = ? WHERE id = ?", (email, user_id))
    conn.commit()
    conn.close()

# Delete data
def delete_user(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

# Example usage
if __name__ == "__main__":
    create_table()
    insert_user("Alice", 25, "alice@example.com")
    insert_user("Bob", 30, "bob@example.com")
    print("Users:", fetch_users())
    update_user(1, age=26)
    delete_user(2)
    print("Users after update and delete:", fetch_users())