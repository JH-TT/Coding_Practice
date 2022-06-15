n = int(input())
cnt = 0
warn = 666
while 1:
    if "666" in str(warn):
        cnt += 1
    if cnt == n:
        print(warn)
        break      
    warn += 1
# 생각보다 바로 떠올리지 못했음...
# 666부터 시작해서 wran에 666이 있을때 마다 cnt를 1씩 증가.
# warn도 계속 1씩 증가하다가 cnt가 n이 되면 warn출력 후 반복문 빠져나옴.