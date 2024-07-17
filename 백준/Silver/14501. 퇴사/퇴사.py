# 입력값 : N, 상담 날짜+금액
# 퇴사 전에 할 수 있는 최대 이익
# DP
# i번째 일까지 일했을 때 얻을 수 있는 최대


import sys

read = sys.stdin.readline

n = int(read())

t = [0 for _ in range(n)]
p = [0 for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n):
    t[i], p[i] = map(int, read().split())

for i in range(n, -1, -1):
    if(i+t[i-1]> n+1):
        dp[i-1] = dp[i]
    else:
        dp[i-1] = max(dp[i], dp[i+t[i-1]-1]+p[i-1])
print(dp[0])
        


