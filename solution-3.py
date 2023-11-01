#3.Find and print the largest number among three given numbers.
num1, num2, num3 = int(input("Enter first Number : ")), int(input("Enter second Number : ")), int(input("Enter third Number : "))
if num1>=num2 and num1>=num3:
    largest=num1
elif num2>=num1 and num2>=num3:
    largest=num2
else:
    largest=num3
print("Largest number is : ",largest)
