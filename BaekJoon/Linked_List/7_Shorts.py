from itertools import combinations

shorts = []
for _ in range(9):
    shorts.append(int(input()))

Not_shorts = list(combinations(shorts, 2))
for i in Not_shorts:
    if sum(i) == sum(shorts) - 100:
        shorts.remove(i[0])
        shorts.remove(i[1])
        break
shorts.sort()
for i in shorts:
    print(i)

# 1. 9개의 키가 나열되면, 그 키들의 총합을 구한다.
# 2. 그 총합에서 100을 뺀다.
# 3. 9개의 키중에 2개씩 조합해서 그 합이 총합에서 100을 뺀 값과 같은지 확인한다.
# 4. 그 2개의 키가 정해지면 리스트에서 그 두 키를 제거한다.
# 5. 정렬후 출력한다.