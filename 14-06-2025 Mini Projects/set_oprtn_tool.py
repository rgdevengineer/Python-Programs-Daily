
# Set Operations Tool

def input_set(prompt):
    return set(input(prompt).split())

def set_operations():
    A = input_set("Enter Set A (space-separated): ")
    B = input_set("Enter Set B (space-separated): ")
    
    while True:
        print("\n--- Set Operations Menu ---")
        print("1. Union (A | B)")
        print("2. Intersection (A & B)")
        print("3. Difference (A-B)")
        print("4. Symmetric Difference (A ^ B)")
        print("5. Check Subset")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("Union:", A | B)
        elif choice == '2':
            print("Intersection:", A & B)
        elif choice == '3':
            print("A - B:", A - B)
            print("B - A", B - A)
        elif choice == '4':
            print("Symmetric Difference:", A ^ B)
        elif choice == '5':
            print("A is subsetof B:", A.issubset(B))
            print("B is subset of A:", B.issubset(A))
        elif choice == '6':
            print("Exiting the tool")
            break
        else:
            print("Invalid choice.Please try again.")

#     print(f"\nSet A: {A}")
#     print(f"Set B: {B}")
#     print("\nSet Operations Results:")
#     print(f"Union: {A | B}")
#     print(f"Intersection: {A & B}")
#     print(f"Difference (A - B): {A - B}")
#     print(f"Symmetric Difference: {A ^ B}")

set_operations()
