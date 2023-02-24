import heapq
import sys

heap = []
N = int(sys.stdin.readline())
for _ in range(N):
    n = int(sys.stdin.readline())

    if n > 0:
        heapq.heappush(heap, -n)  # 값을 음수로 push
    elif n == 0:
        if not heap: # 비어있을 경우
            print(0)
        else:
            print(-heapq.heappop(heap))  # 최소를 다시 양수로 바꿔 최대로 만들어 출력