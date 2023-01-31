def SelectionSort(numbers):

    for i in range(5):
        MinimumPosition = i
        for j in range(i, 6):
            if numbers[j] < numbers[MinimumPosition]:
                MinimumPosition = j


        temp = numbers[i]
        numbers[i] = numbers[MinimumPosition]
        numbers[MinimumPosition]=temp

        print(numbers)

numbers = [5, 3, 8, 6, 7, 2]

SelectionSort(numbers)

print(numbers)

