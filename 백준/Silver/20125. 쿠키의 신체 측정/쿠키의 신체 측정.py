'''
한 변의 길이가 N인 정사각형 
(x,y)

머리, 심장, 허리, 좌우 팔 다리
머리는 심장 바로 윗칸에 1칸
왼쪽 팔은 심장 바로 왼쪽
오른쪽 팔은 심장 바로 오른쪽
허리는 심장 바로 아래쪽
왼쪽 다리는 허리의 왼쪽 아래
오른쪽 다리는 허리의 오른쪽 아래

- 신체 부위는 끊김, 굽힘 x
- 허리, 팔, 다리 길이는 1 이상
- 너비 무조건 1
- 심장의 위치와 팔, 다리, 허리의 길이 구하기

input
N(한 변의 길이) 
N*N 
*는 쿠키의 신체, _는 쿠키의 신체가 없는 칸

output
심장이 위치한 x,y
왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리의 길이

풀이
머리 : 가장 처음 들어오는 * 값
심장 : 머리 좌표에서 (0,1) 위치
왼쪽 팔 : 머리 좌표의 다음 y행에서 제일 처음 *부터 심장 전까지
오른쪽 팔 : 심장에서 마지막 * 좌표 까지
허리 : 심장 좌표에서 (0,1) 위치에서부터 *이 발견되지 않는 y행 까지
왼쪽 다리 : 허리 좌표의 (0,1) 위치부터 *좌표까지
오른쪽 다리 : 허리 좌표의 (0,1) 위치부터 * 좌표까지

'''

import sys
read = sys.stdin.readline
head = [] # 머리 기준 (i, j)
heart = []
arm = 0
left_arm = 0
right_arm = 0
back = 0
back_coor = []
left_leg = 0
right_leg = 0

check = -1


n = int(read())
arr = [[] for _ in range(n)]

for i in range(n):
    arr[i] = list(read().strip())
    
# 머리 체크
for i in range(n):
    for j in range(n):
        if check == -1 and arr[i][j] == '*':
            head = [i,j]
            check +=1
            break

# 심장 체크
heart = [head[0]+1, head[1]]

# arm 체크
for i in range(n):
    if arr[heart[0]][i] == '*' and i < heart[1]:
        left_arm += 1
    elif arr[heart[0]][i] == '*' and i>heart[1]:
        right_arm +=1
       

# 허리 체크
for i in range(head[0]+2, n):
    if arr[i][head[1]] == '*':
        back += 1
        if arr[i+1][head[1]] != '*':
            back_coor = [i, head[1]]

# 다리 체크
for i in range(back_coor[0]+1, n):
    if arr[i][back_coor[1]-1] == '*':
        left_leg +=1
    if arr[i][back_coor[1]+1] == '*':
        right_leg += 1


print(heart[0]+1, heart[1]+1)
print(left_arm, right_arm, back, left_leg, right_leg)
        
