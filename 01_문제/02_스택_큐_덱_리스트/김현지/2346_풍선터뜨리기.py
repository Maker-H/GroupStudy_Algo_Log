'''
5
3 2 1 -3 -1
'''

from collections import deque

N = int(input())
deq = deque(enumerate(map(int, input().split()), start=1))

for _ in range(N):
    d = deq.popleft()
    print(d[0], end=' ')
    if d[1] > 0:
        deq.rotate(-d[1] + 1)
    else:
        deq.rotate(-d[1])
