def back(k, result):
    if max_num == len(result): # 최댓값이 최종 리스트 길이와 같으면 끝.
        print(*result)
        exit(0)

    if 1 <= int(seq[k]) <= max_num and not visit[int(seq[k])]: # 1개씩 보기.
        visit[int(seq[k])] = 1
        back(k + 1, result + [seq[k]])
        visit[int(seq[k])] = 0 # 반드시 재귀함수를 부르고 나서는 데이터들을 재귀함수 부르기 전으로 되돌린다.(밑에 if문도 포함)
    
    if 1 <= int(seq[k:k+2]) <= max_num and not visit[int(seq[k:k+2])]: # 2개씩 보기.
        visit[int(seq[k:k+2])] = 1
        back(k + 2, result + [seq[k:k+2]])
        visit[int(seq[k:k+2])] = 0
        
seq = input()
if len(seq) < 10:
    max_num = len(seq) # 최대값이 10미만이면 최대값이 seq의 길이가 된다.
else:
    max_num = 9 + (len(seq) - 9) // 2 # 그 외에는 한자리숫자들의 개수를 빼고, 나머지 값에서 2를 나눈 몫을 9에 더한것이 최댓값.
visit = [0] * (max_num + 1)
back(0, [])

# 백트래킹은 많이 안풀어봐서 조금 생소했다.
# 확실히 중요한것은 재귀함수를 부르고 나서는 부르기 전으로 되돌려야 한다는 것이 키 포인트.
# 이것만 알면 나머진 테크닉이라 딱히 없다.