import logging

# Create a logger
logger = logging.getLogger("bank_app")
logger.setLevel(logging.DEBUG)

# Create a file handler and set the log level to INFO
file_handler = logging.FileHandler("bank_app.log")
file_handler.setLevel(logging.INFO)

# Create a console handler and set the log level to DEBUG
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)

class Bank(User):
    account_counter = 1000

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.account_number = Bank.account_counter
        Bank.account_counter += 1
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount
        transaction = f"Deposited £{self.amount}"
        self.transaction_history.append(transaction)
        logger.info(f"Account {self.account_number}: {transaction}")
        print("Account balance has been updated: £", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available: £", self.balance)
        else:
            self.balance -= self.amount
            transaction = f"Withdrew £{self.amount}"
            self.transaction_history.append(transaction)
            logger.info(f"Account {self.account_number}: {transaction}")
            print("Account balance has been updated: £", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account Number:", self.account_number)
        print("Account balance: £", self.balance)

    def view_transaction_history(self):
        self.show_details()
        print("Account Number:", self.account_number)
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

# Example usage:
if __name__ == "__main__":
    user1 = Bank("John Doe", 30, "Male")
    user2 = Bank("Jane Smith", 25, "Female")

    user1.deposit(1000)
    user1.withdraw(500)
    user1.view_balance()
    user1.view_transaction_history()

    user2.deposit(1500)
    user2.view_balance()
    user2.withdraw(200)
    user2.view_transaction_history()
