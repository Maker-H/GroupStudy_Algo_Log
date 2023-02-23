import sys
import heapq

N = int(sys.stdin.readline())
q = []

for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))

    if q:
        for num in arr:
            if q[0] < num:  # 더 큰 수이면
                heapq.heappushpop(q, num)  # num push 후 작은 항목 pop
                # 힙에서 가장 작은 항목 pop을 통해 q의 길이가 N임을 유지함
    else:
        for num in arr:
            heapq.heappush(q, num)

print(heapq.heappop(q))  # 힙에서 가장 작은 항목 pop해서 반환 후 출력
