def solution(n):
    return int(change_to_three(n), 3)

def change_to_three(n):
    total = ''
    while n > 0:
        total += str(n % 3)
        n //= 3
    return total