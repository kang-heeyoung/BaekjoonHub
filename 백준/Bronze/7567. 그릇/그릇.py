import sys
read = sys.stdin.readline


bowl = read()

# print(bowl[3])
result = 10
under_bowl = bowl[0]

for i in range(1, len(bowl)-1):
    if under_bowl == bowl[i]:
        result += 5
    else:
        under_bowl = bowl[i]
        result += 10

print(result)