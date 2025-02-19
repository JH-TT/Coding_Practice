# 노드가 홀수또는 짝수이면서 자식 개수도 홀수 또는 짝수 -> 홀짝
# 노드가 홀수 또는 짝수인데 자식 개수가 서로 반대의 경우 -> 역홀짝
# 문제는 모든 노드가 홀짝을 만족하던가 역홀짝을 만족하던가를 보는 문제인듯.
from collections import defaultdict, deque

# 순환은 없기 때문에 루트 노드를 제외한 나머지 노드들은 루트 노드가 되지 못하면 자식노드를 자신이 가진 개수 - 1을 해야한다.
# 루트 노드는 자식 개수를 그대로 가져가기 때문에 숫자 + 자식 개수가 하나를 제외하고 다 맞던지 다 틀리던지 해야 조건에 부합하게 된다. (단, 노드가 1개인 경우는 무조건 홀짝트리 또는 역홀짝트리가 된다.)
# 숫자와 자식의 개수가 서로 홀 또는 짝으로 맞는 노드가 하나이고 그 외에는 전부 반대일때 -> 홀짝노드
# 숫자와 자식의 개수가 서로 홀짝이 반대인 노드가 하나이고 그 외에는 전부 같을때 -> 역홀짝 노드

def solution(nodes, edges):
    answer = [0, 0]
    arr = defaultdict(list)
    check = defaultdict(lambda: False)

    for node in nodes:
        if arr[node]: # defaultdict는 접근하기만 해도 디폴트가 생성된다.
            pass

    for a, b in edges:
        arr[a].append(b)
        arr[b].append(a)

    for node in arr:
        if check[node]:
            continue
        check[node] = True
        q = deque()
        q.append(node)
        cnt = [0, 0] # 왼쪽이 다른, 오른쪽이 같은경우
        cnt[len(arr[node]) % 2 == node % 2] += 1
        while q:
            now = q.popleft()

            for nxt in arr[now]:
                if check[nxt]:
                    continue
                check[nxt] = True
                cnt[len(arr[nxt]) % 2 == nxt % 2] += 1
                q.append(nxt)

        # 단 하나인 경우 무조건 만족
        if sum(cnt) == 1:
            answer[cnt[0] == 1] += 1
        else:
            # 역홀짝
            if cnt[0] == 1:
                answer[1] += 1
            if cnt[1] == 1:
                answer[0] += 1    

    return answer