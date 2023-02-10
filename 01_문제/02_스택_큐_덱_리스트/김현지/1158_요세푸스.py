from collections import deque

N, K = map(int,input().split())
deq = deque()
for n in range(1, N + 1):
    deq.append(n)

nk_list = []
while True:
    deq.rotate(-K+1)
    nk_list.append(deq.popleft())
    if len(deq) == 0:
        break

print('<' + ', '.join(list(map(str, nk_list))) + '>')
