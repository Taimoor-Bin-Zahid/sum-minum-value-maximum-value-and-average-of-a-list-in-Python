def BubbleSort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [5, 3, 8, 7, 2, 33, 57, 7, 10101, 100, 200, 150, 140, 8]
BubbleSort(nums)

print(nums)