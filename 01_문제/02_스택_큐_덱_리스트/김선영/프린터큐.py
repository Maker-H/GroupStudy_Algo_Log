from collections import deque

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))

    target = deque()      # target의 idx를 추적하기 위한 덱
    for _ in range(n):
        target.append(0)
    target[m] = 'target'

    result = []
    while q:
        if q[0] != max(q):                      # 첫 문서가 제일 중요한 문서가 아닐 때
            q.append(q.popleft())
            target.append(target.popleft())
        else:                                   # 첫 문서가 제일 중요한 문서일 때
            q.popleft()
            result.append(target.popleft())     # 제거된 문서 result에 담기

    print(result.index('target')+1)