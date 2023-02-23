

class Bank_Account:
    bank_name = "Uncle Scrooges Vault"
    accounts = []

    def __init__(self, int_rate, balance =0):
        self.int_rate = int_rate
        self.balance = balance
        self.yeild_int = self.balance * self.int_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit amount {amount}\nYour new balance is {self.balance} ")
        return self

    def withdraw(self,amount):
        if self.balance < amount:
            print(f"Insuficiant funds\nYou only have {self.balance} in your account")
        elif self.balance >amount:
            self.balance -= amount
            print(f"withdraw amount {amount}\nYour new balance is {self.balance} ")
        return self

    def yeild_int_rate(self):
        if self.balance < 0:
            print("Not eligible for yeild interest")
        elif self.balance >0: 
            self.yeild_int = self.int_rate * self.balance
            self.balance += self.yeild_int
            print(f"balance with interest is {self.balance}")
            return self

    def balance(self):
        print(f"Your current Balance is {self.balance}")
        return self

    def account_info(self):
        print(f"interest rate:{self.int_rate}\nbalance:{self.balance}")
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.account_info()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = Bank_Account(int_rate=0.05, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self,amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.name)
        self.account.account_info()
        return self

User_Huey = User("Huey","darkwingduckHue@vault.com")
User_Dewey = User("Dewey","darkwingduckDew@vault.com")

User_Huey.display_user_balance().make_deposit(90).make_withdraw(20)
User_Dewey.display_user_balance().make_deposit(2000).make_withdraw(100)
