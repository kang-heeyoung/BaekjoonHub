'''
윷놀이 Y(2), 같은 그림 찾기 F(3), 원카드 O(4)
인원수 부족 시 게임 시작 x

임스와 같이 플레이하기를 신청한 횟수 N, 플레이할 게임의 종류가 주어질때
최대 몇번 임스와 함께 플레이 할 수 있는지

- 임스는 한 번 같이 플레이한 사람과는 다시 플레이하지 않음
- 동명이인 x

input
신청한 횟수 N 플레이할 게임의 종류
같이 플레이하고자 하는 사람들의 이름(N 개)

output

시간 복잡도 1s
N <= 100,000
N^2 가능
'''

import sys
read = sys.stdin.readline

people = []

N, category = read().split()
N = int(N)

for i in range(N):
    p = read()
    people.append(p)

people=list(set(people))
num = len(people)

if category == 'Y':
    print(num)
elif category == 'F':
    print(num//2)
elif category == 'O':
    print(num//3)



