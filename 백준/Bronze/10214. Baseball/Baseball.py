import sys
read = sys.stdin.readline

T = int(read())

for i in range(T):
    y_result = 0
    k_result = 0
    for j in range(9):
        y, k = map(int, read().split())
        y_result += y
        k_result += k
    
    if y_result > k_result:
        print("Yonsei")
    elif y_result < k_result:
        print("Korea")
    else:
        print("Draw") 
        
    