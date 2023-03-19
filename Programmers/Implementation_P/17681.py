def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        bi = bin(a|b)[2:]
        bi = " " * (n-len(bi)) + bi
        bi = bi.replace("1", "#")
        bi = bi.replace("0", " ")
        answer.append(bi)
    
    return answer

# 좀 더 효율적인 방법?
def solution(n, arr1, arr2):
    answer = []
    s = ''
    for i in range(n):
        bi = bin(arr1[i]|arr2[i])[2:]
        bi = " " * (n-len(bi)) + bi
        s += bi
    
    s2 = ''
    for i in s:
        if i == "0":
            s2 += " "
        elif i == "1":
            s2 += "#"
        else:
            s2 += i
        if len(s2) == n:
            answer.append(s2)
            s2 = ''
    
    return answer

# 코드 자체는 길어졌지만 처음에 작성한 코드는 replace가 선형탐색이다보니 O(N^2)의 시간까지 갈 수 있지만
# 아래 코드는 for문을 2개로 나눠서 처리했기 때문에 O(N)이다.