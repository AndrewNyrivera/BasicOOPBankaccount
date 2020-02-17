class BankAccount:
    # initializing the class
    def __init__(self):
        self.balance = 0

    # This function/method will take the amount you put in as a deposit
    def deposit(self, amount):
        # The balance was zero but when you deposit it will increase
        # by the amountyou deposit
        self.balance += amount

    def withdraw(self, amount):

        if self.balance >= amount:  # Makes sure that you have money in your account to withdraw
            self.balance -= amount  # ths can be written as
        else:
            print("Insufficent funds")

    def print_balance(self):  # This func will return your current balance
        return self.balance


# Creates a instance of the class and since no attributes, no need to write any
account = BankAccount()

account.deposit(100)  # Depositing 100 dollars into the account
print(account.print_balance())
account.deposit(1000)
print(account.print_balance())
account.withdraw(432)
print(account.print_balance())
