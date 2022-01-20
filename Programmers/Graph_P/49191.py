# 내 풀이
from collections import Counter

def solution(n, results):
    answer = 0
    a = [[0] * (n + 1) for _ in range(n + 1)]
    for w, l in results:
        a[w][l] = 1
        a[l][w] = -1
    
    # 플로이드 워셜 알고리즘 실행
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if a[i][j] == 0:
                    # i 가 k를 이기고, k가 j를 이기면 i는 j를 이김.
                    if a[i][k] == 1 and a[k][j] == 1:
                        a[i][j] = 1
                    # 반대의 경우.
                    elif a[i][k] == -1 and a[k][j] == -1:
                        a[i][j] = -1
    # 만약 순위를 정할 수 있다면, a에서 0의 개수가 1개일 것이다(자기자신)
    for i in range(1, n + 1):
        if Counter(a[i])[0] == 2:
            answer += 1

    return answer

# 근데 이 풀이는 Counter와 반복문이 3중이라 시간이 더 오래 걸린다. O(N^3).

# 다른 풀이
from collections import defaultdict

def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for w, l in results:
        win[w].add(l)
        lose[l].add(w)
    
    for i in range(1, n + 1):
        # lose[i]의 값들은 i를 이기는 것(winner)들이 있다.
        # 그러니 i한테 지는 것(win[i])들은 lose[i]의 값들이게도 진다. -> win[winner]에 추가해준다.
        for winner in lose[i]: win[winner].update(win[i])
        # 반대의 경우.
        for loser in win[i]: lose[loser].update(lose[i])

    # 결국 자기자신을 제외한 나머지 것들(n-1개)과의 승패여부를 안다면 순위를 정할 수 있다.
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    
    return answer
# 이 문제는 내가 푼 문제보다 빠르다. O(N ^ 2) 이중 for문이기 때문.