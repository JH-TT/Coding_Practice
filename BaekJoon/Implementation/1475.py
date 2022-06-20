from collections import defaultdict
arr = defaultdict(int)

n = input().replace("9", "6")
for i in n:
    arr[i] += 1

res = 0
for i in arr:
    if i == "6":
        if arr[i] % 2 == 0:
            res = max(res, arr[i]//2)
        else:
            res = max(res, arr[i] // 2 + 1)
    else:
        res = max(res, arr[i])

print(res)

# 9를 6으로 전부 바꿔줌.
# 그러고 6이랑 9의 합의 upper값을 세트 개수라 생각.