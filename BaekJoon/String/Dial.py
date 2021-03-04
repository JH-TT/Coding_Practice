# 5622번
a = input()
b = dict()  # 사전 자료형 이용해서 틀을 만든다.
b['2'] = "ABC"
b['3'] = "DFE"
b['4'] = "GHI"
b['5'] = "JKL"
b['6'] = "MNO"
b['7'] = "PQRS"
b['8'] = "TUV"
b['9'] = "WXYZ"
sum = 0

for i in a:  # 입력받은 알파벳을 하나씩 꺼내어 b의 value값에 속해있는지 확인하면서 초를 더한다.(1을 입력하는데 2초이므로 각 숫자의 1만큼을 더한 값이 그 숫자를 입력할때 걸리는 시간)
    for j in range(2, 10):
        if i in b[str(j)]:
            sum += j + 1
print(sum)