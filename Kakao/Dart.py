# 카카오 다트게임

a = input()

j = 0
b = [0] * 3 # 점수 저장 공간.
s = ""
for i in range(len(a)):
    if a[i] == "S": # S를 만나면 지금까지 저장된 s는 숫자들로만 이뤄진 문자열
        b[j] = int(s) # 정수형으로 b배열에 저장.
        s = "" # 다시 초기화
        j += 1 # 숫자가 입력되었으니 b배열의 다음 인덱스로 넘어감.
    elif a[i] == "D":
        b[j] = int(s)
        s = ""
        b[j] = b[j] ** 2
        j += 1
    elif a[i] == "T":
        b[j] = int(s)
        s = ""
        b[j] = b[j] ** 3
        j += 1
    elif a[i] == "*":
        if j == 1: # S T D에서 이미 인덱스가 올랐으니 첫기회때 *이면 이미 j는 1이다.
            b[j - 1] = b[j - 1] * 2
        else:
            b[j - 2] = b[j - 2] * 2
            b[j - 1] = b[j - 1] * 2
    elif a[i] == "#": # 마찬가지
            b[j - 1] = -b[j - 1]
    else:
        s += a[i]

print(sum(b))