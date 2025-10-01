# 1. 숫자들이 연속적으로 있다.
# 2. 각 자리마다 1, 3, 1, 3, ... 을 곱한뒤 전부 하고 그 값을 10을 나눈 나머지가 0이 된다. -> 10의 배수
#        인덱스 짝수 -> 1, 홀수 -> 3
#        10으로 나눈 나머지가 0이다. 만약 mod 10의 값이 R이면 10-R, 20-R, 30-R(이 경우는 모든 R에 대해서는 아님.)만큼 필요하다는 의미

seq = list(input())
total = 0

star_weight = 0

for i in range(len(seq)):
  if not seq[i].isdigit():
    star_weight = 1 if i % 2 == 0 else 3
    continue
  if i % 2 == 0:
      total += int(seq[i]) * 1
  else:
      total += int(seq[i]) * 3

print(total)
for i in range(10):
  if (total + i * star_weight) % 10 == 0:
    print(i)
    break