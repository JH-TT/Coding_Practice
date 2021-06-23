from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    n = len(truck_weights)
    # truck_weights = deque(truck_weights)
    passing_truck = []
    passed_truck = []
    t = []
    
    while len(passed_truck) != n:
        i = 0
        # 현재 다리위 차들이 1초씩 지났을음 나타내고, 만약 다리를 지나는 시간이 되면 빼준다.
        while i < len(t):
            t[i] += 1
            if t[i] > bridge_length:
                passed_truck.append(passing_truck.pop(0))
                t.pop(0)
            else:
                i += 1
        # 대기트럭이 있고, 다리위 트럭무게 + 가장 앞에 있는 트럭 무게가 다리가 버티는 무게보다 작으면 넣는다.
        if (len(truck_weights) != 0) and (truck_weights[0] + sum(passing_truck) <= weight):
            passing_truck.append(truck_weights.pop(0))
            t.append(1)
        
        answer += 1
    
    
    return answer
# 중간에 deque가 있는데, 그냥 리스트랑 큐를 이용해서 해보니까 그냥 리스트가 좀 더 빨랐다.