class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initAmount, acctName):
        self.balance = initAmount
        self.name = acctName
        print(f"\nAccount for '{self.name}' created.\nBalance: ${self.balance:.2f}")
        
    def getBalance(self):
        print(f"\nAccount for '{self.name}' \nBalance: ${self.balance:.2f}")
        
    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposit complete.")
        self.getBalance()
        
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account for '{self.name}' only has a balance of ${self.balance:.2f}. This transaction requires ${amount:.2f}."
            )
            
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw failed: {error}')
            
    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer..')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete.\n\n**********')
        except BalanceException as error:
            print(f"\nTransfer to '{account.name} failed: {error}")
            
class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        interest = (amount * 1.05) - amount
        print(f"\nDeposited ${amount:.2f} and have earned 5% (${interest:.2f}) in interest.")
        self.getBalance()
        
class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initAmount, acctName):
        super().__init__(initAmount, acctName)
        self.fee = 5
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw failed: {error}")