from collections import defaultdict
import sys
input = sys.stdin.readline

# 1 ~ 9
# 5 : V
# 10 : X
# 50 : L
# 100 : C
# 500 : D
# 1000 : M
arabia_one = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
arabia_ten = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
arabia_hun = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
arabia_tho = ["", "M", "MM", "MMM"]

arabia_to_num = defaultdict(lambda: 0)
for i in range(1, len(arabia_one)):
    arabia_to_num[arabia_one[i]] = i
for i in range(1, len(arabia_ten)):
    arabia_to_num[arabia_ten[i]] = i * 10
for i in range(1, len(arabia_hun)):
    arabia_to_num[arabia_hun[i]] = i * 100
for i in range(1, len(arabia_tho)):
    arabia_to_num[arabia_tho[i]] = i * 1000

for _ in range(int(input())):    
    str = list(input().rstrip())
    # 숫자 -> 아라비아
    if str[0].isdigit():
        res = ""
        for i in range(1, len(str) + 1):
            ten = 10 ** (len(str) - i)
            if ten == 1000:
                res += arabia_tho[int(str[i-1])]
            elif ten == 100:
                res += arabia_hun[int(str[i-1])]
            elif ten == 10:
                res += arabia_ten[int(str[i-1])]
            else:
                res += arabia_one[int(str[i-1])]
        print(res)
    else: # 아라비아 -> 숫자
        res = 0
        ara = ""
        for s in str:            
            ara += s
            if arabia_to_num[ara] == 0:
                res += arabia_to_num[ara[:-1]]
                ara = ara[-1]
        if arabia_to_num[ara] == 0:
            res += arabia_to_num[ara[:-1]]
            ara = ara[-1]
        res += arabia_to_num[ara]
        print(res)