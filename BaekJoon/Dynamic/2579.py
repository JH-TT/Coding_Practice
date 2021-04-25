n = int(input())

s = []
rst = [] # 점수 누적
for _ in range(n):
    s.append(int(input()))
rst.append(s[0]) # 첫번째 계단 저장.
if n > 1:
    rst.append(s[0] + s[1]) # 첫번쨰 계단과 두번째 계단 점수 합 저장.
    if n > 2:
        rst.append(max(s[1] + s[2], s[0] + s[2])) # 두칸 + 한칸, 한칸 + 두칸 오른 점수중 더 큰 값 저장.
for i in range(3, n):
    # 마지막계단은 무조건 밟아야한다. 그러기위해선 2가지 경우가 있다.
    # 첫번째는 두칸을 올랐을때 마지막 계단이거나, 두번째는 두칸 + 한칸 올랐을때 마지막 계단이거나.
    # 이 두가지 경우 중 더 큰 값을 저장.
    rst.append(max(rst[i - 3] + s[i - 1] + s[i], rst[i - 2] + s[i]))

print(rst[-1]) # rst의 마지막 인덱스 값을 출력.