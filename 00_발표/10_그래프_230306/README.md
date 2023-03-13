# 자료구조 10회차 - 그래프

## 𝐈𝐧𝐟𝐨

- 📌 발표자 :  [@jaewook718](https://github.com/jaewook718)
- 🗓️ 2023-03-06

### QnA

<br><br>

# Graph

- 두 노드 사이의 관계가 있는 경우 에지로 연결하여 표현하고 추상적이고 일반적인 자료구조

- 그래프 G = (V, E)
  
  ![image](https://user-images.githubusercontent.com/102957590/223635456-edefcfc2-24fe-4f06-a449-5182eea520a0.png)
  
  - V = 노드(node) 또는 정점(vertex) 집합
  - E = 두 노드 쌍으로 정의

- 기본용어
  
  정점(vertex), 노드(node)
  
  - 에지(edge), 링크(link)
  - 분지수(degree)
  - 사이클(cycle) : 4→5→1→2→3→4

- 표현 방법
  
  - 인접행렬(adjacency matrix) : 인접성을 행렬로 표현
  
  ![image](https://user-images.githubusercontent.com/102957590/223635255-1f4bba06-2b40-47b4-b292-7e635579f65a.png)
  
  - 인접리스트(adjacency list) : 각 정점에 인접한 에지만을 연결리스트로 표현
  
  ![image](https://user-images.githubusercontent.com/102957590/223635306-ee16e2cd-c8bc-4bc7-88c4-6179b5f2d510.png)

| 기본연산               | 인접행렬                         | 인접리스트                                      |
| ------------------ | ---------------------------- | ------------------------------------------ |
| 메모리                | O(n^2)                       | O(n+m)                                     |
| (u,v) \in E        | G[u][v] == 1 : O(1)          | G[u].search(v) : O(n)                      |
| u에 인접한 모든 노드 v에 대해 | for v in range(1, n+1): O(n) | for each edge in G[u]:      O(인접 노드 수)     |
| 새 에지 (u,v) 삽입      | G[u][v] = 1:  O(1)           | G[u].append(v): O(1)                       |
| (u, v) 삭제          | G[u][v] = 0 : O(1)           | X = G[u].search(v)<br>G[u].remove(x): O(n) |

## Traversal : DFS, BFS

### DFS(깊이 우선 방문)

```python
def RecursiveDFS(v):
        mark v as visited node
        for each edge (v, w):
                if w is unmarked:
                        RecursiveDFS(w)

def IterativeDFS(s):
        stack.push(s)
        while stack is not empty:
                v = stack.pop()
                if v is unmarked:
                        mark v as visited node
                        for each edge (v, w):
                                if w is unmarked
                                        stack.push(w)
```

- 첫 방문 시간과 최종 방문 시간 기록하기 + 방문 순서 기록하기

```python
def DFS(v) :
        mark[v] = 1
        pre[v] = curr_time
        curr_time += 1
        for each edge(v,w): # v의 인접한 모든 노드 w에 대해서
                if mark[w] != 1:
                        parent[w] = v
                        DFS(w)
        post[v] = curr_time
        curr_time += 1
```

### DFS tree

![image](https://user-images.githubusercontent.com/102957590/223635358-bfa986fa-2e22-4344-b7ce-034de4392e91.png)

![image](https://user-images.githubusercontent.com/102957590/223634896-5d8203bc-206d-4bfd-910b-6d9810d06963.png)

### DAG : 사이클이 없는 방향 그래프

- topological Sorting(위상 정렬) : A→C→B→F→H→D→I→G

### BFS(너비 우선 탐색)

```python
def BFS(v):
        q = queue()
        q.append(v)
        mark[v] = 1
        while q:
                x = q.popleft()
                for each edge(x,w): 
                        if mark[w] != 1:
                                mark[w] = 1
                                q.append(w)
```
