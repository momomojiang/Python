class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)

Joe = User("Joe","Joe@mail.com")
Monty = User("Monty", "monty@mail.com")
Peter = User("Peter", "peter@mail.com")

# Joe.make_deposit(10)
# Joe.make_deposit(10)
# Joe.make_deposit(10)
# Joe.make_withdrawl(10)
# Joe.display_user_balance()

# Monty.make_deposit(10)
# Monty.make_deposit(10)
# Monty.make_withdrawl(10)
# Monty.display_user_balance()


class BankAccount:
    def __init__(self,interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
    def deposite(self, amount):
        self.balance += amount
        print(self.balance)
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print("Balance: $"+self)
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance = self.balance + self.balance * self.interest_rate
            print(self.balance)



# goldAccount = BankAccount(0.02,200)
silverAccount = BankAccount(0.03, 300)


# goldAccount.deposite(20).yield_interest()
silverAccount.deposite(20).deposite(20).yield_interest()