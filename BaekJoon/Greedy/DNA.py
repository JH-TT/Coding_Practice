n, m = map(int, input().split())
l = [input() for _ in range(n)]
ans = ""
dist = 0
s = "ACGT" # 만약 중복된 수의 최댓값이 같은게 있는 경우 알파벳순으로 저장.
for i in range(m):
    tmp = [l[j][i] for j in range(n)] # 1열씩 넣는다.
    d = 0
    for c in s:
        if d < tmp.count(c): # 중복개수가 d보다 크면 그 중복개수를 d로 선언.
            d = tmp.count(c)
            x = c # 그 중복개수가 큰 알파벳을 x로 저장.
    ans += x # 가장 많이 중복된 알파벳을 ans에 더함.
    dist += n - tmp.count(x) # 문자가 다른개수를 더해준다.
print(ans)
print(dist)

# 나는 다른 코드로 작성해 풀었지만, 내가 간과한것이 DNA는 ACGT 이렇게만 있다는 것을 잊고 모든 알파벳으로 입력했을때로 코딩했다보니 좀 코드가 길고, 난잡해 보여서 좀 간단한 코드를 찾아서 올린다. 알고리즘은 내가 할거랑 같다. - 브루스포스알고리즘 -