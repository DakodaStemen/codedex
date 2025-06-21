class BankAccount():
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        # Set up all the details for the account when it's created
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        # Add funds to the balance
        if amount <= 0:
            print("Deposit must be more than zero.")
            return self.balance
        self.balance += amount
        print(f"Deposited ${amount:.2f} into the account.")
        return self.balance

    def withdraw(self, amount):
        # Take funds out if there's enough in the account
        if amount > self.balance:
            print("Insufficient funds. Withdrawal denied.")
            return 0
        self.balance -= amount
        print(f"Withdrew ${amount:.2f} from the account.")
        return amount

    def display_balance(self):
        # Just show the current balance, simple and clean
        print(f"Current balance: ${self.balance:.2f}")
