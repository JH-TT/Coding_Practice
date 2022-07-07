n = int(input())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse = True)

print(sum((A[i] * B[i]) for i in range(n)))

# A는 오름차순, B는 내림차순으로 정렬하고 각 인덱스끼리의 곱의 합을 출력한다.