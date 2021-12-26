import sys
from collections import defaultdict
input = sys.stdin.readline

word = defaultdict(int)
All = 0
while 1:
    a = input().rstrip()
    if a == "\n": break
    word[a] += 1    
    All += 1
    
words = sorted(list(word.keys()))

for i in words:
    print("%s %.4f"%(i, word[i]/All * 100))