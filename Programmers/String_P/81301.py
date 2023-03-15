def solution(s):
    num_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
               "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    
    for num in num_dict:
        s = s.replace(num, num_dict[num])
    
    return int(s)
# 근데 replace의 시간복잡도는
# O(문자열의 길이 * (교체할 문자열의 길이 + 교체되는 문자열의 길이/교체할 문자열의 길이)) 이다.