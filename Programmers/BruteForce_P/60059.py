def solution(key, lock):    
    def spin(a):
        b = []
        for i in a:
            b.append([i[1], n-i[0]-1])            
        return b
    
    answer = False
    key_cor = []
    lock_cor = []
    
    m = len(key)
    n = len(lock)
    for i in range(m):
        for j in range(m):
            if key[i][j] == 1:
                key_cor.append([i, j])
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                lock_cor.append([i, j])
              
    for k in range(4):
        key_cor = spin(key_cor)
        
        for i in range(-n, n+1):
            for j in range(-n, n+1):
                a = []
                for h in key_cor:
                    if h[0]+i < 0 or h[0]+i >= n or h[1]+j<0 or h[1]+j>=n:
                        continue
                    a.append([h[0]+i, h[1]+j])
                a.sort()
                if a == lock_cor:
                    return True
                
  
    return answer

# 풀이방식
# 열쇠의 돌기부분 좌표와 자물쇠의 홈부분 좌표를 각각 리스트에 저장해 놓는다.
# 열쇠의 좌표들을 90도씩 돌리고, 그 상태에서 상하좌우를 움직이면서 자물쇠의 홈 부분과 맞춰본다
# 맞으면 바로 True를 출력, 전부 확인을 해도 못찾았으면 False를 출력한다.