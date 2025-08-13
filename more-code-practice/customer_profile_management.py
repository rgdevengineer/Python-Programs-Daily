
'''
Customer Profile Management
You are building a customer profile manager for a CRM (Customer Relationship Management) system. You need to store and manipulate customer data using Python dictionaries.
Tasks:
Create a dictionary named customer with the following fields:
"name": "John Doe"
"age": 32
"city": "New York"
Print the dictionary.
Add "email" and "phone" to the dictionary.
Print the updated dictionary.
Print the customer’s "name" and "city" values.
Check whether the key "email" exists in the dictionary and print the result.
Delete the "age" field from the dictionary.
Print the updated dictionary.
Print all dictionary keys, values, and items.
Remove and print the last inserted key-value pair.
Use .get() to access the key "membership" (which doesn’t exist).
Print the result.
Update the dictionary with a new field "address" set to "221B Baker Street".
Print the final dictionary.
'''


customer = {"name": "John Doe", "age": 32, "city": "New York"}
print(customer)

customer["email"] = "john.doe@example.com"
customer["phone"] = "123-456-7890"
print(customer)

print(customer["name"])
print(customer["city"])

print("email" in customer)

del customer["age"]

print(customer)
print(customer.keys())
print(customer.values())
print(customer.items())

last_item = customer.popitem()
print(last_item)

member = customer.get("member")
print(member)

address = {"address": "221B Baker Street"}
customer.update(address)
print(customer)