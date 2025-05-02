'''#to find area of rectangle
length=int(input("enter a length of rectangle: "))
width=int(input("enter a width of rectangle: "))
AOR=length*width
print("Area of a rectangle is: ",AOR)


# to find area of a circle

pi=float(input("enter a value of pi: "))
rad=int(input("enter a value of radius: "))
AoC=pi*rad*rad         #aoc=pi(r^2)
print("area of a circle is: ",AoC)

#to get average of three numbers
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third number: "))

avg=(num1+num2+num3)//3

print("the average of three numbers is: ",avg)

#to find whether user can vote or not

age=int(input("enter your age: "))
if age<18:
    print("you are not eligible to vote")
else:
    print("congratulations you are eligible to vote")
'''
#to check whether the given number is divisible by 5 or not

num=int(input("enter a number: "))
if num%5==0:
    print("the number is divisible by 5")
else:
    print("the number is not divisible by 5")
