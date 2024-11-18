arr = [0,2,1,-6,6,-7,9,1,2,0,1]

def canThreePartsEqualSum(arr):
    total_sum = sum(arr)

    if total_sum % 3 != 0:
        return False

    target = total_sum // 3
    current_sum = 0
    partitions = 0

    for num in arr:
        current_sum += num
        if current_sum == target:
            partitions += 1
            current_sum = 0
            if partitions == 3:
                return True

    return False

print(canThreePartsEqualSum(arr))