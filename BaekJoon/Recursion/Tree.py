# 1 : 리스트로 한것
n = int(input())
a = [list(input().split()) for _ in range(n)] # 노드 입력받기 

def preorder(b): # 전위 순회
    a_left = 0
    a_right = 0
    for i in range(n): # 지금 노드가 루트노드라 보고 왼쪽 노드 오른쪽 노드 지정.
        if b == a[i][0]:
            a_left = a[i][1]
            a_right = a[i][2]
            break
    # 루트, 왼쪽, 오른쪽 순으로 순회
    if b != ".":
        print(b, end = "")
    if a_left != ".":
        preorder(a_left)
    if a_right != ".":
        preorder(a_right)

def inorder(b): # 중위 순회
    a_left = 0
    a_right = 0
    for i in range(n):
        if b == a[i][0]:
            a_left = a[i][1]
            a_right = a[i][2]
            break
    # 왼쪽, 루트, 오른쪽 순.
    if a_left != ".":
        inorder(a_left)
    if b != ".":
        print(b, end = "")
    if a_right != ".":
        inorder(a_right)

def postorder(b): # 후위 순회
    a_left = 0
    a_right = 0
    for i in range(n):
        if b == a[i][0]:
            a_left = a[i][1]
            a_right = a[i][2]
            break
    # 왼쪽, 오른쪽, 루트 순.
    if a_left != ".":
        postorder(a_left)
    if a_right != ".":
        postorder(a_right)
    if b != ".":
        print(b, end = "")

preorder(a[0][0])
print()
inorder(a[0][0])
print()
postorder(a[0][0])

# 2 : 딕셔너리로 푼 것.
n = int(input())
a = {}
for i in range(n):
    c, l, r = map(str, input().split())
    a[c] = [l, r]

def preorder(b):
    if b != ".":
        print(b, end = "")
        preorder(a[b][0])
        preorder(a[b][1])

def inorder(b):
    if b != ".":
        inorder(a[b][0])
        print(b, end = "")
        inorder(a[b][1])

def postorder(b):
    if b != ".":
        postorder(a[b][0])
        postorder(a[b][1])
        print(b, end = "")

preorder("A")
print()
inorder("A")
print()
postorder("A")

# 이런 노드를 이용하는건 딕셔너리가 좀 더 편리한것 같다. 그냥 리스트로 했다가는 그 원소의 위치를 찾는데 시간이 걸리니까 좀 비효율적인것 같다