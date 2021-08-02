import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    x = input().rstrip()
    a.append((len(x), x))
print(set(a))    
a = list(set(a))
a.sort()
for i in a:
    print(i[1])

# 문자열 길이가 우선이므로 입력받을때, 길이를 먼저 놓고 그 뒤에 문자열을 저장한다.