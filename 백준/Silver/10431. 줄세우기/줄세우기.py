# 키가 작은 순으로 1번~20번까지 부여
# 같은 키를 가진 학생 없음

# 아무나 한 명을 뽑아 줄의 맨 앞에 세움
# 줄의 맨 뒤에 서면서 다음 과정을 거침
# 자기 앞에 자기보다 키가 큰 학생이 한명 이상 있다면 그중 가장 앞에 있는 학생의 바로 앞에 섬
# 학생들이 총 몇 번 뒤로 물러서게 될까

import sys

read = sys.stdin.readline

t = int(read())
stu = [[] for _ in range(t)]
total = [0 for _ in range(t)]

for i in range(t):
    result = []
    x = list(map(int, read().split()))
    result.append(x[1])
    x = x[2:]
    for j in x:
        for y in result:
            if y >  j:
                total[i] += 1
            else:
                break
        result.append(j)
        result.sort()
        result.reverse()

for i in range(t):
    print(f'{i+1} {total[i]}')

    
        
