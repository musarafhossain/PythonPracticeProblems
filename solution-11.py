#11. Generate the first n numbers in the Fibonacci sequence.
n=int(input("Enter a Number : "))
x=0
for i in range(1,n+1,1):
    x=x+i
    print(x,end=" ")