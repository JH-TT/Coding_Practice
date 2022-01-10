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


# 다른 풀이

def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)] # 범위를 벗어나도 끝에서 자른다
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res) # min 함수 안에는 for문을 이용할 수 있다.

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])