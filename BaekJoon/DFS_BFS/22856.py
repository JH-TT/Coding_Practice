import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def inorder(now):
    global res
    if node[now][0] != -1:
        inorder(node[now][0])
        res += 1
    if now == lastNode:
        print(res)
        exit(0)

    res += 1
    if node[now][1] != -1:
        inorder(node[now][1])
        res += 1

def findLastNode(now):
    global lastNode
    if node[now][0] != -1:
        findLastNode(node[now][0])
    lastNode = now
    if node[now][1] != -1:
        findLastNode(node[now][1])

node = defaultdict(list)
global lastNode, res
lastNode = -1
res = 0

n = int(input())

for _ in range(n):
    a, b, c = map(int, input().split())
    node[a] = [b, c]

findLastNode(1)
inorder(1)

# 중위순회기 때문에 무조건 왼쪽노드는 갔다가 온다.(즉 +2 씩 증가하는셈)
# 오른쪽은 +1씩만 된다.
