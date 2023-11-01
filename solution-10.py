#10. Calculate and print the factorial of a number using a loop.
n = int(input("Enter a number non negative integer : "))
temp=1
if n==0:
    temp=0
elif n>0:
    for i in range(1,n+1,1):
        temp=temp*i
else:
    temp="Factorial is not defined for negative numbers."
print("Factorial is : ",temp)