class Account:
    def __init__(self, account_number, balance=0.0):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def __str__(self):
        return f"Account Number: {self._account_number}, Balance: {self._balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._interest_rate

    def apply_interest(self):
        self._balance += self._balance * self._interest_rate


class CheckingAccount(Account):
    def __init__(self, account_number, balance=0.0, overdraft_limit=500.0):
        super().__init__(account_number, balance)
        self._overdraft_limit = overdraft_limit

    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self._balance + self._overdraft_limit:
            self._balance -= amount
            return True
        return False


class Transaction:
    transactions = []

    @staticmethod
    def log_transaction(account, transaction_type, amount):
        Transaction.transactions.append({
            "account_number": account.account_number,
            "transaction_type": transaction_type,
            "amount": amount,
            "balance": account.balance
        })

    @classmethod
    def get_transaction_history(cls):
        return cls.transactions


# Example usage:
if __name__ == "__main__":
    # Create accounts
    savings = SavingsAccount("SA123", 1000.0)
    checking = CheckingAccount("CA456", 500.0)

    # Perform transactions
    savings.deposit(200)
    Transaction.log_transaction(savings, "Deposit", 200)

    checking.withdraw(600)
    Transaction.log_transaction(checking, "Withdrawal", 600)

    savings.apply_interest()
    Transaction.log_transaction(savings, "Interest Applied", savings.balance)

    # Print account details
    print(savings)
    print(checking)

    # Print transaction history
    print("Transaction History:")
    for transaction in Transaction.get_transaction_history():
        print(transaction)