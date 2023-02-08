import sys

N = int(sys.stdin.readline())
stack = []
result = []
cnt = 0
ans = 0

for _ in range(N):
    num = int(sys.stdin.readline())
    while cnt < num:
        cnt += 1
        stack.append(cnt)
        result.append('+')

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        ans = 1

if ans == 1:
    print('NO')
else:
    for i in result:
        print(i)


