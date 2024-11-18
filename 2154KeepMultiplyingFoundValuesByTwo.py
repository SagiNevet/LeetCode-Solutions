nums = [5,3,6,1,12]
original = 3

def findFinalValue(nums, original):
    i = 0
    while original in nums:
        original *= 2
    return original

print(findFinalValue(nums, original))
