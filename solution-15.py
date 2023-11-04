#15. Calculate the average of a list of numbers.
numbers=[int(i) for i in input("Enter comma separated numbers : ").split(",")]
print("Avarage : ",sum(numbers)/len(numbers))