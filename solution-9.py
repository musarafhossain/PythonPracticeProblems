#9.	Check if a string is a palindrome (reads the same forwards and backwards).
string = input("Enter a string : ")
"""
loop=len(string)//2
l=len(string)-1
a=False
for i in range(loop):
    if string[i]==string[l]:
        a=True
    else:
        break
    l-=1
if(a):
    print("Palindrom")
else:
    print("Not Palindrom")
"""
if string==string[::-1]:
    print("Palindrom")
else:
    print("Not Palindrom")