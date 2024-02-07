import sys
read = sys.stdin.readline

num = int(read())

if num >=90:
    print('A')
elif num >= 80:
    print('B')
elif num>=70:
    print('C')
elif num>=60:
    print('D')
else:
    print('F')