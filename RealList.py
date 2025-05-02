#You’re building a shopping cart feature in an e-commerce app.
#Here’s how Python lists are used in real-time.

# Initial cart with products
shopping_cart = ["laptop", "mouse", "keyboard"]

# Add an item to the cart
shopping_cart.append("headphones")
print("Cart after adding an item:", shopping_cart)

#Remove an item from the cart
shopping_cart.remove("mouse")
print("Cart after removing an item:", shopping_cart)

#Check if an item is in the cart
if "keyboard" in shopping_cart:
    print("Keyboard is in the cart!")

#Count how many times an item appears
shopping_cart.append("laptop")  # Customer added another laptop
laptop_count = shopping_cart.count("laptop")
print("Number of laptops in cart:", laptop_count)

# Show total number of items
print("Total items in cart:", len(shopping_cart))

# Loop through items to display them
print("Items in cart:")
for item in shopping_cart:
    print("-", item)
