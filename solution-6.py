#6. Write a program to check if a number is positive, negative, or zero.
num = int(input("Enetr a number : "))
if num==0:
    print("zero.")
elif num>0:
    print("positive.")
elif num<0:
    print("negative.")
else:
    print("invalid input.")