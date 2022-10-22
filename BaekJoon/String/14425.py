n, m = map(int, input().split())

s = {input() for _ in range(n)} # set으로 하니까 훨씬 빠름
strings = [input() for _ in range(m)]
res = 0

for word in strings:
    res += word in s
print(res)

# 리스트 순회하면서 존재여부 확인문제
# set은 in을 사용할때 O(1)시간으로 찾아서 시간적 이점이 크다는것을 알게됨.