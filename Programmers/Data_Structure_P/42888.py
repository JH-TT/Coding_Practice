from collections import defaultdict

def solution(record):
    answer = []
    ID = defaultdict(str)
    
    for i in record:
        a = i.split()
        if a[0] == "Enter" or a[0] == "Change": # 이미 들어와 있는데 또 같은 아이디로 들어오는 경우는 없으니 덮어씌우는 방식으로 한다.
            ID[a[1]] = a[2]
            
    for i in record:
        a = i.split()
        if a[0] == "Enter":
            answer.append(ID[a[1]] + "님이 들어왔습니다.")
        elif a[0] == "Leave":
            answer.append(ID[a[1]] + "님이 나갔습니다.")
    
    
    return answer