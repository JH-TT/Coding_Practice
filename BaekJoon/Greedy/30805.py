# 딕셔너리를 이용한 풀이
from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

a_dic = defaultdict(list)
b_dic = defaultdict(list)

for i in range(N):
    a_dic[A[i]].append(i)

for i in range(M):
    b_dic[B[i]].append(i)

a_idx = -1
b_idx = -1

ans = []
for a in sorted(a_dic.keys(), reverse = True):
    if a not in b_dic:
        continue
    # 먼저 가능한 숫자만 남겨둔다.
    while a_dic[a] and a_dic[a][0] < a_idx:
        a_dic[a].pop(0)

    while b_dic[a] and b_dic[a][0] < b_idx:
        b_dic[a].pop(0)

    mini = min(len(a_dic[a]), len(b_dic[a]))
    if mini == 0:
        continue
    a_idx = a_dic[a][mini-1]
    b_idx = b_dic[a][mini-1]
    for _ in range(mini):
        ans.append(a)

print(len(ans))
print(*ans)

# 집합을 이용한 풀이
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

ans = []

while True:
    A_set = set(A)
    B_set = set(B)
    AB_set = A_set & B_set # 둘의 공통 수를 구한다.

    if not AB_set:
        break

    max_AB = max(AB_set) # 그 중에 최댓값 가져온다.

    ans.append(max_AB) # 최댓값을 넣고

    # 각 집합에서 최댓값 위치를 찾는다.
    A_idx = A.index(max_AB)
    B_idx = B.index(max_AB)

    # 최댓값이 A, B 둘 중에 마지막 숫자면 종료
    if A_idx == N - 1 or B_idx == M - 1:
        break

    # 더 있으면 그 위치 다음부터 확인
    A = A[A_idx + 1:]
    B = B[B_idx + 1:]

K = len(ans)

if K:
    print(K)
    print(*ans)
else:
    print(K)