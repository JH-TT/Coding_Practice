import sys
input = sys.stdin.readline

n,m=map(int,input().split())
n+=1
a=[0]*n
d=[0]*n
for i in range(1,n):
    a[i]=[0]+list(map(int,input().split()))
    d[i]=[0]*n
a[0]=d[0]=[0]*n

for i in range(1,n):
    for j in range(1,n):
        d[i][j]= a[i][j] + d[i-1][j] + d[i][j-1] - d[i-1][j-1]

for t in range(m):
    q,w,e,r=map(int,input().split())
    print(d[e][r] - d[e][w-1] - d[q-1][r] + d[q-1][w-1])

# 이 문제는 점화식을 나타내기 꽤나 까다로웠던 문제.
# 나타내는 방법을 알고싶으면 
# https://blog.naver.com/kanjw950717/222257559476
# https://blog.naver.com/jjys9047/222251594151 이 두 군데 중 아무데서나 봐라.

# ㅁ ㅁ ㅁ ㅁ
# ㅁ ㅂ ㅂ ㅂ
# ㅁ ㅂ ㅂ ㅂ
# ㅁ ㅂ ㅂ ㅂ 에서 ㅂ만 부분합을 구하고 싶으면, 일단 1열에 있는 ㅁ의 합과 1행의 ㅁ의 합을 빼고, (1, 1)좌표의 값만 2번뺐으니 1번 더해주는 형식.
# 즉 x1, y1, x2, y2가 주어졌다면
# dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1-1][y1-1]이 되고 이를 이항시켜서 특정 좌표의 누적합을 유도해 보면
# dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + board[i][j] -> board는 원래 리스트