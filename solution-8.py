#8. Create a simple calculator program that can add, subtract, multiply, or divide two numbers.
num1, operator, num2 = float(input("Enter First Number : ")), input("Enter oprator (+,-,*,/) : "), float(input("Enter Second Number : "))
if operator=="+":
    print("Sum is :",num1+num2)
elif operator=="-":
    print("Subtraction is :",num1-num2)
elif operator=="*":
    print("Multiplication is :",num1*num2)
elif operator=="/":
    print("Division is :",num1/num2)
else:
    print("Invalid Input")