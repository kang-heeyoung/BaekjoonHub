# W개씩 H행
# 세로로 N칸, 가로로 M칸

import sys
read = sys.stdin.readline

H, W, N, M = map(int, read().split())

if W%(M+1)==0:
    width = W//(M+1)
else:
    width = W//(M+1)+1

if H%(N+1) == 0:
    height = H//(N+1)
else:
    height = H//(N+1)+1

print(width*height)
