nums = [1,2,2,3,1,4]
# nums = [1,2,3,4,5]

def maxFrequencyElements(nums):
    frequency = 0
    result = 0

    for i in range(len(nums)):
        count = 1
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
        if count > frequency:
            frequency = count
    
    for i in range(len(nums)):
        count = 1
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
        if count == frequency:
            result += count

    return result

print(maxFrequencyElements(nums))