from collections import deque

n, m = map(int, input().split())
cnt, *people = map(int, input().split())

party = deque() # 과장되게 말해도될 가능성이 있는 집단
check = [0 for _ in range(m)]
q = [] # 진실을 말해야하는 집단

for i in range(m):
    n, *p = map(int, input().split())

    if len(set(people) & set(p)) > 0:
        q.append(p)
        check[i] = 1
        continue

    party.append(p)

i = 0
while i < len(q):
    party2 = deque()

    while party:
        p = party.popleft()
        if len(set(q[i]) & set(p)) > 0:
            q.append(p)
            continue
        party2.append(p)

    party = party2
    i += 1

print(m - len(q))