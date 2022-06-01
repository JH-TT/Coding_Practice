n = int(input())
t = list(map(int, input().split())) # 시험장 수험생 수
a, b = map(int, input().split()) # 총감독관, 부관독관이 감독할 수 있는 수험생 수

count = n  # 어차피 각 강의실에 총 감독관이 한명씩은 있어야 하니 미리 n으로 시작한다.
for i in range(n): 
    t[i] -= a # 총감독관이 감독할 수 있는 수험생 수를 미리 뺴놓는다.

for i in t: # 나머지에 대해 처리
    if i > 0: # 0이하제외 나머지
        count += i // b # 일단 b로나눈 몫을 더함.
        if i % b != 0: # b명 미만의 학생수가 남을 시.
            count += 1
print(count)