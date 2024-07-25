'''
(x,y), (p,q)
x>p, y>q 인 경우에만 덩치가 더 큼

시간복잡도
1초 : 1억번 연산
N = 50


input
전체 사람의 수 : N
각 사람의 몸무게와 키 ( x, y)

'''

import sys
read = sys.stdin.readline

n = int(read())
list_human = []
rank = [1 for _ in range(n)]

for i in range(n):
    x = list(map(int, read().split()))
    list_human.append(x)

for i in range(n):
    for j in list_human:
        if list_human[i][0] < j[0] and list_human[i][1] < j[1]:
            rank[i] += 1

print(*rank)

