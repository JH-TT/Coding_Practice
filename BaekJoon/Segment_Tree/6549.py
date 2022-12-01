import math, sys
sys.setrecursionlimit(10**6)

# 더 작은 값의 인덱스를 리턴
def merge(left, right):
    if arr[left] < arr[right]:
        return left
    return right

# 세그먼트 초기화(여기서는 해당 범위에서 가장 작은값의 인덱스가 기준)
def init(left, right, node):
    if left == right:
        tree[node] = left
        return
    mid = (left + right) // 2
    init(left, mid, node*2)
    init(mid+1, right, node*2 + 1)
    tree[node] = merge(tree[node*2], tree[node*2+1])

def query(left, right, node, x, y):
    # 범위가 아예 안맞으면 -1 리턴
    if x > right or y < left:
        return -1
      
    # 범위안에 완전히 들어오면 그 값을 리턴
    if left >= x and right <= y:
        return tree[node]
      
    # 그외에는 분할(일부만 들어오는 경우)
    mid = (left + right) // 2
    left = query(left, mid, node*2, x, y)
    right = query(mid+1, right, node*2+1, x, y)
  
    # 왼쪽 부분이 아예 범위를 벗어나면 더이상 볼 필요가 없으니 오른쪽 리턴. 반대도 마찬가지
    if left == -1:
        return right
    elif right == -1:
        return left
    else:
        # 그게 아니면 둘 중에 비교해서 더 작은걸 리턴
        return right if arr[left] >= arr[right] else left

def dac(left, right):
    # 가장 작은 값의 인덱스 가져온다.
    idx = query(0, len(arr)-1, 1, left, right)
    # 블럭 1개면 그거 리턴
    if abs(left - right) == 0:
        return arr[idx]
      
    # 제일 작은놈기준 넓이 vs 왼쪽 넓이 vs 오른쪽 넓이
    v1, v2, v3 = arr[idx] * (right-left+1), 0, 0
    if idx-1 >= left:
        v2 = dac(left, idx-1)
    if idx+1 <= right:
        v3 = dac(idx+1, right)
    return max(v1, v2, v3)

while True:
    temp = list(map(int,input().split()))

    n = temp[0]
    if n == 0:
        break
    arr = temp[1:]
    tree = [0] * pow(2,math.ceil(math.log(len(arr),2))+1)

    init(0, len(arr)-1, 1)
    print(dac(0, len(arr)-1))

# 세그먼트 트리 응용문제