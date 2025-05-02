#calculator class

class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a//self.b

a=float(input("Enter First number: "))
b=float(input("Enter second number: "))

cal=calculator(a,b)
addition=cal.add(nan)
subtraction=cal.sub()
multiplication=cal.mul()
division=cal.div()

print("The addition of two numbers is: ",addition)
print("The subtraction of two numbers is: ",subtraction)
print("The multiplication of two numbers is: ",multiplication)
print("The division of two numbers is: ",division)

#employee salary calculator

class employee:
    
    def __init__(self,sal,bon,name,department):
        self.sal=sal
        self.bon=bon
        self.name=name
        self.department=department
        
    def bonus(self):
        return self.sal+(self.sal*self.bon//100)

    def disp_info(self):
        self.name=name
        self.department=department
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
name=input("enter employee name: ")
department=input("enter employee department: ")
sal=float(input("enter your salary: "))
bon=float(input("enter bonus in %: "))

b=employee(sal,bon,name,department)
details=b.disp_info()
ans=b.bonus()

print(f"congratulations ",name," final salary you have received is: ",ans)

#book class add a discount method

class book:
    def __init__(self,title,author,price,discount):
        self.title=title
        self.author=author
        self.price=price
        self.discount=discount
        
    def discountonbook(self):
        cal=self.price*(self.discount/100)
        return self.price-cal
         

    def book_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        print(f"Discount in %: {self.discount}")

title=input("Enter title of book: ")
author=input("Enter author name: ")
price=float(input("enter price of the book: "))
discount=float(input("enter discount in %: "))
print("the original price of book is: ",price)

b=book(title,author,price,discount)
details=b.book_details()
ans=b.discountonbook()
print("price of book after discount is:",ans)

# bank account activities

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposite(self):
        amount = int(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
        else:
            self.balance += amount
            print("Amount deposited successfully.")
            print("Your current balance is: ₹", self.balance)

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient funds! Current balance is: ₹", self.balance)
        else:
            self.balance -= amount
            print("Withdrawal successful.")
            print("Your new balance is: ₹", self.balance)

    def check_balance(self):
        print("Your current balance is: ₹", self.balance)


owner = input("Enter your name: ")
initial_balance = float(input("Enter opening balance: ₹"))

acct = BankAccount(owner, initial_balance)

print("\nWelcome,", owner)
acct.deposite()
acct.withdraw()
acct.check_balance()


            
            
            








