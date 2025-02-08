import sys
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []

for i in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

cd_cnt = {} # C와 D의 합이 각 몇개씩 있는지

# C와 D는 계산해 놓는다.
for c in C:
    for d in D:
        if c+d in cd_cnt:
            cd_cnt[c+d] += 1
        else:
            cd_cnt[c+d] = 1

cnt = 0
for a in A:
    for b in B:
        if -a-b in cd_cnt:
            cnt += cd_cnt[-a-b]

print(cnt)

# C와 D의 개수를 미리 구해놓고 딕셔너리를 이용해서 빠르게 값이 있는지 체크한다.
# 있으면 cd_cnt만큼 더해준다.

# 이때 A와 B도 미리 다 구해놓고 하는건 안되나?
from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []

for i in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab_cnt = defaultdict(int) # A와 B의 합이 각 몇개씩 있는지
cd_cnt = defaultdict(int) # C와 D의 합이 각 몇개씩 있는지

# A와 B는 계산해 놓는다.
for a in A:
    for b in B:
        ab_cnt[a+b] += 1

# C와 D는 계산해 놓는다.
for c in C:
    for d in D:
        cd_cnt[c+d] += 1

cnt = 0
for ab in ab_cnt:
    if -ab in cd_cnt:
        cnt += ab_cnt[ab] * cd_cnt[-ab]

print(cnt)
# 만약 이렇게 A와 B, C와 D를 각각 미리구한뒤에 ab_cnt의 키 값을 순회하면서 cd_cnt가 있는지 확인하는 방식은 시간초과가 나왔다.
# 이유가 뭘까?
# 단순하게 보면 이것도 될 거 같지만, 사실 잘 보면 아래의 코드는 이중 for문을 한 번 더 돌게되는 격이다.
# 1. A와 B 합 조홥
# 2. C와 D 합 조합
# 3. A와 B 합 조합을 순회하면서 C D의 합 조합을 확인한다.

# 그렇기에 시간초과가 났던것.

# 추가. defaultdict
# defaultdict는 in과 값에 접근하는 방식이 서로 차이가 크다.
# 값 in defaultdict의 경우 말 그대로 키가 있는지 확인만 하지만
# dfd[a] > 0  이런식으로 하게되면 키값 a가 없었다면 dfd[a]에 0을 할당하는 작업을 하게 된다.
# 그래서 값에 직접 접근하는 방식은 성능에 나빠진다.

# 실제로 비교한 코드도 있다.
from collections import defaultdict
import time

# 테스트 데이터
keys = range(10**6)  # 100만 개의 키 생성

# defaultdict 초기화
cd_cnt = defaultdict(int)

# 1. in 연산자 사용
start = time.time()
count = 0
for k in keys:
    if k in cd_cnt:
        count += 1
end = time.time()
print(f"in 연산자 실행 시간: {end - start:.6f}초")

# 2. 직접 접근 방식 (기본값 생성 발생)
cd_cnt.clear()
start = time.time()
count = 0
for k in keys:
    if cd_cnt[k] > 0:
        count += 1
end = time.time()
print(f"값 접근 실행 시간: {end - start:.6f}초")

# in 연산자 실행 시간: 0.096595초
# 값 접근 실행 시간: 0.214399초