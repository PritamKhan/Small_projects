def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

# Main calculator function
def calculator():
    print("Arithmetic Calculator")
    print("Select operation:")

    choice = input("Enter choice | + | - | * | / | \n ")

    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '-':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '*':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '/':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid input. Please enter a valid choice.")
    else:
        print("Invalid input. Please enter a valid choice.")

# Run the calculator
calculator()
