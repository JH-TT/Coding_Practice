from collections import deque

def solution(edges):
    answer = []
    prod_node, max_num = find_prod(edges)
    graph = [[] for _ in range(max_num + 1)]
    ind = [0] * (max_num + 1)

    for a, b in edges:
        if prod_node == a: continue
        graph[a].append(b)
        ind[b] += 1

    visit = [0] * (max_num + 1)
    donut, stick, eight = 0, 0, 0

    # 막대 그래프를 찾는 부분
    stick_node = []
    for node, cnt in enumerate(ind):
        if node == 0: continue
        if node != prod_node and cnt == 0:
            stick_node.append(node)
    stick = len(stick_node)

    # 도넛 or 8자 둘 중 하나
    for now in range(1, max_num + 1):
        if visit[now] or now == prod_node: continue
        q = deque()
        q.append(now)
        visit[now] = 1

        start = now
        cycle = False
        flag = ind[now] > 1 # 8자인지 확인
        while q:
            now_node = q.popleft()  

            if graph[now_node]:
                while graph[now_node]:
                    nxt = graph[now_node].pop()
                    if ind[nxt] > 1: flag = True
                    if nxt == start: cycle = True
                    visit[nxt] = 1
                    q.append(nxt)
        if flag:
            eight += 1
        if not flag and cycle:
            donut += 1

    return [prod_node, donut, stick, eight]

def find_max_num(edges):
    max_num = 0
    for a, b in edges:
        max_num = max([max_num, a, b])
    return max_num

def find_prod(edges):
    max_num = find_max_num(edges)
    rcv = [0] * (max_num + 1)
    snd = [0] * (max_num + 1)
    for a, b in edges:
        snd[a] += 1
        rcv[b] += 1

    for i in range(1, max_num + 1):
        if rcv[i] == 0 and snd[i] > 1:
            return [i, max_num]

# 이 문제는 생성된 노드를 찾는것이 관건
# 문제를 보면 생성된 노드의 특징을 알 수 있다.
# 1. 나가는 간선이 2개 이상(문제에 그래프의 개수는 2개 이상이라고 했음)
# 2. 들어오는 간선이 없음
# 1, 2를 모두 해당하면 해당 노드는 생성 노드가 된다.


# 다른 풀이
  def solution(edges):
    answer = [0, 0, 0, 0]
    n = 0
    graph_cnt = 0

    for a, b in edges:
        n = max([n, a, b])

    rcv = [0] * (n + 1)
    snd = [0] * (n + 1)

    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        snd[a] += 1
        rcv[b] += 1
        graph[a].append(b)

    for i in range(1, n + 1):
        in_ = rcv[i]
        out = snd[i]

        if in_ == 0 and out > 1:
            answer[0] = i
            graph_cnt = len(graph[i])

        if in_ >= 0 and out == 0:
            answer[2] += 1

        if in_ > 1 and out == 2:
            answer[3] += 1
    answer[1] = graph_cnt - answer[2] - answer[3]
    return answer