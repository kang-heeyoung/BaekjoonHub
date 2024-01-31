import sys
read = sys.stdin.readline

N = int(read())
L = int(read())

graph = [[] for i in range(N+1)]

visited = [0]*(N+1)

for i in range(L):
    x, y = map(int, read().split())
    graph[x]+=[y]
    graph[y]+=[x]
    


def dfs(a):
    visited[a]= 1
    for i in graph[a]:
        if visited[i]==0:
            dfs(i)

dfs(1)

print(sum(visited)-1)