# 10809번

a = input()  # 단어 입력받음
al = list(range(97, 123))  # 97부터 122까지 리스트로 저장

for x in al: 
    print(a.find(chr(x)), end=" ") # 각 정수를 문자로 변경후 find함수로 인덱스 출력