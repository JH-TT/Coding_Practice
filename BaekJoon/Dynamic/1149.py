n = int(input()) # 몇개의 집인지 입력받음.

rst = [] # 결과값 받을 공간.
r, g, b = map(int, input().split())
rst.append((r, g, b)) # 첫번째 집의 RGB입력.
for _ in range(1, n):
    r, g, b = map(int, input().split()) # 현재 집의 RGB입력 받음.
    pR, pG, pB = rst[-1] # 그 전 RGB출력
    # 현재 r + min(이전G, 이전B).
    R = r + min(pG, pB)
    G = g + min(pR, pB)
    B = b + min(pR, pG)
    rst.append((R, G, B))
fR, fG, fB = rst[-1] # 마지막 RGB출력.
print(min(fR, fG, fB)) # 그 중 최솟값 출력.