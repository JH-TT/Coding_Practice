from itertools import permutations

n = int(input())
A = list(map(int, input().split()))
expr = list(map(int, input().split()))
calc = []
calc.extend(["+" for _ in range(expr[0])])
calc.extend(["-" for _ in range(expr[1])])
calc.extend(["*" for _ in range(expr[2])])
calc.extend(["/" for _ in range(expr[3])])
mini = float('inf')
maxi = -float('inf')

for permu in list(set(permutations(calc, n-1))):
    idx = 1
    stack = [A[0]]
    for e in permu:
        num = stack.pop()
        if e == "+":
            stack.append(num + A[idx])
        elif e == "-":
            stack.append(num - A[idx])
        elif e == "*":
            stack.append(num * A[idx])
        else:
            if num < 0:
                stack.append(-(-num // A[idx]))
            else:
                stack.append(num // A[idx])
        idx += 1
    mini = min(mini, stack[0])
    maxi = max(maxi, stack[0])
print(maxi)
print(mini)

# 백트래킹도 가능한데 난 dfs짜기 귀찮아서 그냥 permtation으로 진행.
# 비둘기집 원리에 의해 숫자가 6개 이상이면 연산자가 같은게 적어도 1개 이상되기 때문에 permutation을 하고 set을 이용해 중복을 제거해줬다.