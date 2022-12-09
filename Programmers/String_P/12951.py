def solution(s):
    # 내가 푼 풀이 -> 공백이 여러번 나올 수 있다고해서 그 부분도 똑같이 출력해야하는줄 알고 괜히 그 부분까지 구현함.
    # 설명이 많이 부실했던 문제.
    answer = []
    s = list(s)
    for i in range(len(s)):
        if i == 0 and s[i].isalpha():
            s[i] = s[i].upper()
        else:
            if s[i-1] == " " and s[i].isalpha():
                s[i] = s[i].upper()
            else:
                s[i] = s[i].lower()
    
    return "".join(s)

    # 1줄답
    return ' '.join([word.capitalize() for word in s.split(" ")])