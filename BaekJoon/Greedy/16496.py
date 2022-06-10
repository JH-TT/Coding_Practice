n = int(input())
nums = list(input().split())

nums = list(map(lambda x : x*9, nums))
nums.sort(reverse = True)
nums = list(map(lambda x : x[:len(x)//9], nums))
print(str(int("".join(nums))))

# 문자열로 sort하면 각 인덱스별로 비교하므로
# 자릿수가 다른 수랑 비교하기위해 최소 9번 반복시켜서 비교함. 최대 10억-1 까지이므로 한자릿수랑 9자릿수랑 비교할 수도 있으니 9번 곱한다.
# 내림차순으로 정렬하고, 다시 슬라이싱한다.
# join함수를 이용해서 출력한다.
# 이때 0이 맨 앞에 있을 수 없고, 000 이런식으로 있을 수 없으니 int를 써서 정수로 바꿔주고 출력한다.