# nums = [2,1,3,5,6]
# k = 5
# multiplier = 2
# nums = [1,2]
# k = 3
# multiplier = 4

nums = [2,2,3,2]
k = 5
multiplier = 3

def getFinalState(nums, k, multiplier):
    count = 0
    i = 0
    currentMin = 0
    while count < k:
        index = i % len(nums)
        currentMin = min(nums)

        if nums[index] == currentMin:
            nums[index] *= multiplier
            count += 1
        i += 1
        if currentMin != min(nums):
            i = 0
            currentMin = min(nums)

    return nums

print(getFinalState(nums, k, multiplier))