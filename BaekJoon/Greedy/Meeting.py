import sys
input = sys.stdin.readline

# 이 문제의 핵심은 일찍끝나는 회의롤 잡고 그 다음에도 일찍끝나는 회의롤 잡는식으로 해서 최대한 많은 회의를 잡게하는 알고리즘이다.

def g(a):
    l = 0
    result = 0
    for s, e in a:
        if s >= l:   # 시작시간이 끝나느 시간보다 크면.... 끝나는시간 교체.
            l = e
            result += 1 # 강의 하나 늘어남.
    return result

if __name__ == '__main__': # 이 파일에서만 실행되도록 해라.
    n = int(sys.stdin.readline())
    a = [tuple(map(int, input().split())) for _ in range(n)]
    a = sorted(a, key=lambda x: (x[1], x[0]))  # 끝나는 시간을 기준으로 정렬, 같으면 시작시간으로 정렬
    result = g(a)
    print(result)