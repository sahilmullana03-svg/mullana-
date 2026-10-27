#Mini Calculator Code
# Simple Calculator Program

# User se input lena
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation: +, -, *, /")
operation = input("Enter operation: ")

# Conditions check karna
if operation == "+":
    print("Result =", num1 + num2)
elif operation == "-":
    print("Result =", num1 - num2)
elif operation == "*":
    print("Result =", num1 * num2)
elif operation == "/":
    if num2 != 0:   # Zero division check
        print("Result =", num1 / num2)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operation")

