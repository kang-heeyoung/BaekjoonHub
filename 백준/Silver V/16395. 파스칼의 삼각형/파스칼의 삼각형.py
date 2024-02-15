# 찾아야하는 행 : [n-1][k-1]
import sys
read = sys.stdin.readline

n, k = map(int, read().split())

tri = [[1 for col in range(n)] for _ in range(n)]

# print(tri)

for i in range(2, n):
    for j in range(1, i):
        tri[i][j] = tri[i-1][j-1]+ tri[i-1][j]

print(tri[n-1][k-1])