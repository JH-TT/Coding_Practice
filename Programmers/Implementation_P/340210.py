def solution(expressions):
  answer = []
  hints = []; no_answer = []
  min_bin = 2
  max_bin = 9

  # 답이 있는 식과 답이 없는 식을 분리한다.
  # 분리하면서 최소 진수를 구한다.
  for ex in expressions:
      for n in ex:
          if n.isdigit():
              min_bin = max(min_bin, int(n) + 1)

      if ex[-1] == "X":
          no_answer.append(ex)
      else:
          hints.append(ex)

  # 답이 있는 식으로부터 유추해 본다.
  # 1. 왼쪽의 i번째 자리 숫자가 오른쪽의 i번째 자리 숫자보다 크다 -> 몇 진수인지 확인 불가능
  # 2. 왼쪽의 자리 숫자가 오른쪽의 자리 숫자보다 작다 -> |10진수로 생각하고 계산한 결과 - 결과 값의 일의 자리|가 해당 진수.
  # 3. 같으면 0 -> 몇 진수인지 확인 불가능
  # 최소 진수, 최대 진수를 유추해 간다. (최대 진수를 넣은 이유는 정확한 진수를 찾았는지 확인하기 위함)

  for h in hints:
      left, oper, right, _, ans = h.split() # 왼쪽, 연산자, 오른쪽, 결과를 미리 나눈다

      left = list(map(int, left))
      right = list(map(int, right))
      ans = list(map(int, ans)) # 각 자릿수를 리스트로 표현한다.

      left = [0] * (3 - len(left)) + left
      right = [0] * (3 - len(right)) + right
      ans = [0] * (3 - len(ans)) + ans # 3자리 정도로 정한다. (최대 3자리이기 때문)

      i = 2
      while i >= 0:
          if oper == "+":
              d_num = left[i] + right[i]
              if d_num >= 10:
                  d_num -= 10
          else:
              d_num = left[i] - right[i]
              if d_num < 0:
                  d_num += 10

          if d_num - ans[i] == 0: # 십진수와 같은 결과면 얻을 건 없다.
              i -= 1
              continue

          if oper == "+" and (d_num > ans[i]):
              diff_bin = 10 + ans[i] - d_num
          elif oper == "-" and (ans[i] > d_num):
              diff_bin = 10 + d_num - ans[i]
          else:
              diff_bin = max(d_num, ans[i]) - min(d_num, ans[i])

          # 만약 0이 아니면 diff_bin이 해당 진수이고 반복문을 바로 종료해도 된다.
          min_bin = 10 - diff_bin
          max_bin = 10 - diff_bin
          break

      if min_bin == max_bin: # 최소 진수와 최대 진수가 같으면 더 볼 필요 없다.
          break
  flag = (min_bin == max_bin)
  for no in no_answer:
      left, oper, right, _, _ = no.split()

      left2 = list(map(int, left))
      right2 = list(map(int, right))

      # 여유롭게 3자리로 한다.
      left2 = [0] * (3 - len(left2)) + left2
      right2 = [0] * (3 - len(right2)) + right2
      ans = []

      # 진수를 알고 있으면 10진수로 바꿔서 계산한다.
      if flag:
          l_deci = pow(min_bin, 2) * left2[0] + pow(min_bin, 1) * left2[1] + pow(min_bin, 0) * left2[2]
          r_deci = pow(min_bin, 2) * right2[0] + pow(min_bin, 1) * right2[1] + pow(min_bin, 0) * right2[2]

          if oper == "+":
              a = l_deci + r_deci
          else:
              a = l_deci - r_deci

          while a != 0:
              ans.append(str(a % min_bin))
              a //= min_bin
      else:
          i = 2
          while i >= 0:
              if oper == "+":
                  s = left2[i] + right2[i]
                  # 최소 진수 안에서 계산이 되면 ans에 넣는다.
                  if s < min_bin:
                      ans.append(str(s))
                  # 올림이 발생하면 바로 ?로 바꾼다.
                  else:
                      ans = ["?"]
                      break
              else:
                  if left2[i] >= right2[i]:
                      ans.append(str(left2[i] - right2[i]))
                  else:
                      ans = ["?"]
                      break
              i -= 1
      if ans == ["?"]:
          answer.append(left + " " + oper + " " + right + " = " + "?")
      else:
          an = ""
          for i in range(len(ans)-1, -1, -1):
              if an == "" and ans[i] == "0":
                  continue
              an += ans[i]
          if an == "":
              an = "0"
          answer.append(left + " " + oper + " " + right + " = " + an)

  return answer

# 그냥 쌩 구현이었는데 런타임에러 때문에 애먹었다...
# 앵간하면 함수 쓰는것보단 for문 돌려서 만드는게 더 나은듯...