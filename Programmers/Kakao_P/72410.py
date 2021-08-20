def solution(new_id):
    answer = ''
    
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

    # 1 -> 함수가 있다는건 알았는데 뭐였는지 까먹었음.
    new_id = new_id.lower()
    
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c        
    
    # 3 -> 이 방법은 생각 못했음...
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]        
    
    # 5
    if answer == '':
        answer = 'a'
    
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7
    while len(answer) <= 2:
        answer += answer[:-1]

    
    return answer

# 정규표현식을 이용.
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    # sub('패턴', '변경문자열', '문자열', 변경횟수) : 패턴과 일치되는 부분을 다른 문자로 변경
    st = re.sub('[^a-z0-9\-_.]', '', st) # [^ ]는 not을 의미. a-z는 소문자 a 부터 z까지. 0-9는 숫자. \-_.은 \-는 -를 문자로 둔다는것, 나머지는 그냥 문자들을 의미하므로 소문자, 숫자. - _ . 을 제외한 나머지를 비운다 보면됨.
    st = re.sub('\.+', '.', st) # +는 반복됨을 의미
    st = re.sub('^[.]|[.]$', '', st) # 여기서의 ^는 시작부분, $는 끝부분을 의미
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st