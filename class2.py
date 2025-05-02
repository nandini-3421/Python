#Area of circle

class circle:
    def __init__(self,pi,r):
        self.pi=pi
        self.r=r
    def area(self):
        return self.pi*self.r*self.r
pi=float(input("enter value of pi: "))
r=int(input("enter value of radius: "))

aoc=circle(pi,r)
ans=aoc.area()
print("the area of circle is: ",ans)

#calculate simple interest

class si:
    def __init__(self,principal,rate,time):
        self.principal=principal
        self.rate=rate
        self.time=time
    def interest(self):
        return (self.principal*self.rate*self.time)/100

principal=int(input("enter principal amount: "))
rate=int(input("enter interest rate: "))
time=int(input("enter time(in years): "))

intt=si(principal,rate,time)
ans=intt.interest()
print("the simple interest for given data is: ",ans)

#

    
