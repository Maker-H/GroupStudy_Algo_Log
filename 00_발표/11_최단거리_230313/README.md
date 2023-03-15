# 자료구조 11회차 - 최단거리

## 𝐈𝐧𝐟𝐨

- 📌 발표자 : [@jongwook123](https://github.com/jongwook123)
- 🗓️ 2023-03-13

#### 최단 경로 문제(Shortest path algorithm)

- 에지에 가중치가 주어진 방향 그래프를 대상으로 한다.
  
  - 가중치는 모두 양수

- 출발노드 s 가 입력되고 , 출발 노드 s에서 다른 모든 노드까지의 최단 경로를 찾는 문제들을 다룬다.
  
  <img src="https://user-images.githubusercontent.com/122584199/224641940-56eb742c-af56-4d43-bf96-eac7537c69a8.png" title="" alt="Untitled (1)" width="299">
  
  <img src="https://user-images.githubusercontent.com/122584199/224642587-155e8420-fb93-4721-ace9-e7b2f73b1b20.png" title="" alt="Untitled (6)" width="300">

- 최단 경로의 기본 성질
  
  1. u → v : 노드 u에서 노드 v로의 하나의 에지로 구성된 경로
  
  2. s —> v : 노드 s에서 v로의 경로를 표시하고, 중간에 여러 노드가 존재 가능
  
  3. s —>u→ v 인경우, 이경로에서 u는 v의 parent이다
  
  4. 만약 s —>u→ v 가 s→v의 최단경로라면 s —>u역시 최단경로이다.
     
     <img src="https://user-images.githubusercontent.com/122584199/224642076-0512c287-070a-48a4-a359-421b009aa00f.png" title="" alt="Untitled (2)" width="259">
     
     - 기존에 최단거리를 relax를 통해 계속 업데이트 하는 방식으로 갱신한다. 모든 노드를 다 돌때 까지
       
       ![Untitled (3)](https://user-images.githubusercontent.com/122584199/224642088-c94b4575-57d8-4b26-bbf1-c9342501ab1a.png)
       
       -> 이때 dist[s] = 0 나머지 노드들은 dist[v] = ∞로 초기값을 설정한다.
       
       ![Untitled (4)](https://user-images.githubusercontent.com/122584199/224642093-4fb8997c-222c-4671-9eef-c1dccdbee80f.png)

- Bellman - Ford

```python
def relax(u,v):        # u : 출발점 v : 도착점
        if dist[v] > dist[u] + weight(u,v):
                dist[v] = dist[u] + weight(u,v)

for i in range(n):    # 모든 노드에 대해 relax로 최단거리를 업데이트 해준다.
        for each edge u -> in G:
                relax(u,v)

# n번의 반복동안 간선(E)만큼 수행한다. -> O(nE) -> E == n(n-1) == n^2 -> O(n^3)
```

- Dijkstra
  
  - Bellman - Ford는 전부를 탐색하기에 시간(O(n^3))이 오래걸린다. 가지치기 방식을 통해 조금더 빠른것이 Dijkstra 방식.
    
    <img src="https://user-images.githubusercontent.com/122584199/224642101-ef65fa89-68bc-416c-a592-4f6d5e955b1a.png" title="" alt="Untitled (5)" width="283">

```python
def relax(u,v):        # u : 출발점 v : 도착점
        if dist[v] > dist[u] + weight(u,v):
                dist[v] = dist[u] + weight(u,v)

Q = min-heap # (distance 중 가장 작은값을 매번알아야하기때문)

while Q != 0:      # n개의 노드가 다 들어가있음
        u = Q.deleteMin()
        for each u -> v: # 인접 부분 탐색
                relax(u,v)
                Q.decreasekey(v,dist[v]) # 최소값 갱신 이때 heapify-up을 사용하므로 O(logn)

# 각노드 v : Q insert delete 반복 O(nlogn)
# 각에지 : 한번의 relax -> decreasekey O(logn)
#          O(Elogn) == O(n^2logn)

# => O(n^2logn) 
# (만약 Fibonacci Heap을 쓸 경우 decreasekey가 O(1)이 되어서 O(n^2)가 된다.)
```
