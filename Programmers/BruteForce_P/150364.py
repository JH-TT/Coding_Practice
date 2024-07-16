def solution(edges, target):
  answer = []
  n = len(edges) + 1
  tree = [[] for _ in range(n + 1)]
  idx = [0 for _ in range(n + 1)]
  leaf_cnt = 0

  for edge in edges:
      tree[edge[0]].append(edge[1])

  for i in range(1, n + 1):
      if len(tree[i]) == 0 and target[i-1] != 0:
          leaf_cnt += 1
          continue
      tree[i].sort()

  count = [0 for _ in range(n + 1)]    
  # target이 되기위한 count를 계산한다.
  # 모든 리프 노드가 count * 1 <= target <= count * 3 이 되면 성공
  # 만약 어느 하나라도 target < count * 1 이 되는 순간 -1 리턴
  # 각 리프 노드마다 count가 있을것이고 여기서부터 1, 2, 3을 넣으면서
  # (count-1) * 1 <= target-숫자카드 <= (count-1) * 3가 유지되는지 확인한다.

  idx = [0 for _ in range(n + 1)] # 현재 부모노드가 자식노드를 가리키는 인덱스
  success_flag = [False for i in range(n + 1)] # target범위안에 들어오는 경우
  success = 0
  # target 범위 탐색하기
  seq = []
  while True:
      i = 1
      # 리프노드 가져오기
      while len(tree[i]) != 0:
          child = tree[i][idx[i]] # 자식을 가져온다.
          idx[i] = (idx[i] + 1) % len(tree[i])
          i = child
      # 여기부터 i는 리프노드

      # 일단 drop을 했다고 하자
      count[i] += 1
      seq.append(i)
      # 그러면 횟수가 1증가했다.

      # 이때 target이 더 적어지면 가망이 없으므로 종료한다.
      if target[i-1] < count[i] * 1:
          return [-1]          
      # target을 확인하면서 범위에 들어오면 성공 카운트를 올려준다.
      if success_flag[i] == False and (count[i] * 1 <= target[i-1] <= count[i] * 3):
          success_flag[i] = True
          success += 1        
      # 모든 노드가 target을 충족하는 경우 더이상 볼 필요 없으니 반복문 종료
      if success == leaf_cnt:
          break        
  # 현재 seq는 최소한의 개수를 선정하게 된 상황.
  # 여기서 부터는 1, 2, 3 을 넣으면서 target이 계속 유지되는지 본다.
  for s in seq:
      flag = False
      # 1, 2, 3을 하나씩 넣으면서 target이 범위안에 계속 있을 수 있는지 확인한다.
      for i in [1, 2, 3]:
          if (count[s]-1) * 1 <= target[s-1]-i <= (count[s]-1) * 3:
              flag = True
              target[s-1] -= i
              answer.append(i)
              count[s] -= 1
              break
      # 1, 2, 3을 다 넣었지만 그래도 target이 유지되지 않으면 실패
      if not flag:
          return [-1]
  return answer

# 구현 자체가 어려운건 아니었는데 아이디어를 떠올리는게 쉽지 않았던 문제