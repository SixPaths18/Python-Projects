number1 = int(input("Enter a number: "))   # User inputs a number
operation = input("Enter an operation(+, -, *, /): ")   # User inputs an operation
number2 = int(input("Enter another number: "))   # User inputs another number

if operation == "+":   # Adittion of number1 and number2
    print(number1, operation, number2, "=", number1 + number2)

elif operation == "-":   # Subtraction of number1 and number2
    print(number1, operation, number2, "=", number1 - number2)

elif operation == "*":   # Multiplication of number1 and number2
    print(number1, operation, number2, "=", number1 * number2)

elif operation == "/":   # Division of number1 and number2
    print(number1, operation, number2, "=", number1 / number2)