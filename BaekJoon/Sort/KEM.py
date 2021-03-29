n = int(input())
a = []
for _ in range(n):
    a.append(input().split())

"""
1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름순으로(아스키 코드 기준.)
"""

a.sort(key = lambda x : (-int(x[1]), int(x[2]), -(int(x[3])), x[0])) # 이렇게 "-"를 붙이면 그 숫자는 내림차순으로 정렬되게 된다.

for i in a:
    print(i[0])