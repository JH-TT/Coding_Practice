# 10250번

a = int(input())  # 테스터 횟수
for _ in range(a):
    h, w, n = map(int, input().split())  # 층, 호, n번째 손님
    if n % h == 0:  # 맨윗층에 가야할 경우
        print((n % h + h) * 100 + (n//h))
    else: # 그 외층. 호수에 1을 더하는 이유는 n / h가 나머지가 생긴다는건 한 라인은 다 채우고 남은 사람이 있다는 것이다. 그러니 1을 더해서 다음 라인에 들어가도록 하는것이다.
        print((n % h) * 100 + (n//h + 1))