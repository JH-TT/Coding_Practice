import sys
out = sys.stdout

n = int(input())
out.write("? 1\n")
out.flush()
a = int(input())
out.write("? " + str(n) + "\n")
out.flush()
b = int(input())
if a == 1 and b == 0:
    out.write("! -1\n")
elif a == 0 and b == 1:
    out.write("! 1\n")
else:
    out.write("! 0\n")
out.flush()

# 첫번째와 마지막만 알면 된다.
# 왜냐면 첫번째와 마지막을 제외한 나머지는 오르막길과 내리막길이 동시에 발생하기 때문이다.