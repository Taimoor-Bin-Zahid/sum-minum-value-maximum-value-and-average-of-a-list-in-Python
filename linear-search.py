# Using While loop...................................................

position = -1  # global variable

def LinearSearch(list, number):
    i = 0

    while i < len(list):
        if list[i] == number:
            globals()['position'] = i
            return True
        i = i + 1

    return False

list = [5, 8, 4, 6, 9, 2]
number = 4

if LinearSearch(list, number):
    print("Found at ", position)
else:
    print("Not Found!")

#  Using For Loop....................................................

#Linear Search for a value in the list using for loop and function.

indexposition = -1
def search(list, n):

    for i in range(len(list)):
        if list[i] == n:
            globals()['indexposition'] = i
            return True
    else:
        return False

list = [23,12,73,33,19]
n = 19
if search(list, n):
    print("Value is",n,"and is found at position no.", indexposition)
else:
    print("Value is",n,"and Not found in the list, try again")