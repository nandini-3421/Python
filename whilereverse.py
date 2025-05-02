#prog to reverse a nmber and to check whether it is a palindrome or not 
'''
rev=0
n=int(input("enter a number"))
temp=n
while(n>0):
    rem=n%10
    rev=rev*10+rem      #recursive
    n=n//10             #quotient
    print(rev)
print("the reverse of a number is: ",rev)
if(rev==temp):
    print("the number is palindrome")
else:
    print("the number is not a palindrome")
'''

#program to get sum of digits (e.g 243 sum= 9)
'''
s=0
num=int(input("enter a number "))
temp=num
while(num>0):
    rem=num%10
    s=s+rem
    num=num//10
    
print("the addition of digits is ",s)
'''
#to check whether the number is armstrong

arm=0
n=int(input("enter a number"))
temp=n
while(n>0):
    rem=n%10
    arm=arm+rem*rem*rem
    n=n//10
print("the number addition is ",arm)
if(arm==temp):
    print("the number is armstrong")
else:
    print("the number is not armstrong")
