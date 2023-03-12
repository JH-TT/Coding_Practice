from collections import defaultdict, Counter

def solution(X, Y):
    answer = ''
    cnt = dict(Counter(X))
    res = defaultdict(int)
    
    for y in Y:
        if (y in cnt) and cnt[y] > 0:
            res[y] += 1
            cnt[y] -= 1
            
    for i in range(9, -1, -1):
        answer += str(i) * res[str(i)]
        
    if answer == "":
        return "-1"
    else:
        return answer if answer[0] != "0" else "0"

# answer가 "000..." 처럼 엄청 긴 경우에 int(answer)를 이용해서 0으로만 이뤄져 있는지 확인할 때 엄청난 시간이 걸림 그래서 첫 숫자가 0인지만 판단하는걸로 해결
