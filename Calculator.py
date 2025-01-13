welcome = "welcome to the calculator"
print(welcome.upper())

print("Select any of the options:\n")

while 1:
    print("Select any of the options:\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Reminder")
    print("6. Exit")

    selection = int(input("Enter your selection:\n"))

    if selection == 1:
        number1 = int(input("Enter your first number: "))
        number2 = int(input("Enter your Second number: "))
        print("The Sum: ", number1 + number2)
    elif selection == 2:
        number1 = int(input("Enter your first number: "))
        number2 = int(input("Enter your Second number: "))
        print("The Difference: ", number1 - number2)
    elif selection == 3:
        number1 = int(input("Enter your first number: "))
        number2 = int(input("Enter your Second number: "))
        print("The Product: ", number1 * number2)
    elif selection == 4:
        number1 = int(input("Enter your first number: "))
        number2 = int(input("Enter your Second number: "))
        print("The Quotient: ", number1 / number2)
    elif selection == 5:
        number1 = int(input("Enter your first number: "))
        number2 = int(input("Enter your Second number: "))
        print("The Reminder: ", number1 % number2)
    elif selection == 6:
        print("Exiting.")
        break
    print()

    