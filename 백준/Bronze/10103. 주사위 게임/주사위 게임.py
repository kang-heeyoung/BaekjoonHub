import sys
read = sys.stdin.readline

T = int(read())

a = 100
b = 100

for i in range(T):
    x, y = map(int, read().split())
    if x>y:
        b = b - x
    elif y>x:
        a = a-y
    else:
        pass
    
print(a)
print(b)