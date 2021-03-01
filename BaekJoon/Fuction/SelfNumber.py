# 4673번 : 함수d의 실행. d(75) = 75 + 7 + 5 = 87 이런식. 이때 생성자가 없는 숫자를 셀프 넘버라고 한다. 그럼 10000보다 작거나 같은 셀프 넘버를 출력 하시오.

def d(n):
    sum = n   # 자기자신
    for i in str(n):  # 각 자릿수를 추출하기 위해 str로 변환
        sum += int(i)  # 각 자리수들은 다시 정수형으로 변환후 계산
    return sum

a = [i for i in range(1, 10001)]
for i in range(1, 10001):
    if d(i) in a:  # 함수를 통해 나온 값이 a에 있으면 제거
        a.remove(d(i))

for i in a: # 제거 후 남은것들은 셀프넘버들
    print(i)