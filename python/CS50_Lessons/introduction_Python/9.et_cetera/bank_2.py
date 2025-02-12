class Account:
    # Initialize the Account with a balance of 0
    def __init__(self):
        self._balance = 0 

    # This is a getter for the balance attribute.
    # It is called when we try to access the attribute using dot notation (e.g. account.balance).
    @property
    def balance(self):
        return self._balance

    # This method allows us to deposit an amount 'n' to the balance.
    def deposit(self, n):
        self._balance += n

    # This method allows us to withdraw an amount 'n' from the balance.
    def withdraw(self, n):
        self._balance -= n 


def main():
    # Create an instance of the Account class
    account = Account()
    # Print the balance of the account
    print("Balance", account.balance)

    # Deposit 100 to the account
    account.deposit(100)
    # Print the balance of the account
    print("Balance", account.balance)
    # Withdraw 50 from the account
    account.withdraw(50)
    # Print the balance of the account
    print("Balance", account.balance)

# If the script is run directly, run the main function
if __name__ == "__main__":
    main()
