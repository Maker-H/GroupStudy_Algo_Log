import sys
import heapq
T = int(sys.stdin.readline())
arr = []

for tc in range(T):

    N = int(sys.stdin.readline())

    heapq.heappush(arr,-N)                  # heappop은 최소값을 빼내기 때문에 -로 변환하여 push

    if N == 0:
        print(abs(heapq.heappop(arr)))      # heappop으로 최소값을 빼낸후 절대값으로 양수로 변환
