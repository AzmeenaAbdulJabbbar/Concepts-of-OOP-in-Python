class BankAccount:
    def __init__(self ,balance):
        self.__balance = balance 
    def deposit(self, deposit):
        self.__balance += deposit
    # Encapsulation: Hiding the balance attribute
    def withdraw(self, withdraw):
        if withdraw >self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= withdraw
    # Encapsulation: Providing a method to access the balance
    def get_Balance(self,): 
        return self.__balance
# Example usage
# Creating an instance of BankAccount
account = BankAccount(1000)
account.deposit(500)
account.withdraw(1600)   
print("Balance:", account.get_Balance())