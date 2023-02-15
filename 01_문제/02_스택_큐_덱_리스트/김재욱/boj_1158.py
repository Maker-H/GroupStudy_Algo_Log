from collections import deque

N, K = map(int, input().split())

Q = deque([i for i in range(1, N+1)])
lst = []
while Q:
    for _ in range(K-1): # k-1번째까지 넘어가기
        Q.append(Q.popleft())

    lst.append(Q.popleft()) # k번째 뽑기

print('<'+', '.join(str(l) for l in lst)+'>')