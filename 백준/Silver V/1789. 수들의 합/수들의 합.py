import sys
read = sys.stdin.readline

N = int(read())

total = 0
cnt = 0


while True:
    cnt += 1
    total += cnt
    if total > N:
        break

print(cnt-1)
        