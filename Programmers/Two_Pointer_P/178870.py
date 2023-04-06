def solution(sequence, k):
    answer = []
    res = 10 ** 7
    start = 0
    end = 0
    total = sequence[end]
    while start <= end and end < len(sequence):
        # 이미 나온 길이보다 길면 길이를 줄인다.
        if end-start >= res:
            total -= sequence[start]
            start += 1
        if total < k:
            end += 1
            if end >= len(sequence):
                break
            total += sequence[end]
        elif total > k:
            total -= sequence[start]
            start += 1
        else:
            answer = [start, end]
            res = end-start
            total -= sequence[start]
            start += 1
            end += 1
            if end >= len(sequence):
                break
            total += sequence[end]
    
    return answer

# 조금 더 효율적으로 진행하기 위해 이미 합 k가 나와서 길이와 범위가 나왔다면 다음에는 그 길이이상이 되지않게 start를 조절해서 진행했음.
# 그래서 아무니 느려봐야 400ms대가 나옴