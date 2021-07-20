n, k = map(int, input().split())
seq = list(map(int, input().split()))

res = [0] * (max(seq) + 1) # 각 숫자들의 개수
start = 0
end = 0
ans = 0
while 1:
    if end == len(seq): # 마지막 까지 갔으면 현재 ans랑 새로운 수열의 길이중에 큰값을 ans로 한다.
        ans = max(ans, end - start)
        break
    if res[seq[end]] < k: # 개수가 아직 적당하면 추가한다.
        res[seq[end]] += 1
        end += 1
    else:
        ans = max(ans, end - start) # 개수를 초과하게 되면 ans를 업데이트 하고 첫 인덱스를 1 증가시킨다.
        res[seq[start]] -= 1 # 빠지게 되는 숫자의 개수를 줄인다.
        start += 1
print(ans)