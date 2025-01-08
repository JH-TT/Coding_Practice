def solution(diffs, times, limit):
  answer = max(diffs)
  left = 0
  right = max(diffs) + 1
  times = [0] + times # 첫 퍼즐부터 숙련도보다 높으면 이전 퍼즐이 없기때문에 추가 조건을 넣기 귀찮으니 항등원을 넣어준다.
  while left + 1 < right:
      mid = (left + right) // 2

      total_time = 0
      for i in range(len(diffs)):
          # 충분한 숙련도의 경우 time_cur만큼 사용
          if diffs[i] <= mid:
              total_time += times[i+1]
          else: # 숙련도가 부족하면 이전 퍼즐 다시하고 옴 (이때 diff - mid 만큼 반복)
              total_time += (times[i+1] + times[i]) * (diffs[i] - mid)
              total_time += times[i+1] # diff-mid만큼 반복하고 와서야 time_cur을 소비해서 성공

      if total_time <= limit:
          answer = min(answer, mid)
          right = mid
      else:
          left = mid

  return answer
    
# 전형적인 이분탐색 문제