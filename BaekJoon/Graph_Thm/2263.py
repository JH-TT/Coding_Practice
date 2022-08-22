import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def tree(in_s, in_e, post_s, post_e):
    if (in_s > in_e) or (post_s > post_e):
        return

    root = post[post_e]
    print(root, end=" ")

    idx = pre[root] # root가 inorder에서 어디에 위치하는지

    # 이 밑에 두 줄 없이 idx로만 하기에는 한계가 있음.
    left = idx - in_s # 왼쪽으로 루트가 얼만큼 떨어졌는지
    right = in_e - idx # 오른쪽으로 루트가 얼만큼 떨어졌는지
  
    tree(in_s, in_s+left-1, post_s, post_s+left-1)
    tree(in_e-right+1, in_e, post_e-right, post_e-1)

n = int(input())

inorder = list(map(int, input().split()))
post = list(map(int, input().split()))
pre = [0] * (n + 1)

# index함수를 쓸 바엔 미리 구해놓고 뽑아서 쓰자.
# inorder에서 post의 끝 값 위치를 저장함
for i in range(n):
    pre[inorder[i]] = i

tree(0, n-1, 0, n-1)
# 중위 순회(inorder), 후위 순회(postorder)의 특징을 알면 틀은 거의 잡은거