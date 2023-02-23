# https://www.acmicpc.net/problem/11279
# 11279 [안영기] 힙 / 최대 힙 / 실버

import sys
import heapq

N = int(input())
heap = []
for i in range(N):
  n = int(sys.stdin.readline())
  if n == 0:            # n이 0일때 가장 큰 수 출력
    if not heap:        # 비어있는 경우 0 출력
      print(0)
    else:
      print((-1) * heapq.heappop(heap))   # 최대힙은 최소힙에 활용되는 pop, push에 -1을 곱해주면 됨
  else:
    heapq.heappush(heap, (-1) * n)



# import sys
# import heapq
#
# N = int(input())
# heap = []
# for i in range(N):
#   n = int(sys.stdin.readline())
#   if n == 0:            # n이 0일때 가장 큰 수 출력
#     if not heap:        # 비어있는 경우 0 출력
#       print(0)
#     else:
#       print((-1) * heapq.heappop(heap))
#   else:
#     heapq.heappush(heap, (-1) * n)

