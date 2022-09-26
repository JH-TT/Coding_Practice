def check():
    s = list(input())
    t = list(input())
    while len(t) >= len(s):
        if t == s:
            return 1
        if t[-1] == "A":
            t.pop()
        else:
            t.pop()
            t = list(reversed(t))
    return 0

print(check())

# t부터 하나씩 빼면서 확인하면 됨.