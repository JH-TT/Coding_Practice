# 4344번 : 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

a = int(input()) # 몇번의 테스트를 거칠건지
for _ in range(a):
    b = list(map(int, input().split()))
    avg = sum(b[1:]) / b[0] # b배열에서 첫번째는 학생의 수, 그 외는 점수
    c = [i for i in b[1:] if i > avg] # b배열에서 평균이 넘는 점수들만 c에 넣는다.
    print("%.3f%%" %round(len(c)/b[0]*100, 3))