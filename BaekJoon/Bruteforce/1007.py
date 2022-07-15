from itertools import combinations
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    cor = []
    mini = sys.maxsize
    x_ = 0
    y_ = 0
    for _ in range(n):
        a, b = map(int, input().split())
        x_ += a
        y_ += b
        cor.append([a, b])

    combi = list(combinations(cor, n//2)) # 절반은 뺄 좌표들
    for i in combi[:len(combi)//2]:
        print(i)
        # 빼는놈들
        sub_x = 0
        sub_y = 0
        for x, y in i:
            sub_x += x
            sub_y += y
      
        d = ((x_ - 2*sub_x)**2 + (y_ - 2*sub_y)**2) ** (0.5) # 벡터 총 합 길이
        mini = min(mini, d)

    print(mini)

# line 18 -> 절반만 보는이유.. : (x - y) ** 2 == (y - x) ** 2 와 같은 원리.
# ex) 점이 abcd가 있으면 거기서 2개를 뽑는다 하자.
# 모든 경우의 수는 -> (a, b) (a, c) (a, d) (b, c) (b, d) (c, d) 인데,
# 주석 첫번째를 보면, 제곱을 할때는 서로 순서가 달라도 결과가 같다 라는것을 생각했을때
# (a, b)를 뽑았을때의 값과 (c, d)를 뽑았을떄의 값이 같게된다.
# 즉 (x1+x2+x3+x4+...+xi-y1-y2-y3-...yi)**2 == (y1+y2+y3+...+yi-x1-x2-x3-...-xi)**2 이다.
# 좌항은 (y1, y2, ..., yi)의 점을 뽑은 경우고, 우항은 (x1, x2, x3, ..., xi)를 뽑은 경우이므로 겹치게 된다는것.
# 이를 생각해서 짝지어보면 정확히 모든경우의 수의 절반이 나오고 따라서 combination의 절반만 확인하는것이다.