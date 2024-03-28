import sys
read = sys.stdin.readline

a = 0 # 300
b = 0 # 60
c = 0 # 10

T = int(input())

if T%10 != 0:
    print("-1")
else:
    a = T // 300
    T = T % 300
    b = T // 60
    T = T % 60
    c = T // 10
    print(a,b,c)


    