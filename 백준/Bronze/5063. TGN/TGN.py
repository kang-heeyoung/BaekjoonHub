import sys
read = sys.stdin.readline

T = int(read())

for i in range(T):
    r, e, c = map(int, read().split())
    if r<e-c:
        print("advertise")
    elif r == e-c:
        print("does not matter")
    else:
        print("do not advertise")