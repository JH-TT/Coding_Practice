def solution(a):
    if len(a) < 3:
        return len(a)
    mini = min(a)
    INF = float('inf')
    
    # 왼쪽부터
    start = INF
    cnt = 0
    for i in range(len(a)):
        if a[i] == mini:
            break
        if a[i] < start:
            start = a[i]
            cnt += 1
    start2 = INF
    cnt2 = 0
    for i in range(len(a)-1, -1, -1):
        if a[i] == mini:
            break
        if a[i] < start2:
            start2 = a[i]
            cnt2 += 1
    
    return cnt + cnt2 + 1

# 풍선이 살아남을 수 있는 상황
# 해당 풍선 좌측과 우측 둘 다 해당 풍선의 숫자보다 작은 풍선이 있으면 안된다.
# 시작값과 끝값은 상관없음 
# 즉, left -> right, right -> left 방향으로 훑으면서 최솟값이 갱신되면 answer에 1을 추가하는 방식으로 한다. 