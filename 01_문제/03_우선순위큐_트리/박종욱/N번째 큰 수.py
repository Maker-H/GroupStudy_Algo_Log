import heapq
import sys
T = int(sys.stdin.readline())

S = []                  # 푸시해줄 리스트 생성

for _ in range(T):
    arr = map(int,input().split())  

    for ar in arr:
        if len(S) < T:      # 리스트의 길이 제한 (원하는 T번째의 숫자뽑기)
            heapq.heappush(S,ar)    
        else:
            if S[0] < ar:
                heapq.heappop(S)            # 제일 최소값 제거
                heapq.heappush(S,ar)        # 다시 추가



print(S[0]) # 연산이 끝나면 가장 앞의값이 5번째로 작은값