def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key = lambda x : (x[col-1], -x[0]))
    S_ = []
    for i in range(row_begin-1, row_end):
        total = 0
        for j in data[i]:
            total += (j % (i+1))
        S_.append(total)
    
    for s in S_:
        answer ^= s
    
    return answer