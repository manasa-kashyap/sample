def show_menu():
    print("*************************")
    print("*  Simple Calculator    *")
    print("*************************")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def calculate():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == '1':
            print(f"Result: {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print(f"Result: {num1 / num2}")

        input("Press Enter to continue...")

calculate()
