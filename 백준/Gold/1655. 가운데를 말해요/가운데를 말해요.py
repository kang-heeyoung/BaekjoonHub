import heapq
import sys

min = []
max = []
result = []

N = int(sys.stdin.readline())

for i in range(1, N+1):
    num = int(sys.stdin.readline())
    if len(min) == len(max):
        heapq.heappush(max, -num)
    else:
        heapq.heappush(min, num)
        
    if i > 1 and -max[0] > min[0]:
        x = - heapq.heappop(max)
        y = - heapq.heappop(min)
        heapq.heappush(max, y)
        heapq.heappush(min, x)
    
    result.append(-max[0])
    
print(*result)