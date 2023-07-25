import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base):
    return math.log(x, base)

print("Scientific Calculator")

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("0. Exit")

    choice = input("Enter choice (0-7): ")

    if choice == '0':
        print("Calculator closed.")
        break

    if choice not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Invalid choice. Please try again.")
        continue

    if choice in ['1', '2', '3', '4', '5', '7']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero")
            else:
                print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
        elif choice == '7':
            if num1 <= 0 or num2 <= 0:
                print("Error: Invalid input for logarithm")
            else:
                print("Result:", logarithm(num1, num2))

    elif choice == '6':
        num = float(input("Enter a number: "))

        if num < 0:
            print("Error: Invalid input for square root")
        else:
            print("Result:", square_root(num))

    print()
