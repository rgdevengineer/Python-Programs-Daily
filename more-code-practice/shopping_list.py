
'''
Shopping List
You’re building a shopping list feature in a grocery app. You need to support various list operations such as adding items, removing them, merging with others, and handling user inputs from text.

Tasks:

Create a grocery list named my_cart with the items: "apples", "bananas", and "milk"

Print the grocery list.

Add "bread" to the end of the list.

Print the updated grocery list.

Insert "ketchup" at the beginning of the list.

Print the updated grocery list.

Remove "bananas" from the list.

Print the updated grocery list.

Remove the last item from the list and store it in a variable named removed_item.

Print the value of removed_item.

Extend the grocery list by adding "rice" and "butter".

Print the updated grocery list.

Sort the grocery list in alphabetical order.

Print the updated grocery list.

Reverse the order of the grocery list.

Print the updated grocery list.

Concatenate the grocery list with another list containing "juice" and "jam".

Print the resulting list.

Duplicate the grocery list twice.

Print the resulting list.

Define a string with the value "tomato cucumber spinach" and convert it into a list.

Print the converted list.
'''

my_cart = ["apples", "bananas", "milk"]

print("Initial cart:", my_cart)

my_cart.append("bread")

print("After adding bread:", my_cart)

my_cart.insert(0, "ketchup")

print("After inserting ketchup:", my_cart)

my_cart.remove("bananas")

print("After removing bananas:", my_cart)

removed_item = my_cart.pop()

print("Removed last item:", removed_item)

my_cart.extend(["rice", "butter"])

print("After extending with rice and butter:", my_cart)

my_cart.sort()

print("After sorting alphabetically:", my_cart)

my_cart.reverse()

print("After reversing:",my_cart)

new_list = my_cart + ["juice", "jam"]

print("After concatenation:", new_list)

duplicated_cart = my_cart * 2

print("duplicated grocery list:", duplicated_cart)

veg_string = "tomato cucumber spinach"
veg_list = veg_string.split()

print("Converted vegetable list:", veg_list)
