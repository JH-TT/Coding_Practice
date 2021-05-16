# 입력받은 단어로 알파벳의 자릿수를 기록하고
# 각 알파벳의 중요도를 입력해주는것이 포인트!
import sys
input = sys.stdin.readline

n = int(input())
words = []
num = [0] * 26
for _ in range(n):
    s = input().rstrip()
    words.append(s)

for i in words:
    j = 0 # 자릿수를 계산할 변수.
    while i:
        now = i[-1]
        num[ord(now) - ord("A")] += pow(10, j) # 각 자릿수를 기록.
        j += 1 # 자릿수 1 증가.
        i = i[:-1] # 마지막 인덱스 빼고 나머지 이어서.

num.sort(reverse = True) # 중요도 내림차순.
res = 0 # 결과값.

# 가장 중요도가 높은 알파벳부터 순서대로 9 ~ 1까지 곱해준다.
for i in range(9, 0, -1):
    res += i * num[9-i]
print(res)