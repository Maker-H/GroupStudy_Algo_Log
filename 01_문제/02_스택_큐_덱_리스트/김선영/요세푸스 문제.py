from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque()

for person in range(1, n+1):
    q.append(person)                 # 사람 넣기

ans = []
while q:
    for _ in range(k-1):         # K-1번째까지 빼서 뒤에 넣음
        q.append(q.popleft())
    ans.append(str(q.popleft()))            # K번째는 없앰
ans_format = ', '.join(ans)
print(f'<{ans_format}>')

