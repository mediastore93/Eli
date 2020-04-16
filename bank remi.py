class BankAccount(object):
    money=0
    name=""
    age=0
    def __init__(self,money,name,age):
        self.money=money
        self.name=name
        self.age=age

    def deposit(self,cash):
        self.money+=cash

    def withdraw(self,cash):
        if (self.age<9):
            return False
        else:
            self.money-=cash
            return True
        
def makeBankAccount(name,age):
    bank=BankAccount(0,name,age)
    return bank
print("what is your name?")
n=str(input())
print("how old are you?")
a=int(input())
account=makeBankAccount(n,a)
print (account.money)
print ("how much money do you want to deposit?")
cash=int(input())
account.deposit(cash)
print (account.money)

print ("how much money do you want to withdraw?")
w=int(input())
if (not account.withdraw(w)):
    print("NO you are not allowed because you are under 9!") 
print (account.money)

nik_account=makeBankAccount("nik",100)
print("how mach money do you want to deposit?")
cash=int(input())
nik_account.deposit(cash)
print (nik_account.money)
nik_account.withdraw(50)
print (nik_account.money)
