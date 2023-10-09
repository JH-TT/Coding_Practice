from collections import defaultdict
import re

def solution(word, pages):
    answer = 0
    MAX = 0

    cnt = defaultdict(lambda: [0, 0, 0]) # 인덱스, 기본점수, 링크점수
    
    # 자기 자신 링크 가져오기
    idx = 0
    for page in pages:
        # 자신의 링크 파싱
        myLinksp = page.split("<meta property=\"og:url\" content=\"https://")
        myLink = myLinksp[1][:myLinksp[1].index('"')]
        cnt[myLink][0] = idx # 인덱스 저장
        
        # 단어들 가져오기
        wordsp = re.split(r'[^a-zA-Z]', page)
        wordCnt = 0
        for w in wordsp:
            if w == '': continue
            if w.lower() == word.lower():
                cnt[myLink][1] += 1
        
        # 외부링크 점수 더하기
        
        # 외부링크 가져오기
        outerLinksp = page.split("<a href=\"https://")
        outerCnt = len(outerLinksp[1:])
        for outer in outerLinksp[1:]:
            outerLink = outer[:outer.index('"')]
            # 자신의 링크 점수 더하기
            cnt[outerLink][2] += (cnt[myLink][1] / outerCnt)
        
        idx += 1
    
    for page in pages:
        # 자신의 링크 파싱
        myLinksp = page.split("<meta property=\"og:url\" content=\"https://")
        myLink = myLinksp[1][:myLinksp[1].index('"')]
        if cnt[myLink][1] + cnt[myLink][2] > MAX:
            answer = cnt[myLink][0]
            MAX = cnt[myLink][1] + cnt[myLink][2]

    return answer

# 메타데이터 부분을 잘못 파싱해서 애먹었었다... 주어진 테케는 다 성공해서 의심을 안했음..
# property="og:url" 의 content=https://로 봐야하는데 content=https://로만 파싱해서 생긴 일이었다.