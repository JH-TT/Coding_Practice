from itertools import combinations
import sys
input = sys.stdin.readline

L, C = map(int, input().split())
a = list(input().split())
a.sort()
c = ["a", "e", "i", "o", "u"]
b = list(combinations(a, L))


for i in b:
    ja = 0
    mo = 0
    for j in i:
        if j not in c:
            ja += 1
        else:
            mo += 1  
    if ja >= 2 and mo >= 1:
        print("".join(i))