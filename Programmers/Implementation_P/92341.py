from collections import defaultdict
import math, heapq

def solution(fees, records):
    answer = []
    max_time = 23*60+59
    parking = defaultdict(int)
    fee = defaultdict(int)
    for rec in records:
        t, num, type = rec.split()
        if num not in answer:
            answer.append(num)
        if type == "IN":
            parking[num] = change_time(t)
        else:
            fee[num] += change_time(t) - parking[num]
            del parking[num]
    
    for p in parking:
        fee[p] += max_time - parking[p]
    answer.sort()
    return [max(fees[1] + math.ceil((fee[a]-fees[0])/fees[2])*fees[3], fees[1]) for a in answer]

def change_time(t):
    h, m = map(int, t.split(":"))
    return h*60+m