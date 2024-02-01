import sys
read = sys.stdin.readline

A, I = map(int, read().split())

# I = ? / A

print(int(A*(I-0.99)+1))