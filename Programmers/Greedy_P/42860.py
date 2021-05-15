# 주의! 끝 인덱스에서 오른쪽 화살표를 누르면 처음 인덱스로 간다는 얘기는 없었음!

def solution(name):
    answer = 0
    answer2 = 10001
    l = len(name)
    print("문자열 길이 :", l)
    cursor = []
    
    for i in range(l):
        n = ord(name[i])
        print("문자", name[i], "아스키코드", n)
        if n != 65:
            cursor.append(i)

        if 66 <= n <= 78:
            answer += n - 65
            print("1 실행")
        elif 78 <= n <= 90:
            answer += 91 - n
            print("2 실행")
    print("중간 과정 결과 :", answer)
    print("A가 아닌 위치 :", cursor)
    l2 = len(cursor)
    # 다시 돌아가는 방법x
    if l2 == 1:
        if (cursor[-1] - 0) <= (l + 0 - cursor[-1]):
            answer2 = min(answer2, cursor[-1] - 0)
        else:
            answer2 = min(answer2, l + 0 - cursor[-1])
    elif l2 >= 2:
        if (cursor[-1] - cursor[0]) <= (l + cursor[0] * 2 - cursor[1]):
            answer2 = min(answer2, cursor[-1] - cursor[0])
            print("오른쪽이 더 빠름", answer2)
        else:
            answer2 = min(answer2, l + cursor[0] * 2 - cursor[1])
            print("왼쪽이 더 빠름", answer2)
    # 다시 돌아가는 방법o
    if l2 >= 2:
        for i in range(l2 - 1):
            answer2 = min(answer2, cursor[i] * 2 + l - cursor[i + 1])
            print("다시 돌아가는것이 더 빠름", cursor[i], answer2)
    if answer2 != 10001:
        answer += answer2
            
    
    return answer