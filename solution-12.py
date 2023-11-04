#12. Check if a number is prime and print the result.
n=int(input("Enter a Number : "))
con = False if n<=0 else True
for i in range(2,n,1):
    if n%i==0:
        con=False
        break
print("Prime number.") if con else print("Not a prime number.")