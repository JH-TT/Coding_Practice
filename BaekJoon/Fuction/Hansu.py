# 1065번 : 한수 -> 정수X의 각 자리가 등차수열을 이루는 경우.

def s(n = int(input())):   # 매개변수에 input을 넣는다.
    count = 0  # 한수의 개수를 셀 변수
    for i in range(1, n + 1):
      a = list(map(int, str(i))) # 정수를 str로 변환하고 각 자릿수를 정수형으로 리스트를 생성한다.
      if i < 100: # 1, 2자릿수는 무조건 등차수열을 만족.
          count += 1
      elif a[0]-a[1] == a[1]-a[2]: # 3자리 이상은 비교해서 결정.
          count += 1
    return count
print(s())