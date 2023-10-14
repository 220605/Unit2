class BankAccount:
   def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number=account_number 
    self.__account_holder_name=account_holder_name 
    self.__account_balance=initial_balance

def deposit(self,amount):
  if amount>0:
    self.__account_balance+=amount
    return f"Deposited ₹{amount}. Newbalance: ₹{self.__account_balance}"
  else:
    return"Invalid deposit amount. please deposit a positive amount."

def withdraw(self,amount):
  if 0<amount <=self.__account_balance:
    self.__account_balance-=amount
    return f"withdraw ₹{amount}. New balance: ₹{self.__amount_balance}"
  else:
    return "Invalid withdrawal amount or insufficient balance."

def display_balance(self):
    return f"Account balance for {self.__account_holder_name}: ₹{self.__account_balance}"

if __name__=="__main__":
 my_account=BankAccount("123456789","John doe",1000.0)
  #test deposit functionality
print(my_account.deposit(500))
# test withdrawal functionality
print(my_account.withdraw(200))
# display the account balance
print(my_account.display_balance())