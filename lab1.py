#to find the greatest number among two numbers
'''
num1=int(input("enter a first number: "))
num2=int(input("enter second number: "))
if num1>num2:
    print("the greatest number is: ",num1)
else:
    print("the greatest number is: ",num2)


#to find whether person is eligible to vote or not

age=int(input("enter your age: "))
if age<18:
    print("you are not eligible to vote")
else:
    print("congratulations you are eligible to vote")

#to check whether the number is even or odd

num=int(input("enter a number: "))
if(num%2==0):
    print("the number is even")

else:
    print("the number is odd")
'''
#to accept basic salary from user and give 10% of DA on basic salary,
#12% HRA on basic salary to employee if the salary is more than 50000.
#calculate total salary

salary=float(input("enter your basic salary:"))
da=0
hra=0
if salary>54000:
    da=0.10*salary
    hra=0.12*salary

    print("your total salary is:",salary+da+hra)
    
else:
    print("your salary is", salary)
