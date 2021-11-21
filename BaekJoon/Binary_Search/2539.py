import sys
input = sys.stdin.readline

def need(width):
    prev = -1 # 시작은 -1로
    ret = 0
    for pos in m_x:
        if prev == -1: # 현재 시작점이 안정해졌으면 pos를 시작점으로 둠
            prev = pos
            ret += 1
        elif prev + width <= pos:
            prev = pos
            ret += 1
    
    return ret

r, c = map(int, input().split()) # 행, 렬
n = int(input()) # 사용할 색종이 개수
mistake = int(input()) # 실수한 개수

max_h = 0 # 최고 높이 i.e 색종이의 최소길이
m_x = [] # 각 x값들의 모임

for _ in range(mistake):
    m_r, m_c = map(int, input().split())
    max_h = max(max_h, m_r)
    if m_c not in m_x: # 중복이 없도록 넣음.
        m_x.append(m_c)

m_x.sort() # 정렬

# 이분탐색 시작.
start = max_h
end = 1000000
while start < end:
    m = (start + end) // 2
    if need(m) <= n: # n개 이하로 사용하면 더 줄일 수 있다는 의미.
        end = m
    else: # 아니면 더 길어야 된다.
        start = m + 1