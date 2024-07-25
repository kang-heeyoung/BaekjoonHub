'''
1. 금메달 수가 더 많은 나라
2. 금메달 수가 같을 경우 은메달 수가 더 많은 나라
3. 은메달 수가 같을 경우 동메달 수가 더 많은 나라

각 국가 : 1~N(정수)
등수 : (자신보다 더 잘한 나라 수) + 1
두 나라가 금,은,동 수가 모두 같다면 같은 등수

input
전체국가수 / 등수 알고 싶은 나라 번호
나라번호 금 은 동

output
해당 국가의 등수
'''

import sys
read = sys.stdin.readline

n , k = map(int,read().split())
rank = 1
medal = {}
x = []

for i in range(n):
    x = list(map(int, read().split()))
    medal[x[0]] = x[1:]

for i in range(1,n+1):
    if i != k:
        if medal[i][0] >medal[k][0] or (medal[i][0] == medal[k][0] and medal[i][1] > medal[k][1]) or (medal[i][1] == medal[k][1] and medal[i][2] > medal[k][2]):
           rank += 1
        

print(rank)
    

