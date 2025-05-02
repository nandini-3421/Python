#list: in pyton, a list is a built- in data type used to store multiple
#items in a single variable. lists are ordered, changeable (mutable),
#and allow duplicate values
#creating a list
#list also can contain null values

emp=["Sam","Ram","Shyam","Ghanashyam"]
stud=[1,"Ramesh","malad","O Grade"]

print(emp)
print("the list of student rexord",stud)
print("the final list of students is: ",stud)


#you can access individual value using index
#indexing of the list start with zero
print(emp[0])
print(stud[2])
print(stud[-1])

#updating list
emp[2]="raghav"
print(emp)


#create list with five elements and find minimum among it

list=[45,56,23,2,67]

minimum=list[0]
for i in list:
    if i>minimum:
        minimum=i
print("the minimum is ",minimum)

#to find maximum in list 
list=[45,56,23,2,67]

maximum=list[0]

for i in list:
    if i>maximum:
        maximum=i
print("the maximum is ",maximum)
