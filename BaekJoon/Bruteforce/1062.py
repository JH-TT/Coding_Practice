import sys
from itertools import combinations
input = sys.stdin.readline

wordNum, letterNum = map(int, input().split())

if letterNum < 5 : # 기본 중복 알파벳개수보다 적으면 0개 출력 후 종료.
    print(0)
    exit(0)

base = {'a', 'n', 't', 'i', 'c'} # 모든 문자열은 anta로 시작해서 tica로 끝난다고 했음. 기본 중복 알파벳

wordSets = [] # 단어를 담을 곳.
allSet = set({}) # 모든 중복된 알파벳
for _ in range(wordNum) :
    wordSet = set(input().rstrip())
    wordSets.append(wordSet)
    allSet |= wordSet

otherSet = allSet - base # 모든 중복된 알파벳에서 기본 중복 알파벳을 빼 준다.

otherSetLen = len(otherSet)
if otherSetLen <= letterNum - 5 : # 나머지 알파벳 길이가 더 적으면 antatica밖에 없단 소리.
    print(wordNum)
    exit(0)
else : # 그외엔 letterNum - 5개의 알파벳을 제외한 나머지를 뽑는다.
    candidates = combinations(otherSet, len(otherSet) - (letterNum - 5))

result = 0
for candidate in candidates :
    tmpSet = allSet - set(candidate) # 모든 알파벳에서 candidate를 빼 주면, 현재 배운 알파벳들이 된다.
    cnt = 0
    for wordSet in wordSets :
        if wordSet <= tmpSet : # 현재 단어가 배운 알파벳 수보다 적거나 같으면 그 단어를 배울 수 있다는 의미.
            cnt += 1
    result = max(result, cnt) # 큰 값을 계속 업데이트 시켜준다.

print(result)