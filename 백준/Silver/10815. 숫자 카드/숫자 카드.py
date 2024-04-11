import sys
read = sys.stdin.readline

N = int(read())
my_num = list(map(int, read().split()))

M = int(read())
input_num = list(map(int,read().split()))

# -10 2 3 6 10
#  -5 2 3 4 5 9 10

idx_check = 0
input_dic = {}
for i in range(M):
    input_dic[input_num[i]] = 0

for i in my_num:
    if i in input_dic.keys():
        input_dic[i] = 1
    

print(" ".join(map(str, list(input_dic.values()))))
    
