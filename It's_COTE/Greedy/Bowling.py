from itertools import combinations

n, m = map(int, input().split())
weigh = list(map(int, input().split()))

acc = list(combinations(weigh, 2)) # n개의 볼링공중에 2개를 선택하는 경우 구해놓는다.
a = len(acc) # 그 개수는 a에 저장.

for i in acc:
    if i[0] == i[1]: # 서로 다른 무게만 선택한다 했으니, 무게가 같으면 1씩 빼준다.
        a -= 1
print(a)

# 다른 방법(책 답지)
# 볼링공 무게가 1 3 2 3 2 로 입력됐을 때.
# step 1: A가 무게가 1인 공을 선택할 때의 경우의 수
# 1 (무게가 1인 공의 개수) x 4 (B가 선택하는 경우의 수) = 4
# step 2: A가 무게가 2인 공을 선택할 때의 경우의 수
# 2 (무게가 2인 공의 개수) x 2 (B가 선개하는 경우의 수) = 4
# step 3: A가 무게가 3인 공을 선택할 때의 경우의 수
# 2 (무게가 3인 공의 개수) x 0 (B가 선택하는 경위의 수) = 0
# 총 8가지

# 코드로 옮겨보자.
n, m = map(int, input().split())
data list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있다.
array = [0] * 11

for i in data:
    # 각 무게에 해당하는 볼링고의 개수 카운트
    array[i] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링고의 개수(A가 선택한 무게의 볼링공 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기