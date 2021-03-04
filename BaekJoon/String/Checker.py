# 1316번
a = int(input())
count = 0   # 그룹단어 개수
for _ in range(a):
    b = input() 
    c = list(set(b))  # 쓰인 알파벳 저장
    for i in c:
        n = b.count(i)
        b = b.replace(i*n, "1") # 알파벳이 a에 있는 개수만큼 연속으로 이어져 있다면 1로 바뀐다.
    if len(b) == len(c): # 만약 그룹단어라면 b는 전부 1로만 돼 있어야 한다. 그리고 그 개수는 사용된 알파벳의 개수와 동일.
        count += 1
print(count)