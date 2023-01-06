# 카카오 블라인드
def solution(numbers):
    answer = []
    for n in numbers:
        if n == 1:
            answer.append(1)
            continue
        b = format(n, 'b')
        flag = isPerfect(b)
        l = len(b)
        if not flag[0]:
            b = "0" * (2 ** flag[1] - l - 1) + b
        
        if b[len(b)//2] == "0":
            if "1" in b:
                answer.append(0)
            else:
                answer.append(1)
            continue
        if checkbinary(b, 0, len(b)//2-1, flag[1], 2) and checkbinary(b, len(b)//2+1, len(b)-1, flag[1], 2):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer

def isPerfect(b):
    i = 1
    while 2**i-1 < len(b):
        i += 1
    return [2**i-1 == len(b), i]

def checkbinary(bi, start, end, end_level, level):
    if end_level == level:
        return True
    if bi[(end+start) // 2] == "0":
        if ("1" in bi[start:(end+start)//2]) or ("1" in bi[(end+start)//2+1:end+1]):
            return False
    return checkbinary(bi, start, (end+start)//2-1, end_level, level+1) and checkbinary(bi, (end+start)//2+1, end, end_level, level+1)

# 시험 당시에는 쉽게 풀었는데...왜 다시푸니까 더 오래걸렸지?
# 풀이 방식
# 주어진 10진수를 2진수로 변경한다.
# 완전 이진트리가 되도록 0을 2진수 앞에 붙여준다.(노드의 개수가 2**n-1 에 맞도록)
# 노드들을 탐색한다.
# 만약 해당노드가 리프노드가 아니고 더미노드이면 그 노드기준 왼쪽과 오른쪽 서브트리에 1이 있는지 확인하고 있으면 이진트리가 아니므로 False를 리턴한다.
# 리프노드면 0이든 1이든 상관없기 때문에 True를 리턴한다.
# 그렇게 모든 노드를 탐색하고 False를 리턴하지 않았으면 answer에 1을 넣는다.