number = int(input('Enter The Number of Elements: '))

listOne = list()

for i in range(number):
    elements = int(input("Enter the number: "))
    listOne.append(elements)


SumOne = sum(listOne)
MinimumOne = min(listOne)
MaximumOne = max(listOne)
AverageOne = SumOne / len(listOne)


print("Sum of numbers is: ", SumOne)
print("Minimum of Numbers is: ", MinimumOne)
print("Maximum of Numbers is: ", MaximumOne)
print("Average of Numbers is: ", AverageOne)
