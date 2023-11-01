#7. Write a Python program to swap the values of two variables.
num1, num2 = int(input("Enter num1 : ")), int(input("Enter num2 : "))
temp=num1
num1=num2
num2=temp
print("num1 :",num1," num2 :",num2)