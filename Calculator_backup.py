while True:
    print("\n===== SMART CALCULATOR =====")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose operation: ")

    if choice == "1":
        print("Answer:", a + b)

    elif choice == "2":
        print("Answer:", a - b)

    elif choice == "3":
        print("Answer:", a * b)

    elif choice == "4":
        if b != 0:
            print("Answer:", a / b)
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid choice")

    again = input("\nCalculate again? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you!")
        break