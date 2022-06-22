N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
res = N # 결과값
total = 0 # 현재 부분합
if sum(arr) < S: # 조건을 만족시키는 부분합을 찾지 못한 경우
    print(0)
elif S < min(arr): # arr의 최솟값보다 S가 작으면 arr의 원소 한 개 만으로 조건을 충족시킨다.
    print(1)
else:
    while start < N:
        # 먼저 end가 범위를 벗어나거나 total이 S이상이 될 떄 까지 end를 이동시킨다.
        while total < S and end < N:
            total += arr[end]
            end += 1
        # end를 끝까지 보냈음에도 S보다 작으면 더이상 찾을 수 없다는 의미.
        if total < S:
            break
        # total이 S이상이 된 경우 start를 이동시킨다. 이동시키면서 total은 start가 가리키는 원소값을 뺀다.
        # res는 꾸준히 업데이트 시켜준다.
        res = min(res, end - start)
        total -= arr[start]
        start += 1
    print(res)