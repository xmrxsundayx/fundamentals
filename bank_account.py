class bank_account:
    bank_name = "Uncle Scrooges Vault"
    # accounts = []

    def __init__(self, int_rate = 0.05, balance =0):
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

    def display_account_info(self):
        print(f"interest rate:{self.int_rate}\nbalance:{self.balance}")
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


savings = bank_account()
checking = bank_account()


savings.deposit(2000).deposit(200).deposit(20).withdraw(1000).yeild_int_rate().display_account_info()
checking.deposit(4000).deposit(500).withdraw(20).withdraw(1000).withdraw(100).withdraw(900).yeild_int_rate().display_account_info()

bank_account.print_all_accounts()  
