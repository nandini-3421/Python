#OOP
#1) Class: It is the blue prinnt to describe object
#2) class is the collection of variables and methods
#3) to access class members you need to create object of the class
#4) object is called as runtime entity or we can say is instance of a class
'''
class car:
    def display(self):
        print("this is my dream car")

honda=car()       #object creation
toyota=car()
honda.display()

#example

class Student:
    def __init__(self,name,sector):  #costructor
        self.name=name
        self.sector=sector

    def getInfo(self):
        print("hello my nme is nandini")
        
    def display(self):
        print(f"welcome {self.name} to the {self.sector} sector")

s1=Student("raj","banking")
s1.display()
s1.getInfo()

'''  
#whenever we pass the data to class constructor we need use __init__ method
#parameters inside the method are called as local parameters
#scope is only within the function

#area of rectangle
class Rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
num1=int(input("enter length: "))
num2=int(input("enter breadth: "))
r=Rect(num1,num2)
ans=r.area()
print("the area of rectangle is",ans)
