import sys
read = sys.stdin.readline

num = list(map(int, read().split()))

min = 100
max = 0
sum = 0

for i in range(3):
    if num[i] > max:
        max = num[i]
    
    if num[i] < min:
        min = num[i]
    sum += num[i]

print(sum - max - min)


    
        