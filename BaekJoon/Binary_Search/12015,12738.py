from bisect import bisect_left

n = int(input())
seq = list(map(int, input().split()))
res = []

for i in range(n):
    if not res:
        res.append(seq[i])
    else:
        a = bisect_left(res, seq[i])
        if a >= len(res):
            res.append(seq[i])
        else:
            res[a] = seq[i]
print(len(res))
# 이 문제는 떠오르기 어려웠던 문제.
# 이분탐색을 이용해서 res의 최댓값보다 크면 바로 넣고, 작은 수면 bisect의 값을 구해서 res에서 그 위치에 그 수로 바꾼다.
# 즉 작은 수가 나오면 새로 업데이트 시키면서 나아간다.
# 정확한 수열을 아니지만 개수는 동일하게 만들 수 있다.

# 이 문제는 가장 긴 증가하는 부분수열2
# 가장 긴 증가하는 부분수열3도 같은 코드.(12738번)
# + 7/14추가 2352번 반도체 설계도 같은풀이.(안꼬일려면 결국 연결되는 포트의 번호가 증가하는 수열이어야 한다.)