from datetime import datetime
from collections import defaultdict
import sys
input = sys.stdin.readline

def to_minute(t):
    deadline = t.split("/") # 날짜와 분리
    h_m = deadline.pop()
    deadline.extend(h_m.split(":")) # 시, 분 분리
    d = 24 * 60
    h = 60
    return int(deadline[0]) * d + int(deadline[1]) * h + int(deadline[2])

log, d, fee = input().split()
d = to_minute(d)
borrow = defaultdict(dict) # 각 사람이 어떤 부품을 언제 빌렸는지 dict형식으로 저장.
offender_fee = defaultdict(int) # 각 사람의 벌금
date_format = "%Y-%m-%d %H:%M"

for _ in range(int(log)):
    data = input()
    date = data[:16]
    part, person = data[16:].split()
    # 반납이면 벌금계산.
    if borrow[person].get(part):
        b_date = borrow[person][part]
        # date형식으로 변환
        return_date = datetime.strptime(date, date_format)
        borrow_date = datetime.strptime(b_date, date_format)
        period = return_date - borrow_date
        a = period.days * 24 * 60 + period.seconds // 60 # 총 기간을 분으로 변환
        diff = a - d # 유효기간을 빼준다.
        if diff > 0: # 빌린 기간이 유효기간보다 길면 벌금청구
            offender_fee[person] += diff * int(fee)
        del borrow[person][part]
    # 빌리는거면 추가.
    else:
        borrow[person][part] = date

offender = sorted(offender_fee.keys())
if offender:
    for i in offender:
        print(i, offender_fee[i])
else:
    print(-1)
# 처음에는 borrow를 defaultdict(list)형식으로 해서 데이터를 찾을때 for문을 이용해야하는 바람에
# 시간초과가 떴다. 그래서 dict로 해결