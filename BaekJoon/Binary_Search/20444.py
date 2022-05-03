n, k = map(int, input().split())

start = 0
end = n//2

while start <= end:
    mid = (start + end) // 2
    cnt = (mid+1)*(n-mid+1)
    if cnt == k:
        print("YES")
        exit()
    elif cnt < k:
        start = mid+1
    else:
        end = mid - 1
print("NO")

# n과 k의 범위가 2^31이상이다보니 O(lonN)의 시간복잡도로 풀어야했다.
# 그중에 가장 유명한 알고리즘이 이분탐색
# 가로 혹은 세로로 자르는 경우를 이분탐색으로 찾는다.
# 일단 색종이를 가로로 자른 개수, 세로로 자른 개수를 이용해서 계산하면
# 색종이 개수 = (가로+1) * (세로+1)인데 세로는 n-가로로 바꿔서 표현가능.
# 가로 or 세로의 범위는 0 ~ n//2까지 이므로 end를 n//2로 둔것.
# 앞서 계산한 색종이 개수를 이분탐색으로 돌려서 k보다 작으면 start를
# k보다 크면 end를 조정해서 반복문이 끝나기전에 찾으면 YES 그렇지 않으면 NO를 출력한다.