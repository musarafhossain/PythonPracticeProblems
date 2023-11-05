#17. Calculate the sum of natural numbers up to a given value using a loop.
n=int(input("Enter a number : "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("Sum is ",sum)