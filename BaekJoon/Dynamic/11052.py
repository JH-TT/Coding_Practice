# 내가 한 풀이.
n = int(input())

card = list(map(int, input().split()))

for i in range(1, n):
    big = card[i] # 그 인덱스 값 저장.
    for j in range(i):
        a = (i + 1) // (j + 1)
        b = (i + 1) % (j + 1)
        # 그 자체의 값이랑 다른 개수의 카드들을 조합한 값이랑 비교해서 더 큰 값 저장.
        if b > 0:
            big = max(big, card[j] * a + card[b - 1])
        else:
            big = max(big, card[j] * a)
    card[i] = big
print(card[-1]) # 마지막값 출력.


# 더 간결한 풀이
n = int(input())

cd = [0] * (n + 1)
card = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    cd[i] = card[i]

for i in range(2, n + 1):
    for j in range(1, i):
        # 내가 한 풀이를 간결하게 표현.
        if cd[i] < cd[i - j] + card[j]:
            cd[i] = cd[i - j] + card[j]
print(cd[n])