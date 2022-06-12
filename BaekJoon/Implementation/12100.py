import copy

def dfs(Arr, dir, cnt):
    arr = copy.deepcopy(Arr)
    if cnt == 5:
        r = max(max(a) for a in arr)
        res.append(r)
        return

    # 각 방향에 맞게 스택을 이용해서 같은 수가 겹치면 더하는 방식을 이용한다.
    if dir == "Up":
        for i in range(n):
            stack = []
            for j in range(n):                
                if arr[j][i] == 0:
                    continue
                  
                if stack and stack[-1] == arr[j][i]:
                    s = stack.pop()
                    stack.append(s + arr[j][i])
                    stack.append(0) # 한 번 합친건 더이상 합칠 수 없으므로 경계를 두기위해 0을 넣어준다.
                else:
                    stack.append(arr[j][i])
                arr[j][i] = 0
            j = 0
            while stack:
                s = stack.pop(0)
                if s == 0:
                    continue
                arr[j][i] = s
                j += 1
    elif dir == "Down":
        for i in range(n):
            stack = []
            for j in range(n-1, -1, -1):
                if arr[j][i] == 0:
                    continue
                  
                if stack and stack[-1] == arr[j][i]:
                    s = stack.pop()
                    stack.append(s + arr[j][i])
                    stack.append(0)
                else:
                    stack.append(arr[j][i])
                arr[j][i] = 0
            j = n-1
            while stack:
                s = stack.pop(0)
                if s == 0:
                    continue
                arr[j][i] = s
                j -= 1
    elif dir == "Right":
        for i in range(n):
            stack = []
            for j in range(n-1, -1, -1):
                if arr[i][j] == 0:
                    continue
                  
                if stack and stack[-1] == arr[i][j]:
                    s = stack.pop()                    
                    stack.append(s + arr[i][j])
                    stack.append(0)
                else:
                    stack.append(arr[i][j])
                arr[i][j] = 0
            j = n-1
            while stack:
                s = stack.pop(0)
                if s == 0:
                    continue
                arr[i][j] = s
                j -= 1
    else:
        for i in range(n):
            stack = []
            for j in range(n):
                if arr[i][j] == 0:
                    continue
                  
                if stack and stack[-1] == arr[i][j]:
                    s = stack.pop()
                    stack.append(s + arr[i][j])
                    stack.append(0)
                else:
                    stack.append(arr[i][j])
                arr[i][j] = 0
            j = 0
            while stack:
                s = stack.pop(0)
                if s == 0:
                    continue
                arr[i][j] = s
                j += 1
    # 백트래킹 실행. 시작할때 copy를 이용하기 때문에 arr리스트는 보존된다.
    dfs(arr, "Up", cnt+1)
    dfs(arr, "Down", cnt+1)
    dfs(arr, "Right", cnt+1)
    dfs(arr, "Left", cnt+1)
        

n = int(input())
direction = ["Up", "Down", "Right", "Left"]
res = []
a = [list(map(int, input().split())) for _ in range(n)]

for d in direction:
    arr = copy.deepcopy(a)
    dfs(arr, d, 0)
print(max(res))

# 방향에 따라 데이터를 달리 처리해야돼서 짜는게 귀찮았음.
# 백트래킹을 이용하기위해 리스트를 보존해야되는걸 고려해야했음.