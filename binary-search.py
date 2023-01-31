position = -1 # global variable

def BinarySearch(list, number):

    LowerBound = 0
    UpperBound = len(list) - 1

    while LowerBound <= UpperBound:
        MiddleBound = (LowerBound + UpperBound) // 2 # finding middle bound using the integer division

        if list[MiddleBound] == number:
            globals()['position'] = MiddleBound
            return True
        else:
            if list[MiddleBound] < number:
                LowerBound = MiddleBound + 1
            else:
                UpperBound = MiddleBound - 1
    return False

list = [4, 7, 8, 12, 45, 99, 102, 702, 10987, 56666]
number = 7

if BinarySearch(list, number):
    print("Found at ", position)
else:
    print("Value not Found")
