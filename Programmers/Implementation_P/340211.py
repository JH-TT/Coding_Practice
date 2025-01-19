def get_path(sr, sc, er, ec, track):
  now_r = sr
  now_c = sc

  while now_r != er or now_c != ec:

      if now_r > er:
          now_r -= 1
          track.append([now_r, now_c])
          continue

      if now_r < er:
          now_r += 1
          track.append([now_r, now_c])
          continue

      if now_c > ec:
          now_c -= 1
          track.append([now_r, now_c])
          continue

      if now_c < ec:
          now_c += 1
          track.append([now_r, now_c])
          continue

def solution(points, routes):
  answer = 0
  points = [[]] + points

  robot_tracks = []

  for i, route in enumerate(routes):
      track = [[points[route[0]][0], points[route[0]][1]]]
      start_point = route[0]

      for j in range(1, len(route)):
          end_point = route[j]

          sr, sc = points[start_point]
          er, ec = points[end_point]

          get_path(sr, sc, er, ec, track)

          start_point = end_point

      robot_tracks.append(track)

  max_idx = max(len(i) for i in robot_tracks)

  for i in range(max_idx):
      cor = set()
      cor_check = set()

      for j in range(len(robot_tracks)):
          if len(robot_tracks[j]) <= i:
              continue

          r, c = robot_tracks[j][i]

          if (r, c) in cor_check:
              continue

          if (r, c) in cor:
              cor_check.add((r, c))
              continue

          cor.add((r, c))
      answer += len(cor_check)

  return answer

# 이 문제의 핵심은 r좌표 먼저 이동후, c좌표 이동이다.
# 따라서 로봇은 직선, ㄱ, ㄴ자 모양으로만 움직인다고 보면 된다.

# 나는 처음엔 r좌표 먼저 이동한다는걸 bfs에서 r좌표쪽을 먼저 보는걸로 잘못 이해해서 문제를 푸는데 실패했다.
# 그냥 r좌표 먼저 넣고 c좌표 넣고 비교했으면 충분히 풀고도 남았던 문제...
# 오랜만에 문제 풀려고 하니 이런 실수를 하게되네...