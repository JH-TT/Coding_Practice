import sys
input = sys.stdin.readline

number = [2, 5, 5, 4, 5, 6, 3, 7, 6, 6]

T = int(input())

res = [[10**26, ""] for _ in range(101)]
res[2] = ["1", "1"]
res[3] = ["7", "7"]
res[4] = ["4", "11"]
res[5] = ["2", "71"]
res[6] = ["6", "111"]
res[7] = ["8", "711"]

for i in range(8, 101):
    # 2부터 i의 절반값까지 for문을 돌면서 최솟값의 경우를 모두 구하고 그 중에 최솟값을 최솟값으로 지정한다.
    for j in range(2, i//2 + 1):
        mini = list(res[j][0] + res[i - j][0])
        mini.sort()
        # 맨 앞이 0이면 0이 아닌 가장 작은 수와 교환한다.
        if mini[0] == "0":
            for h in range(1, len(mini) - 1):
                if mini[h] != "0":
                    mini[0], mini[h] = mini[h], mini[0]
                    break          
        mini = "".join(mini)
        # 맨 앞을 제외한 나머지 자리에 6을 전부 0으로 바꾼다.
        mini = mini[0] + mini[1:].replace("6", "0")
        res[i][0] = str(min(int(res[i][0]), int(mini)))
    # 최댓값은 i-2개로 했을때 최댓값에 1을 계속 추가해 준다.(문자열)
    res[i][1] = res[i - 2][1] + res[2][1]

for n in range(T):
    n = int(input())
    
    print(res[n][0], res[n][1])


# 다른 사람의 풀이
from sys import stdin as f

T = int(f.readline())
num = [0,0,1,7,4,2,0,8,10] # 가장 앞자리만 6이고 나머지는 0이므로 인덱스 6의 값이 0인것이다.
dp = [-1 for i in range(101)]
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 7
dp[4] = 4
dp[5] = 2
dp[6] = 6
dp[7] = 8


def find_min(n):
    if dp[n] == -1:
        dp[n] = min([10*find_min(n-i)+num[i] for i in range(2,8)])
    return dp[n]

def find_max(n):
    res = '1' * (n//2 - 1)
    return '7'+res if n % 2 else '1'+res
for test_case in range(T):
    n = int(f.readline())
    print(find_min(n),find_max(n))
# 이 풀이는 최솟값을 2 ~ 7개가 남는다는 가정으로 경우의 수를 모두 구해서 그 중에 최솟값을 최솟값으로 지정했다.        