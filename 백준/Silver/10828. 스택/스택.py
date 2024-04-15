import sys
read = sys.stdin.readline

my_stack = []
top = 0

T = int(read())

for i in range(T):
    cmd= read().rstrip().split()
    if cmd[0] == 'push':
        num = cmd[1]
    cmd = cmd[0]    
    
    if cmd == 'push':
        my_stack.append(int(num))
        top +=1
    elif cmd == 'pop':
        if top == 0:
            print(-1)
        else:  
            print(my_stack[top-1])
            del my_stack[top-1]
            top -=1
    elif cmd == 'top':
        if top == 0:
            print(-1)
        else:
            print(my_stack[top-1])
    elif cmd == 'size':
        print(top)
    elif cmd == 'empty':
        if top == 0:
            print(1)
        else:
            print(0)