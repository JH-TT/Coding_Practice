n = int(input())

d = [0] * 31
d[2] = 3 # 3 * 2 타일은 총 3가지 경우.

for i in range(4, n + 1):
    if i % 2 == 0:
        d[i] += d[i - 2] * 3 # 가로 i - 2경우와 가로가 2인 경우(3가지) 이므로 3을 곱해준다.
        for j in range(i - 4, -1, -2):
            d[i] += d[j] * 2 # i - 4부터는 i - 4만의 특수한 경우2가지 라서 곱하기 2를 해준다.
        d[i] += 2 # 3 * i 만의 특수한 경우 2가지.
print(d[n])

# 이 문제는 이러한 규칙이 주어진다.
# 3 * i면, d[i] = d[i - 2] * 3 + d[i - 4] * 2 + d[i - 6] * 2 + ... + 2
# 왜 이런지는 링크를 따라서 이미지와 함께보는게 좋을거 같다.
# https://blog.naver.com/zdudman... (참고)