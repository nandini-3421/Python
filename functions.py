#Functions: block of statement which we can reuse anywhere
#function is written with keyword def
# WAP to write function to greet a person
'''
#creating function
def hello():
    print("hello user")
hello()

#Example
def greet():
    print("welcome to axis bank ")

def inData():
    uname=input("enter your name: ")
    print("hello ",uname)
greet()
inData()


# WAP to accept two numbers and print addition of it and product of it
def add(a,b):
    return a+b

def prod(a,b):
    mul=a*b
    print("the product of two numbers is: ",mul)
    
ans=add(34,26)
print("the addition of two numbers is: ",ans)
prod(5,9)

#WAP to get square of a number

def sq(a):
    square=a*a
    print("the square of a number is: ",square)
sq(4)

def sq(a):
    return a*a
square=sq(4)
print("the square of number is",square)


#area of circle
def aoc(radius):
    pi=3.14159
    return pi*radius*radius
print("Area: ",aoc(5)) 


#WAP to get average of three numbers

def avg(a,b,c):
    return (a+b+c)/3
num1=float(input("enter first number: "))
num2=float(input("enter second number: "))
num3=float(input("enter third number: "))
print("Average: ", avg(num1,num2,num3))

'''
#to check the number is even or odd
def checkNum(n):
    if(n%2==0):
        print("the given number is even")
    else:
        print("the number is odd")

num=int(input("enter a number: "))
checkNum(num)












































