# 내가 푼 방식
import math

def calc_zero_cnt(n, a):
    cnt = 0
    f = 5
    for i in range(1, a+1):
        cnt += n // f
        f *= 5
    return cnt

n = int(input())
zero_cnt = calc_zero_cnt(n, int(math.log(n, 5)) + 1)

res = 1
for i in range(2, n+1):
    res *= i
    res %= 10 ** (zero_cnt + 1)
print(res // 10 ** zero_cnt)
# 나는 %연산을 이용해서 n펙토리얼에서 0의 개수가 나오는 규칙을 만든다음 그 규칙을 이용해서 뒤에서 낮은차수 0의 개수 + 1번째 자릿수를 출력하도록 했다.

# 훨씬 쉬운 방식
import math

print([i for i in list(str(math.factorial(int(input())))) if i != '0'][-1])

# math라이브러리에 펙토리얼을 계산해서 그것을 각 자릿수를 str로 만든 후에 리스트로 구성한다.
# for문을 돌면서 0인것 빼고 전부 넣고, 다 한뒤에 맨 뒤 원소를 꺼낸다.

# n이 20000이라서 math.factorial이 안될줄 알았는데 역시 라이브러리는 좋다.