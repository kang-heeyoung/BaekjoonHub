import sys
read = sys.stdin.readline


T = int(read())

for _ in range(T):
    R, S = read().split()
    for c in list(S):
        for _ in range (int(R)):
            print(c, end="")
    print(end="\n")

