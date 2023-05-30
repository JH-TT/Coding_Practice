def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    
    # arr1의 행
    for i in range(len(arr1)):
        for j in range(len(arr2[0])): # arr2의 열
            total = 0
            for k in range(len(arr2)):
                total += arr1[i][k] * arr2[k][j]
            answer[i].append(total)
    
    return answer

    # 추가! 한줄 코드
    return [list(sum(a*b for a, b in zip(arr1_row, arr2_col)) for arr2_col in zip(*arr2)) for arr1_row in arr1]
    # zip(*arr2)를 하면 arr2가 언패킹에 의해 각 행의 같은 열끼리 묶이게 된다. 즉 column끼리 묶이게 된다는 뜻