from collections import defaultdict
import sys
input = sys.stdin.readline

# w, h, d 는 피타고리안 트리플
# x, y에 대해(x > y > 0), 다음을 만족한다.
# w = 2xy
# h = x^2 - y^2
# d = x^2 + y^2

# 이때 w, h 에 대한 직사각형을 만들기 위한 철사의 길이는 2(w + h)이고,
# 이를 x, y로 바꿔서 다시 계산하면 2(2xy + x^2  - y^2) = 2(x - y) ^ 2가 된다.
# 철사의 길이는 최대 1,000,000 이므로 2(x - y) ^ 2 <= 1,000,000을 만족해야 하고
# 이는 x - y <= 대략 707.1... 그러니 x 와 y의 차이가 707까지만 허용이 된다는 의미
# 또한 w의 경우 2xy < 250000이다. 왜냐하면 2(w + h)가 100만 이하면서 w < h를 만족해야하기 때문에 w의 상한은 24만9999가 상한이 된다.
# 즉 xy < 125000인데 x는 y보다 크다고 했으니 y^2 < xy를 만족한다. 따라서 최종은 y^2 < 125000이고 양변에 루트를 씌우면 y < 353.xxx가 된다. 이로써 y는 최대 353까지만 된다는것을 알게 되었다.

# 이 두 조건을 총합하면
# x와 y에 대해서 x > y > 0을 만족하고 이 둘의 차이는 최대 707까지만 허용되며 y는 353까지만 가능하다.
    # 이 말은 이중for문으로 충분히 돌리고도 남는정도. (353 * 707 = 249571)
# 마지막으로, 닮음이 인정되지 않는다. (h와 w의 관계 3번째가 그 내용) -> 이는 w와 h는 서로소 관계여야 한다는 의미!
# 그런데 w가 2xy여서 소수를 구할 수 없기 때문에 gcd를 구한뒤에 각 w와 h를 나누고 해당 쌍을 넣는 방식으로 한다.

# 일단 모든 w,h 쌍을 미리 구해놓는다.
# 그 다음 테스트 케이스를 돌면서 확인한다.

width_and_height = []
is_check = defaultdict(int)

# 최대 공약수를 가져온다.
def gcd(x, y) -> int:
    while y:
        x, y = y, x % y
    return x

for y in range(1, 354):
    for x in range(y + 1, y + 708):
        w = 2 * x * y
        h = x**2 - y**2

        # 철사로 만들 수 있는 정도를 넘으면 for문 탈출.
        if 2 * (w + h) > 1000000:
            break

        # w는 h보다 작아야 한다.
        if w >= h:
            continue

        g = gcd(w, h)
        w //= g
        h //= g
        if is_check[(w, h)]:
            continue
        is_check[(w, h)] = 1
        width_and_height.append((w, h))

width_and_height.sort(key = lambda x: x[0] + x[1])

for _ in range(int(input())):
    L = int(input())

    cnt = 0
    total_length = 0
    for w, h in width_and_height:
        if total_length + 2 * (w + h) > L:
            break
        total_length += 2 * (w + h)
        cnt += 1
    print(cnt)

# x와 y의 조건을 잘 생각해서 진행하면 충분히 풀리는 문제.
# 유클리드 호제법이 중요한 문제