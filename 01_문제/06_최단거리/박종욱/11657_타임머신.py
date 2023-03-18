import sys

INF = int(1e9)    
def bell(K):
    dist[K] = 0   # 시작점 0

    for i in range(1,N+1):      # 모든 노드에 대해
        for j in range(M):      # 모든 간선확인
            now, nxt, weight = arr[j][0],arr[j][1],arr[j][2]
            if dist[now] != INF and dist[nxt] > dist[now] + weight:   # 최단거리 업데이트
                dist[nxt] = dist[now] + weight

                if i == N:          #음수순환이 존재하면
                    return True
    return False


N,M = map(int,sys.stdin.readline().split())
arr = []

dist = [INF]*(N+1)    # 모든 값을 무한으로 설정
for _ in range(M):
    A,B,C = map(int,sys.stdin.readline().split())
    arr.append((A,B,C))                       # 매핑


nc = bell(1)

if nc:        # 음수순환이 존재하면
    print(-1)
else:
    for i in range(2,N+1):
        if dist[i] != INF:      # INF가 아닐때
            print(dist[i])      # 최단경로 출력
        else:
            print(-1)