import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
VISITED_ALL = (1 << n) - 1 # 전부 방문하면 1111 이런식

cache = [[None] * (1 << n) for _ in range(n)] # dp를 이용할 이중리스트 cache[city][visit] 형태이다.
INF = float('inf')

def TSP(last, visit):
    # 다 방문했으면 마지막으로 0으로 오는 길이 있는지 확인.
    # 있으면 그 가중치를 리턴하고 없으면 무한대값을 리턴해서 답이 될 수 없도록 한다.
    if visit == VISITED_ALL:
        return arr[last][0] or INF
    # cache값이 None이 아니라는 것은 이미 구했다는 의미. 그러니 바로 리턴해준다.
    if cache[last][visit] is not None:
        return cache[last][visit]

    # 현재 도시에서 다른 도시로 가는 최소거리를 구한다.
    tmp = INF
    for city in range(n):
        if visit & (1 << city) == 0 and arr[last][city] != 0:
            tmp = min(tmp, TSP(city, visit | (1 << city)) + arr[last][city])
    cache[last][visit] = tmp # 그 값을 cache에 넣어준다.
    return tmp

print(TSP(0, 1 << 0))

# 참고 : https://velog.io/@kimdukbae/BOJ-2098-%EC%99%B8%ED%8C%90%EC%9B%90-%EC%88%9C%ED%9A%8C-Python
# 진행 순서를 보면 탑다운 형식인듯