from collections import deque
import sys


T = int(sys.stdin.readline())
a = deque()


for i in range(1,T+1):
    a.append(i)


while len(a) > 1:
    a.popleft()
    b = a.popleft()
    a.append(b)


print(*a)