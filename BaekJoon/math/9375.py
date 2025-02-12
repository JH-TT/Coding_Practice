from collections import defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    clothes = defaultdict(list)
    categories = set()

    for _ in range(int(input())):
        cloth, category = input().split()
        clothes[category].append(cloth)
        categories.add(category)

    categories = list(categories)

    total = 1
    for c in categories:
        total *= (len(clothes[c]) + 1)

    print(total - 1)

# 각 옷 종류별로 안 입는 경우까지 더해서 + 1 씩 해준다.
# 그 다음 모든 개수를 곱한뒤에 전부 안입는 경우인 1개만 빼준다.