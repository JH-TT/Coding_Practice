# 1157번
a = input().upper() # 일단 입력받은건 전부 대문자로 바꾼다.
b = list(set(a)) # 사용된 알파벳만 리스트 형식으로 저장
c = [a.count(x) for x in b]  # 각 알파벳마다 몇 번 사용 되었는지 저장
if c.count(max(c)) > 1:
    print("?")
else:
    print(b[c.index(max(c))])