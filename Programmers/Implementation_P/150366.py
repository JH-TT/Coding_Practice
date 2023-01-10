def solution(commands):
    answer = []
    arr = ["EMPTY" for _ in range(2500)]
    parent = list(range(2500))
    
    for cmd in commands:
        c, *a = cmd.split()
        if c == "UPDATE":
            # 병합된 상태일수 있으니 참조하는 부분을 찾고 그 부분에 업데이트 한다.
            if len(a) == 3:
                target = parent[(int(a[0])-1)*50+(int(a[1])-1)]
                arr[target] = a[2]
            else:
                arr = updateArr(arr, a[0], a[1])
        elif c == "PRINT":
            # 참조하는 값을 찾아 answer에 담는다.
            target = parent[(int(a[0])-1)*50+(int(a[1])-1)]
            answer.append(arr[target])
        elif c == "MERGE":
            # 같은 칸이면 무시한다.
            if a[0] == a[2] and a[1] == a[3]:
                continue
            # 다른 칸이면 합병한다.
            parent = union_parent(parent, arr, int(a[0])-1, int(a[1])-1, int(a[2])-1, int(a[3])-1)
        elif c == "UNMERGE":
            # 현재 참조하는 값을 구한다.
            target = parent[(int(a[0])-1)*50+(int(a[1])-1)]
            v = arr[target]
            # 합친것을 전부 푼다.
            arr, parent = unmerge(parent, arr, target)
            # 아까 구해놓은 값을 기준칸에 넣는다.
            arr[(int(a[0])-1)*50+(int(a[1])-1)] = v
    return answer

# 모든 칸을 돌면서 해당 루트노드면 전부 자기 자신을 루트노드로 놓고 값은 EMPTY로 둔다.
def unmerge(parent, arr, v):
    for i in range(2500):
        if parent[i] == v:
            parent[i] = i
            arr[i] = "EMPTY"
    return [arr, parent]

# value1은 value2로 전부 바꾼다.
# 여기는 find_parent 함수를 사용하지 않았는데 이유는 결국 합병된 칸들은 루트노드를 참조하고 있기 때문에 자기자신이 무슨값이든 간에 루트노드의 값만 바뀌면 된다.
def updateArr(arr, value1, value2):
    for i in range(2500):
        if arr[i] == value1:
            arr[i] = value2
    return arr

# 만약 a와 b가 2개 이상의 병합된 그룹이라면
# a가 b를 참조해야하는 상황이 오게되면 a와 같은 그룹들도 전부 b를 참조하도록 바꾼다.
# n의 범위가 2500밖에 안되기 때문에 무식하게 간다.
def match_parent(parent, v1, v2):
    for i in range(2500):
        if parent[i] == v1:
            parent[i] = v2
    return parent
  
# 각 칸들의 루트노드를 가져온다.
# 만약 둘 중 한곳에만 값이 있으면 값이 있는 곳을 기준으로 병합하고
# 둘 다 있으면 r1, c1가 참조하는 루트노드 기준으로 병합한다.
# 같은 그룹이면 그냥 끝낸다.
def union_parent(parent, arr, r1, c1, r2, c2):
    a = parent[r1*50+c1]
    b = parent[r2*50+c2]
    if arr[a] == "EMPTY" and arr[b] != "EMPTY":
        return match_parent(parent, a, b)
    if a == b:
        return parent
    return match_parent(parent, b, a)

# 이 문제는 parent리스트를 얼마나 잘 활용하냐에 따라 달렸었다.
# 참조하는 값을 생각해야 하다보니 print를 하거나 update를 할 때도 결국 대부분 parent를 기준으로 비교하고 업데이트 했다.
# union_parent는 기존에 우리가 알던 방식보다는 쉬운 편이었다.
# 왜냐면 원래는 재귀를 이용해서 한 칸 한 칸 올라가는 방식이었지만, 이 방식은 경로를 압축해서 바로 루트노드를 바라보도록 설계했기 때문이다.
# 그래서 원래는 find_parent라는 함수도 있었어야 했지만, 여기는 바로 루트노드를 바라보기 때문에 parent[index]로 바로 루트노드를 꺼냈다.