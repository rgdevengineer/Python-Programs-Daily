
# Polymorphism with Iterables
# Write a function length() that can return the length of a list, string, or tuple.

def length(item):
    return len(item)

print(length("Python"))
print(length([1,2,3]))
print(length((1,2)))

