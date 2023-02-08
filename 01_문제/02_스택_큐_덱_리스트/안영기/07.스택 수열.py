import sys
sys.stdin = open('스택 수열.txt', 'r')

N = int(input())
stack = []
cal = []
count = 1
ans = 1

for i in range(N):
    num = int(sys.stdin.readline())
    while count <= num:
        stack.append(count)
        count += 1
        cal.append('+')

    if stack[-1] == num:
        stack.pop()
        cal.append('-')
    else:
        ans = 0
        break

if ans == 0:
    print('NO')
else:
    for i in cal:
        print(i)




