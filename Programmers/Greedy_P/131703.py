import copy

def solution(beginning, target):
    b1 = copy.deepcopy(beginning)
    b2 = copy.deepcopy(beginning)
    b3 = copy.deepcopy(beginning)
    b4 = copy.deepcopy(beginning)
    answer = min(case_1(b1, target), case_2(b2, target), case_3(b3, target), case_4(b4, target))
    return answer if answer != 10**7 else -1

def case_1(b, t):
    res = 0
    # 행이 다르면 뒤집는다.
    for i in range(len(b)):
        if b == t:
            return res
        if b[i][0] != t[i][0]:
            change_row(b, i)
            res += 1
    # 열이 다르면 뒤집는다.
    for i in range(len(b[0])):
        if b == t:
            return res
        if b[0][i] != t[0][i]:
            change_col(b, i)
            res += 1
    if b == t:
        return res
    return 10**7

def case_2(b, t):
    res = 0
    # 같으면 뒤집는다.
    for i in range(len(b)):
        if b == t:
            return res
        if b[i][0] == t[i][0]:
            change_row(b, i)
            res += 1  
    # 열이 다르면 뒤집는다.
    for i in range(len(b[0])):
        if b == t:
            return res
        if b[0][i] != t[0][i]:
            change_col(b, i)
            res += 1
    if b == t:
        return res
    return 10**7 # t를 못만듦

def case_3(b, t):
    res = 0
    for i in range(len(b[0])):
        if b == t:
            return res
        if b[0][i] != t[0][i]:
            change_col(b, i)
            res += 1
    for i in range(len(b)):
        if b == t:
            return res
        if b[i][0] != t[i][0]:
            change_row(b, i)
            res += 1
    if b == t:
        return res
    return 10**7

def case_4(b, t):
    res = 0
    for i in range(len(b[0])):
        if b == t:
            return res
        if b[0][i] == t[0][i]:
            change_col(b, i)
            res += 1
    for i in range(len(b)):
        if b == t:
            return res
        if b[i][0] != t[i][0]:
            change_row(b, i)
            res += 1
    if b == t:
        return res
    return 10**7

def change_row(arr, idx):
    arr[idx] = [(arr[idx][a] + 1) % 2 for a in range(len(arr[idx]))]

def change_col(arr, idx):
    for i in range(len(arr)):
        arr[i][idx] = (arr[i][idx] + 1) % 2

# 이 문제는 완탐이긴 한데 아예 전부볼 필요가 없던 문제였다.
# 첫번째 행과 첫번째 행의 열들만 확인하면 되는 문제다.
# 케이스가 4가지가 있는데
# 1. 행이 다르면 뒤집고, 다음에 열이 다르면 뒤집는다.
# 2. 행이 같으면 뒤집고, 다음에 열이 다르면 뒤집는다.
# 3. 열이 다르면 뒤집고, 다음에 행이 다르면 뒤집는다.
# 4. 열이 같으면 뒤집고, 다음에 행이 다르면 뒤집는다.

# 이 4가지중에 최솟값이 답이되고 저 케이스들을 돌아도 못찾으면 -1을 리턴한다. 

# 다른사람 풀이

def solution(beginning, target):
    answer = 0
    table = [[beginning[i][j] ^ target[i][j] for j in range(len(beginning[i]))] for i in range(len(beginning))]
    cnt = 0
    m = len(table)
    n = len(table[0])

    for i in range(1, m):
        if (table[i] != table[0]):
            cnt+=1
            if (list(map(lambda x: x ^ 1, table[i])) != table[0]):
                return -1

    answer = min((cnt) + sum(table[0]), (m - cnt) + (n - sum(table[0])))

    return answer

# 이 문제는 beginning과 target의 다른 부분만 1로 두어서 새로운 테이블을 생성한다.
# 첫번째 행과 비교해서 다르면 뒤집는다.
#   이때 뒤집었는데 첫 번째 행과 다르면 이는 못찾는 배열이되고 -1을 리턴한다.
#   그게 아니면 cnt를 증가시킨다.
# 만약 끝까지 가면 각 행은 같은 모습을 가지고 있을것이다.
# 이때 구하는 가짓수는 min(첫번째 행과 다른 행 뒤집기 + 1로 이뤄진 열 뒤집기, 첫번째 행과 다른 행을 그대로 두고 반대로 첫번째 행과 나머지를 뒤집기 + 1로 이뤄진 열 뒤집기)가 된다. 이를 표현한 코드가 answer 부분이다.


# 완탐정도는 알고 있었지만 나는 백트래킹으로 구현하려고 했다.
# 그런데 dfs함수에 리스트를 넘기면 다음 dfs의 배열은 이전 dfs의 배열을 "참조"하고 있기 때문에 배열이 계속 변했다.
# 이 부분을 처리하지못해 풀지 못한 문제다.