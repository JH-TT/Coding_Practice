# 처음 풀이
n = int(input())
balloon = list(map(int, input().split()))
res = []
b_n = balloon[0]
index = 0
balloon[0] = 0
res.append(1)

i = 1
while i < n:
    cnt = 0
    if b_n > 0:
        j = 1
        while 1:
            if balloon[(index + j)%n] != 0:
                cnt += 1
            if cnt == b_n:
                b_n = balloon[(index+j)%n]
                balloon[(index+j)%n] = 0
                index = (index + j) % n
                res.append(index + 1)
                i += 1
                break        
            j += 1
        continue
    else:
        j = 1
        while 1:
            if balloon[(index-j)%n] != 0:
                cnt += 1
            if cnt == -b_n:
                b_n = balloon[(index-j)%n]
                balloon[(index-j)%n] = 0
                index = (index-j)%n
                res.append(index + 1)
                i += 1
                break
            j += 1
print(*res)
# 그냥 노가다 코드이다. 코드도 많이 더럽다

# enumerate, pop을 이용해서 풀기
n = int(input())
balloon = list(map(int, input().split()))

arr = [1]
for index, i in enumerate(balloon): # enumerate를 사용하면 인덱스와 값이 같이 나온다.
    balloon[index] = (i, index + 1)

cnt = balloon[0][0]
index = 0
balloon.pop(0)

for _ in range(n-1):
    if cnt < 0:
        index = (index + cnt) % len(balloon) # 음수면 그냥 그대로 계산
    else:
        index = (index + cnt - 1) % len(balloon) # 양수는 개수가 1개 줄어드는것을 감안해서(pop읋 사용하기 때문) -1을 해준다.
    
    a, b = balloon.pop(index)
    cnt = a
    arr.append(b)
print(*arr)
# 훨씬 빠르게 작동한다.