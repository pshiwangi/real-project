menu = {
    'pizza': 40,
    'pasta': 35,
    'burger': 50,
    'dessert': 25,
    'drink': 15,
    'salad': 34,
    'cookies': 10,
    'fruit': 12,
    'pastries': 20,
}

print(menu)

print("welcome to Deep restaurant")
print("pizza: rs40\npasta: rs35\nburger: rs50\ndessert: rs25\ndrink: rs15\nsalad: rs34\ncookies: rs10\nfruit: rs12\npastries: rs20")
print(menu)

order_totel = 0

item_1 = input("Enter the name of itme you want to order = ")
if item_1 in menu:
 order_totel+= menu[item_1] #0 +40
print(f"your item {item_1} has been added to your order")

another_order = input("Do you want to add another item? (Yes?No) ")

if another_order == "No": 
   
    print(f"The total amount of items is to pay {order_totel}")
   
   
item_2 = input("Enter the name of itme you want to order = ")
if item_2 in menu:
 order_totel+= menu[item_2] #0 +35
 print(f"Order item { item_2 }has been added to your order")
else:
    print(f"Ordered item{item_2} is not avaialable!")

another_order = input("Do you want to add another item? (Yes?No) ")
if  another_order == "Yes":
    item_2 = input("Enter the name of itme you want to order = ")
    if item_2 in menu:
        order_totel += menu[item_2]
    print(f"your item {item_2} has been added to your order")
else:
    print(f"Ordered item{item_2} is not avaialable!")

    print(f"The total amount of items is to pay {order_totel}")

    

