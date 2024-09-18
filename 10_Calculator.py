# Python calculator

operator = input("Enter an operator (+ - * /) :")
num1 =float(input("number1 = "))
num2 =float(input("number2 = "))

if operator == "+" :
    print(f"{num1} + {num2} = ",num1+num2)
elif operator == "-":
    print(f"{num1} - {num2} = ", num1 - num2)
elif operator == "*":
    print(f"{num1} * {num2} = ", num1 * num2)
elif operator == "/":
    print(f"{num1} / {num2} = ", num1 / num2)
else:
    print("Try Again!")
