from bisect import *
import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

res = [1] * n                   # 무조건 0번쨰 인덱스는 1이니까 그냥 전부 1로 초기화 한다.
sub_seq = []                    # 단순 증가하는 부분수열의 길이를 재기위한 리스트(여기에 있는 값들이 최종 증가하는 부분수열이 아니다)
for i in range(n):
    if not sub_seq:             # sub_seq가 비어있으면 넣어줌.
        sub_seq.append(seq[i])
    else:
        idx = bisect_left(sub_seq, seq[i]) # bisect를 이용해 이분탐색으로 위치를 찾는다.
        if idx == len(sub_seq): # 가장 큰 수인 경우는 sub_seq에 넣어줌.
            sub_seq.append(seq[i])
        else:                   # 그 외에는 원래 sub_seq에 idx위치에 있는 수와 seq[i]와 바꿔준다.
            sub_seq[idx] = seq[i]
        res[i] = idx+1

ans = []                        # 여기가 최종 증가하는 부분수열
l = len(sub_seq)                # 증가하는 부분수열의 (최대)길이

# 역추적으로 l의 값과 같은 값을 갖고있는 수가 있으면 그걸 ans에 넣고 l감소
for i in range(n-1, -1, -1):
    if l == 0:
        break
    if res[i] == l:
        ans.append(seq[i])
        l -= 1
      
print(len(sub_seq))
print(*sorted(ans)) # 언패킹 이용.

# 원래 개수를 출력하고 각 숫자들의 부분수열 위치까지 나타내는건 어렵지 않았음.
# 그런데 여기서 역으로 탐색하면서 보는건 몰랐음(원래는 seq를 0번째 인덱스부터 확인하려 했음)
# 참고 : https://rebro.kr/33