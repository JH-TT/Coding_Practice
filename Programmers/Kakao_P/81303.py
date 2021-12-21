from collections import defaultdict

def solution(n, k, cmd):
    answer = ['O'] * n
    # defaultdict를 이용해 딕셔너리 default를 리스트로 준다.
    l_list = defaultdict(list)
    
    # 현재 인덱스에서 prev와 next를 초기화 해준다.
    # 0번인덱스(맨 위)는 이전이 없으니 1번인덱스부터 초기화해준다.    
    for i in range(1, n + 1):
        l_list[i].append(i - 1)
        l_list[i].append(i + 1)
    
    # 삭제한 데이터 저장공간
    deleted = []    
    k += 1
    
    for com in cmd:
        c = com.split()
        
        # 아래로
        if c[0] == "D":
            for _ in range(int(c[1])):
                k = l_list[k][1]
        # 위로
        elif c[0] == "U":
            for _ in range(int(c[1])):
                k = l_list[k][0]
        # 삭제                
        elif c[0] == "C":
            prev, next = l_list[k]
            deleted.append([prev, next, k]) # 현재 노드 정보 삭제후 deleted에 저장
            answer[k - 1] = "X" # 그 값은 X로 설정
            
            if next == n + 1: # 마지막이면 위쪽 행 선택
                k = l_list[k][0]
            else: # 그 외에는 아래쪽 행 선택
                k = l_list[k][1]
            
            # 맨위가 삭제되면 다음노드의 이전이 prev
            if prev == 0:
                l_list[next][0] = prev
            # 맨 아래가 삭제되면 이전노드의 마지막이 next
            elif next == n + 1:
                l_list[prev][1] = next
            # 그 외에는 링크드리스트 삭제하는것 처럼
            else:
                l_list[prev][1] = next
                l_list[next][0] = prev
        # 복구
        else:
            prev, next, now = deleted.pop() # deleted리스트에서 꺼내온다.
            answer[now - 1] = "O" # O로 복구
            
            # 맨 위가 복구되면 다음의 이전에 현재
            if prev == 0:
                l_list[next][0] = now
            # 마지막이 복구되면 이전의 다음이 현재
            elif next == n + 1:
                l_list[prev][1] = now
            else:
                l_list[prev][1] = now
                l_list[next][0] = now
    
    return "".join(answer)

# 참고 - https://minhyeok-rithm.tistory.com/entry/%ED%91%9C-%ED%8E%B8%EC%A7%91-1  