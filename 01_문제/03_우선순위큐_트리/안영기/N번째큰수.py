# https://www.acmicpc.net/problem/2075
# 2075 [안영기] N번째 큰 수 / 힙 / 실버

import sys
import heapq

input = sys.stdin.readline

heap = []
N = int(input())

for i in range(N):
    arr = list(map(int, input().split()))
    for num in arr:
        if len(heap) < N:
            heapq.heappush(heap, num)
        else:
            # heapq 모듈은 내부의 숫자들 중 가장 작은 수가 0번째 인덱스에 오는 구조
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
print(heap[0])

