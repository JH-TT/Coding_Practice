# 나의 풀이
from itertools import permutations

def solution(numbers):
    numbers = sorted(numbers, reverse=True)
    N = int(''.join(numbers))
    answer = 0
    arr = list(numbers)
    res = set()

    eratos = [True] * (N + 1)
    eratos[0] = False
    eratos[1] = False
    for i in range(2, int(N**0.5) + 1):
        if eratos[i]:
            j = 2
            while i * j <= N:
                eratos[i * j] = False
                j += 1

    for i in arr:
        if eratos[int(i)]:
            res.add(int(i))

    for i in range(2, len(arr) + 1):
        sub = set(permutations(arr, i))

        for j in sub:
            n = int(''.join(j))
            if eratos[n]:
                res.add(n)

    return len(res)
# 일단 itertools의 permutation을 이용했고, 에레토스테네스의 채를 이용해 소수인지 판단하고, 소수면 set에 집어넣는 식으로 함.

# 다른코드(나랑 비숫하지만 더 깔끔)
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2)) # 0, 1은 소수가 아니므로 뺀다.
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i)) # 에라토스테네스의 채를 이용해서 소수가 아닌 수들은 빼준다.
    return len(a)
# 먼저 permutations와 map을 이용해서 주어진 문자열을 통해 나타낼 수 있는 모든 정수를 a에 add한다.    



# 아래코드가 나보다 2배 빨랐으며(가장 오래걸린 시간이 내 코드는 1600ms인데 아래는 800ms밖에 안걸림) 코드도 짧고 간단하게 잘 나타내었다.