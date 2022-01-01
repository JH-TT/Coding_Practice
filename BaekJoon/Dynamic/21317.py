import sys
input = sys.stdin.readline
INF = float('inf') # 최솟값을 계속 업데이트 시켜주는 것이지 때문에 최댓값을 미리 선언해 준다.

n = int(input())

jump = [] # 점프할때 드는 에너지 저장하는 리스트
energy =  [[0, 0]] + [[INF, INF] for _ in range(n-1)] # 현재 돌까지 가는데 드는 에너지 저장하는 리스트.

for _ in range(n - 1):
    a, b = map(int, input().split())
    jump.append([a, b])
k = int(input()) # 매우 큰 점프를 사용할 때 드는 에너지.

# 초기화 하는 부분.
if n > 1:
    energy[1][0] = min(energy[0][0] + jump[0][0], energy[1][0])

if n > 2:
    energy[2][0] = min(energy[1][0] + jump[1][0], energy[0][0] + jump[0][1], energy[2][0])

# 크게 2가지가 있다.
# 1. 매우 큰 점프를 아직까지 사용하지 않은 경우 : 인덱스 0에 들어갈 값
# 2. 매우 큰 점프를 사용했거나, 이제 사용할 경우 : 인덱스 1에 들어갈 값

# 전자는 위에 두 조건문처럼 해주면됨.
# 후자는 또 2가지로 나뉘는데, 이미 매우 큰 점프를 사용한 상태, 이제 매우 큰 점프를 사용할 상태 이 중에 최솟값으로 업데이트
# 이미 매우 큰 점프를 사용했으면, energy의 오른쪽 값들을 전자와 같은 방식으로 해주고 + 사용할 상태는 두 칸 뒤에 있는 돌의 왼쪽 값 + k를 해준다. 이 중에 최솟값으로 업데이트.
for i in range(3, n):
    energy[i][0] = min(energy[i-1][0] + jump[i-1][0], energy[i-2][0] + jump[i-2][1], energy[i][0]) # 1번의 경우
    energy[i][1] = min(energy[i-1][1] + jump[i-1][0], energy[i-2][1] + jump[i-2][1], energy[i-3][0] + k, energy[i][1]) # 2번의 경우

print(min(energy[n-1]))