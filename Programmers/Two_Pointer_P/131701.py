def solution(elements):
    answer = set()
    n = len(elements)
    start_prefix_sum = 0 # 시작 누적합 계속 sum함수를 사용하면 시간초과 우려있음
    for i in range(1, n):
        start_prefix_sum += elements[i-1]
        total = start_prefix_sum
        answer.add(total)
        for j in range(n):
            total += (elements[(i+j) % n] - elements[j])
            answer.add(total)
    answer.add(sum(elements))
    return len(answer)

# 몇 개의 부분수열이어도 결국 n-1번 한칸씩 움직이면 다시 돌아온다. 이 점을 이용해 투 포인터로 풀었다.