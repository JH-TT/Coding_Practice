import sys
input = sys.stdin.readline

n = int(input())
mi, ma = [0, 0, 0], [0, 0, 0]
first = list(map(int, input().split()))
for i in range(3):
    mi[i] = first[i]
    ma[i] = first[i]

for t in range(1, n):
    nums = list(map(int, input().split()))
    mi_a, mi_b, mi_c = mi
    ma_a, ma_b, ma_c = ma
    for j in range(3):
        if j == 0:
            mi[j] = nums[j] + min(mi_a, mi_b)
            ma[j] = nums[j] + max(ma_a, ma_b)
        elif j == 1:
            mi[j] = nums[j] + min(mi_a, mi_b, mi_c)
            ma[j] = nums[j] + max(ma_a, ma_b, ma_c)
        else:
            mi[j] = nums[j] + min(mi_b, mi_c)
            ma[j] = nums[j] + max(ma_b, ma_c)
print(max(ma), min(mi))

# dp 아이디어 자체는 어렵지 않았는데 메모리가 4mb밖에 안주어져서 신경쓸 부분이 많았던 문제
# 가장 중요한 부분은 한 줄씩 입력받을때 마다 dp값 업데이트이다.
# 만약 한 번에 입력받고 진행하면 바로 메모리가 터진다.
# 단순 계산하면 30만개의 int 자료형인데 이는 약 1mb이다.
# 그래서 나는 최대 같은 크기의 리스트 2개를 더 만들수 있겠구나! -> min, max리스트 생각함
# 결과는, 메모리 초과...
# 이것저것 합치면 4mb가 넘나봄...
# 그래서 한줄씩 입력받을때 마다 진행하도록 변경했고 min, max도 크기 3의 리스트로 변경해서 진행했는데 통과했다!