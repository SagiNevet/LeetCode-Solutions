# score = [5,4,3,2,1]
score = [10,3,8,9,4]

def findRelativeRanks(score):
    answer = [None] * len(score)

    sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])

    for rank, (index, num) in enumerate(sorted_scores):
        if rank == 0:
            answer[index] = "Gold Medal"
        elif rank == 1:
            answer[index] = "Silver Medal"
        elif rank == 2:
            answer[index] = "Bronze Medal"
        else:
            answer[index] = str(rank + 1)

    return answer

print(findRelativeRanks(score))