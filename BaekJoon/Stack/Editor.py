from collections import deque # 빨리 입력받고 삭제위해 deque이용.
import sys
input = sys.stdin.readline

array = deque(input().rstrip()) # sys를 이용하면 \n도 입력되기 때문에 \n은 없앤상태로 입력받음.
sub = deque() # 커서 오른쪽들은 여기에 저장.

n = int(input())
for _ in range(n):
    com = list(input().split())
    if com[0] == "L" and len(array) != 0:
        sub.appendleft(array.pop()) # 커서를 왼쪽으로 옮기면 커서의 오른쪽에 있는 문자는 sub에 저장.
    elif com[0] == "D" and len(sub) != 0:
        array.append(sub.popleft()) # 커서를 오른쪽으로 옮기면 sub에있는 문자를 array에 다시 옮김.
    elif com[0] == "B" and len(array) != 0:
        array.pop() # 없애는건 그냥 pop이용
    elif com[0] == "P":
        array.append(com[1]) # 추가는 append이용.

array = array + sub  # 커서 왼쪽 문자들과 오른쪽 문자들 합침.

print(''.join(array))