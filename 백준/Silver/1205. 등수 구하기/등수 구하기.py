'''
랭킹리스트 순서가 곧 등수 (공동 등수 존재)
새로운 점수가 랭킹 리스트에서 몇 등 하는 지 구하기
랭킹 리스트에 올라갈 수 없을 경우 -1

input
N(리스트에 있는 개수), 태수의 새 점수, P(랭킹 리스트에 올라 갈 수 있는 점수의 개수)
현재 랭킹에 있는 점수(비오름차순)

output
새로운 점수의 등수
'''
import sys
read = sys.stdin.readline

N, new_score, list_num = map(int,read().split()) 

# N이 0이 들어올 경우
if N != 0:
    rank = list(map(int, read().split()))
else:
    rank = []
total_rank = 1

if N != 0 and rank[N-1] >= new_score and list_num == N:
    print(-1)
else:
    for i in rank:
        if i>new_score:
             total_rank += 1
    print(total_rank)