from collections import deque

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    que = deque(list(map(int, input().split())))
    idx = deque(list(range(N)))
    cnt = 0

    while que:
        mq = 0
        for q in que:
            if q > mq:
                mq = q

        if que[0] == mq:
            que.popleft()
            # idx_pop = idx.popleft()
            cnt += 1
            if idx.popleft() == M:
                print(cnt)
        else:
            que.append(que.popleft())
            idx.append(idx.popleft())


