# check_num : input_num
# result_num : 만들어진 num
# count : 결과값

import sys
read = sys.stdin.readline

N = int(read())
count = 0
check_num = N

while True:
    x = N // 10
    y = N % 10
    result_num = x+y
    count += 1
    N = y*10 + (result_num % 10)
    if check_num == N:
        print(count)
        break
        
        