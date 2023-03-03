# 자료구조 9회차 - Union Find / Disjoint Set

[메인으로 돌아가기](https://github.com/Maker-H/GroupStudy_Algo_Log)

## 𝐈𝐧𝐟𝐨

- 📌 발표자 : [@Maker-H](https://github.com/Maker-H)
- 🗓️ 2023-02-27

<br><br>

# Union Find / Disjoint Set 자료구조

- 집합을 표현하는 자료구조
- S라는 집합 = {1, 8, 2, -1}
- T라는 집합 = {2, 5, 4}

<br>

### 집합(set)과 관련된 연산

1. Memebership 연산

- 2가 S의 원소인가?를 물어보는 연산
- True와 False로 답할 수 있는 연산

2.합집합, 교집합, 차집합

- 합집합(Unioin)
- 교집합(Intersection)
- 차집합(Difference)

**⇒ 파이썬에서는 list를 +, - 할 수 있고 set이라는 자료구조 사용해서 집합과 관련된 연산 할 수 있다**

<br>

### 강의에서 다루는 연산

1. make_set(x) 연산
    - **O(1)**
    - x 만으로 구성된 집합을 만드는 연산
2. find(x) - Membership 연산
    - **O(logN)**
    - x가 속한 **집합의 대표값**을 반환
3. union(x, y)
    - **O(logN)**
    - x와 y가 속한 집합이 다르다면 하나의 집합으로 만들어주는 연산 

<br>

## 1. 원형 양방향 연결 리스트로 구현할 경우

1. make_set(x)
    - 노드 x를 포함한 리스트 만들어 리턴
    - 더미노드 뒤에 x만 붙이면 되기에 **O(1)**

2. find(x)
    - 리스트에서 x가 있는지 더미노드부터 뒤로 순회
    - x 발견하면 노드 x가 속한 리스트의 head 노드를 찾아 리턴 (head 노드가 집합을 대표)
    - w.c는 x가 가장 끝에 있는 경우이므로 **O(N)**
    
![image](https://user-images.githubusercontent.com/83294376/221509888-82428105-d58f-4671-bbb2-e1f9172c8246.png)

    

3. union(x, y)
    - 리스트에서 x가 있는지 더미노드부터 뒤로 순회 - **O(N)**
    - 리스트에서 y가 있는지 더미노드부터 뒤로 순회 - **O(N)**
    - x, y에 대해 find 함수를 불러 head 노드를 찾은 후, 두 노드가 서로 다르다면 (다른 집합이라면) 두 리스트를 연결하여 하나의 리스트로 만든 후(링크만 이어주면 됨), 전체의 head 노드를 리턴 - **O(1)**
    - 결론적으로 **O(N)**

<br>

## 2. 트리로 구현할 경우
- 트리의 노드는 parent만을 가리킨다
- 루트는 None이 아니라 자기 자신을 가리킨다. 그러므로 부모가 자기자신인 노드가 루트 노드이다
- 트리의 루트 노드가 집합을 대표한다
- S = {1, 3, 5, 2}고 3이 루트인 경우
- find(2) = 3, find(1) = 3
- rank는 union할 때, 두 집합에 대한 부모, 자식 관계를 결정할 때 사용함

<br>


1. **find(x)**
    - 루트 노드를 찾아 올라가는 만큼이 수행시간이 되기에 트리의 높이인 h가 수행시간이 된다 - **O(logN)**
2. **union(x, y)**
    - find(x)로 루트 찾기 - **O(logN)**
    - find(y)로 루트 찾기 - **O(logN)**
    - 각 루트가 다르다면 **높이가 더 낮은 루트가 다른 루트를 가리키게 해 하나의 트리를 만든다 (높이가 다른 트리를 결합할 경우 전체 높이가 달라지지 않는다)**

![image](https://user-images.githubusercontent.com/83294376/221509839-e7658db3-262d-4da2-bf6e-6d1226f164cd.png)

구현

```python
class DisjointSet:
    def __init__(self, key):
        self.key = key
        self.parent = self
        self.rank = 0

    # x만을 원소로 가지는 집합 만들기
    def make_set(x):
        return DisjointSet(x)

    def find(x):
        whlie x.parent != x:
            x = x.parent
        # 루트일때 while에서 빠져나온다
        return x

    def unoin(x, y):
        x1, y1 = self.find(x), self.find(y)

        # 이 if문이 존재하기에 x1의 높이는 항상 y1보다 작거나 같다
        if x1.rank > y1.rank: 
            x1, y1 = y1, x1

        x1.parent = y1

        if x1.rank = y1.rank:
            y1.rank += 1
```

![image](https://user-images.githubusercontent.com/83294376/221509758-4ffbb02b-5881-4e8a-9234-335efe8d33ce.png)

지수와 같이 표기된 숫자는 높이 이다

<br>

### 시간복잡도

- rank가 1 증가할때 노드의 개수는 2배 증가한다
- N(h) = 높이가 h인 트리의 최소 노드 개수
    - N(0) = 1
    - N(1) = 2 (노드 1개씩 있는 트리를 union)
    - N(2) = 4 (노드 2개씩 있는 트리를 union)
    - N(h) = 2N(h-1) = $2^hN(0)$ = $2^h$
- n (노드개수) ≥ N(h) > $2^h$
- logN ≥ h
- O(logN)
