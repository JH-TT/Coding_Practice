def solution(numbers):
    arr = list(map(lambda x : str(x) * 3, numbers))
    arr.sort(reverse = True)
    res = list(map(lambda x : x[:len(x) // 3], arr))
    answer = str(int("".join(res)))
    
    return answer

# 곱하기 3을 해주는 이유 : [9, 998]이 주어진다고 하자.
# 답은 9998이 되어야하는데 그냥 정렬을 해버리면 9989가 되어버리니까
# 각 숫자를 string으로 * 3을 해줘서 999, 998998998을 비교해준다.
# 스트링 정렬은 하나씩 보기때문에 정렬하면 999, 998998998로 될것이고, 원래대로 바꾸면 9, 998이되어 9998이 될 수 있다.

# 다른풀이
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
# cmp_to_key에 대한 설명은 https://jeonzzang.tistory.com/48 참고.