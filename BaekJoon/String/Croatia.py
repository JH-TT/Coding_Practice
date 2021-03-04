# 2941번
a = input()
# 특정 문자가 있다면 나만의 표시로 바꿔두기
a = a.replace("lj", ".")
a = a.replace("nj", ".")
a = a.replace("dz=", ".")
print(len(a) - a.count("=") - a.count("-"))  # =와 -는 다른 알파벳 하나와 합쳐져 하나의 크로아티아 알파벳이 되므로 한번씩 빼준다.