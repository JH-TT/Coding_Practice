def divide_char(s, n):
    divided = []
    idx = 0
    while idx < len(s):
        if idx + n >= len(s):
            divided.append(s[idx:])
            break
        divided.append(s[idx:idx+n])
        idx += n
    return divided

def count_char(arr):
    before = arr[0]
    cnt = 1
    after = []
    for i in range(1, len(arr)):
        if before == arr[i]:
            cnt += 1
        else:
            if cnt > 1:
                after.append(str(cnt) + before)
            else:
                after.append(before)
            before = arr[i]
            cnt = 1
    if cnt > 1:
        after.append(str(cnt) + before)
    else:
        after.append(before)

    return len("".join(after))

def solution(s):
    answer = 10000
    if len(s) == 1: return 1
    for i in range(1, (len(s)//2) + 1):
        d = divide_char(s, i)
        answer = min(answer, count_char(d))
    
    return answer