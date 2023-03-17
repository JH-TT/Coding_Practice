def solution(numbers, hand):
    answer = ''
    left = "*"
    right = "#"
    loc = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           "*": [3, 0], 0: [3, 1], "#": [3, 2]}
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            left = num
        elif num in [3, 6, 9]:
            answer += "R"
            right = num
        else:
            ldist = sum([abs(loc[num][0]-loc[left][0]), abs(loc[num][1]-loc[left][1])])
            rdist = sum([abs(loc[num][0]-loc[right][0]), abs(loc[num][1]-loc[right][1])])
            if ldist < rdist:
                answer += "L"
                left = num
            elif ldist > rdist:
                answer += "R"
                right = num
            else:
                if hand == "left":
                    answer += "L"
                    left = num
                else:
                    answer += "R"
                    right = num
    
    return answer

# 그냥 구현문제
# 각 숫자 위치를 딕셔너리로 저장한 뒤 거리계산할때 편리하게 사용했다.