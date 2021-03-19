# 카카오 비밀지도
n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
arr3 = [] # 최종적으로 담겨지는 이진수

result = [] # 결과값
s = "" # result에 넣을 문자열
for i in range(n):
    arr3.append(format(arr1[i] | arr2[i], "b")) # arr1 혹은 arr2에서 1이라도 있으면 그건 #이라고 했으니,
                                                # "|" 로 두 수의 이진수를 논리식으로 계산후, arr3에 저장한다.
for i in range(n):
    if len(arr3[i]) < n: # 만약  길이가 짧으면, 앞에 나머지 자리는 " "으로 채워진다.
        s += " " * (n - len(arr3[i])) # 예를 들면, 6자리인데 이진수로 10011이 나왔다면 result엔 " #  ##" 으로 저장된다.
    for j in arr3[i]:
        if j == "1": # 1이면 #으로 저장
            s += "#"
        else: # 0이면 " "으로 저장
            s += " "
    result.append(s) # 다 하고나서 result에 저장
    s = "" # 다시 초기화
print(result)
