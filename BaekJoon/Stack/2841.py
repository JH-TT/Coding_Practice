import sys
input = sys.stdin.readline

n, f = map(int, input().split())
finger = 0
m = [[] for _ in range(7)]

for _ in range(n):
    line, fret = map(int, input().split())
    while len(m[line]) and m[line][-1] > fret: # 입력받은 fret이 작으면 fret보다 큰 수가 있을때까지 손을 뗀다.
        m[line].pop()
        finger += 1
    if m[line] and m[line][-1] == fret: # 같은음을 연주하는거는 넘긴다.
        continue
    m[line].append(fret) # 그 외에는 줄을 누른다.
    finger += 1
print(finger)