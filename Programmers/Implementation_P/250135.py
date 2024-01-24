def solution(h1, m1, s1, h2, m2, s2):
  def meetCount(h, m, s):
      hd, md, sd = (h*30 + 0.5*m + s*0.5/60) % 360, 6*m+0.1*s, 6*s
      cnt = -1
  
      if sd >= hd: cnt += 1 
      if sd >= md: cnt += 1
  
      cnt += (h * 60 + m) * 2
      cnt -= h
      if (h >= 12): cnt -= 2
  
      return cnt
return meetCount(h2, m2, s2) - meetCount(h1, m1, s1) + ((h1==0 or h1==12)and m1==0 and s1==0)

# 참고: https://school.programmers.co.kr/questions/63464
# 요약: (00:00:00부터 h2:m2:s2까지 만난횟수) - (00:00:00부터 h1:m1:s1까지 만난횟수)로 결과를 구했음.