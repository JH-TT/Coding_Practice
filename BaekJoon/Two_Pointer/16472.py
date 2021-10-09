import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().rstrip())

al = {}
length = 0

i = 0
j = 0
while j < len(arr):
    if arr[j] not in al:
        al[arr[j]] = 1
    else:
        al[arr[j]] += 1
    
    if len(al) > n: # 요구 알파벳의 종류가 넘으면
        length = max(length, j - i) # 지금까지의 길이 저장.
        while len(al) > n: # 요구수치로 돌아올때 까지 반복.
            if al[arr[i]] == 1: # 빼야할 알파벳 개수가 1개면 딕셔너리에서 삭제
                al.pop(arr[i])
            else:
                al[arr[i]] -= 1
            i += 1  # 뒤쪽 인덱스값 증가
    j += 1

length = max(length, j - i) # 남은 문자열의 길이

print(length)

# 투 포인터로 이용하는 문제.
# 그냥 리스트로만 해결하려하면 시간초과뜸. 딕셔너리를 활용해서 데이터를 쉽게 처리하기.