from collections import defaultdict

def solution(str1, str2):
    
    a = defaultdict(int)
    b = defaultdict(int)
    
    gyo = 0 # 교집합 원소 개수
    hap = 0 # 합집합 원소 개수
    
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha(): # 해당 문자열이 알파벳으로 구성된거면 개수 1 증가
            a[str1[i:i+2].upper()] += 1
    
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            b[str2[i:i+2].upper()] += 1

    # 교집합이 둘 다 공집합이면 65536 리턴.
    if not a and not b:
        return 65536

    # a기준으로 교집합 실행.
    for i in a.keys():
        gyo += min(a[i], b[i])
        hap += a[i]
        
    for i in b.keys():
        hap += b[i]
    # n(A | B) -> n(A) + n(B) - n(A & B) 이용.
    hap -= gyo
    total = gyo / hap
    
    return int(65536 * total) # 정수부분만 출력하기위해 int사용