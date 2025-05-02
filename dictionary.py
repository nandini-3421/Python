#dictionaries are used to store data values in key:value pair
#a dictionary is a collection which is ordered, changeable anddo not allow duplication
#dictionaries are written with curly brackets, and have keys and values:
#creation of a dictionary:
'''
empdata={
    "sameer":"accountant",
    "raj":"IT",
    "raman":"manager"
    }
print(empdata)


vehicalinfo={
    "brand":"toyota",
    "price":"4.5 lakhs",
    "color":"red"
    }
print("my vehical is ",vehicalinfo)


country={
    "India":"Delhi",
    "German":"Berlin",
    "England":"London"
    }
print(country)
print("Capital of India ",country["India"])

country["Italy"]="Rome"
print(country)

del country["German"]
print(country)

#1) shopping cart example to add total value of products

cart={
    "apple":2.5,
    "banana":1.2,
    "milk":3.0
    }

total=0
for item, price in cart.items():
    print(f"{item}:${price}")
    total+=price

print(f"Total: ${total}")
print("Total:",total,"$")
print(f"Total shopiing cost is {total}")

#2) dictionary storing username and password
users={
    "alice":"pass123"
    "bob":"secure456"
    "charlie":"char789"
    }

username=input("enter a username: ") #simulate a login
password=input("enter a password: ")

if username in users:               #check login
    if users[username]==password:
        print("login successful!")
    else:
        print("incorrect password.")
else:
    print("user not found.")

'''
#3) create a weather dictionary ("london":23) ask user to enter city name
#and print result as london has 23 degree celcius now

weather={
    "london":23,
    "delhi":35,
    "paris":19
    }
city=input("enter city name: ")

if city in weather:
    print(f"{city} has {weather[city]} degree celsius now")
else:
    print("weather data for this city is not available")
          



