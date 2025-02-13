''' Write a Python program to create a class representing abank.
Include methods for managing customer accounts andtransactions (deposit, withdraw, and balance_enquiry). '''
class Bank:
    def __init__(self):
        self.accts = {}  # Stores account info

    def create(self, acct_no, name, bal=0):
        if acct_no in self.accts:
            print("Account exists.")
        else:
            self.accts[acct_no] = {"name": name, "bal": bal}
            print(f"Account created for {name}. Balance: {bal}.")

    def deposit(self, acct_no, amt):
        if acct_no in self.accts:
            self.accts[acct_no]["bal"] += amt
            print(f"Deposited {amt}. Balance: {self.accts[acct_no]['bal']}.")
        else:
            print("Account not found.")

    def withdraw(self, acct_no, amt):
        if acct_no in self.accts:
            if self.accts[acct_no]["bal"] >= amt:
                self.accts[acct_no]["bal"] -= amt
                print(f"Withdrawn {amt}. Balance: {self.accts[acct_no]['bal']}.")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")

    def balance(self, acct_no):
        if acct_no in self.accts:
            print(f"{self.accts[acct_no]['name']}: Balance: {self.accts[acct_no]['bal']}.")
        else:
            print("Account not found.")

# Example Usage
b = Bank()
b.create("1001", "Alice", 500)
b.create("1002", "Bob", 1000)
b.deposit("1001", 200)
b.withdraw("1002", 300)
b.balance("1001")
b.balance("1003")  # Non-existent account
