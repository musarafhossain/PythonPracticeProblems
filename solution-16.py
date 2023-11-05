#16. Create a program to convert temperatures between Celsius and Fahrenheit.
#Formula --> [( °F = °C * 9/5) + 32] [°C = (°F - 32) * 5/9]
def celtoFah():
    cel=float(input("Enter Temperature in Celcius : "))
    fah=(cel*9/5)+32
    return fah

def fahtoCel():
    fah=float(input("Enter Temperature Fahrenheit : "))
    cel=(fah-32)*5/9
    return cel

while 1:
    ch=int(input("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Exit\nEnter your choice : "))
    if ch==1:
        print("Tenperature in Fahrenheit :",celtoFah())
    elif ch==2:
        print("Temperature in Celsius :",fahtoCel())
    elif ch==3:
        exit()
    else:
        print("Invalid Input")