def solution(n,a,b):

    def next_game(x):
        if x % 2 == 0:
            return x // 2
        else:
            return x // 2 + 1

    answer = 1

    while abs(a-b) != 1 or min(a,b) % 2 != 1:
        a = next_game(a)
        b = next_game(b)        
        answer += 1

    return answer

# 보자마자 이진트리가 생각났다
# 그래서 자식노드번호와 부모노드번호관계를 이용해서 풀었다