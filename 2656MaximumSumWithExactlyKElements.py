# nums = [1,2,3,4,5]
# k = 3

nums = [5,5,5]
k = 2


def maximizeSum(nums, k):
    sum = 0
    count = 0
    i = 0
    while count != k:
        index = i % len(nums)
        if nums[index] == max(nums):
            sum += max(nums)
            nums[index] += 1
            count += 1
        i += 1
    return sum

print(maximizeSum(nums, k))
print(nums)