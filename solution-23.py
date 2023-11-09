#23. Write a program to check if a number is a perfect number.
n=int(input("Enter a number : "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
print("Perfect Number" if n==sum else "Not Perfect Number",sum)