def solution(number, k):
    answer = ''
    if k <= 0:
        return number
    if len(number) == k+1:
        return max(number)
    
    stack = [number[0]]
    for i in number[1:]:
       #만약 stack의 원소보다 큰 것이 나오면 다 제거 후, 큰 숫자 넣음.
        while len(stack) > 0 and stack[-1] < i and k > 0:
            k -= 1
            stack.pop()
        stack.append(i)
    # 만약 뒤의 숫자가 앞의 숫자보다 작거나 같으면 k가 감소되지 않고 넘어온다.
    # 이럴 땐 k 만큼의 개수를 뒤에서 제거 후 출력.
    if k != 0:
        stack = stack[:-k] # 뒤에서 k개 제거.
    
    return ''.join(stack)