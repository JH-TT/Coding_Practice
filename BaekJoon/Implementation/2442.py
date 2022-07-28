n = int(input())

for i in range(1, n+1):
    a = "*" * (2 * i - 1)
    b = " " * (n-i)
    print(f"{b}{a}")

# f-string이용