
# Set Operations Tool

def input_set(prompt):
    return set(input(prompt).split())

def set_operations():
    A = input_set("Enter Set A (space-separated): ")
    B = input_set("Enter Set B (space-separated): ")

    print(f"\nSet A: {A}")
    print(f"Set B: {B}")
    print("\nSet Operations Results:")
    print(f"Union: {A | B}")
    print(f"Intersection: {A & B}")
    print(f"Difference (A - B): {A - B}")
    print(f"Symmetric Difference: {A ^ B}")

set_operations()
