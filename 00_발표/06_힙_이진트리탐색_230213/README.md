# 트리 정리

---

# 트리(tree)

---

- **계층적 관계**를 표현하는 자료구조
- 부모, 자식 노드를 갖고 데이터를 표현한 자료구조
- 자식이 하나만 있거나 없는 경우를 연결리스트
- 자식이 최대 두 개인 트리를 **이진 트리** - 가장 많이 쓰임

### 트리의 용어

![Untitled](C:\Users\SSAFY\Desktop\Export-ad6b608b-3c7e-43c4-9777-bff555455294\트리%20정리%20c0b6e5b21dff481587276985f7f946b8\Untitled.png)

- 노드(Node) : 각각의 요소
- 엣지(Edge) : 노드를 연결하는 선, 링크라고도 부름
- **루트(root) 노드** : 최고 조상, 트리는 항상 루트에서부터 시작하고 하나만 가짐
- 리프(leaf) 노드 : 자식이 없는 노드
- 레벨 : 루트 노드가 0, 한 세대씩 내려가면서 1씩 증가
- 깊이 : 루트 - 현재 노드의 거리
- 높이 : 현재 노드 - 리프의 거리
  - **트리 높이** : 루트 노드의 높이
- 경로(path) : 두 노드 사이를 연결하는 엣지의 시퀀스
  - A &H의 경로 : A - B - D - H / 경로 길이 : 6
- **크기(size)** : 트리에 포함된 모든 노드의 개수

### 표현법

1. **리스트**

`A = [2,8,6,1,10,15,3,12,11]`

- 부모노드가 자식노드 2개씩 가지고 있다고 가정하고 리스트를 구성, 비어있는 자식 노드는 None으로 처리
1. 리스트(재귀적)

`[a, [a의 왼쪽 부트리], [a의 오른쪽 부트리]]`

- [a의 왼쪽 부트리] = `[b, [], [d, [], []]]`
- [a의 오른쪽 부트리] = `[c, [e, [], []], [f, [], []]]`

`[a, [b, [], [d, [], []]], [c, [e, [], []], [f, [], []]]`

[이진트리그리기](http://ironcreek.net/syntaxtree/)

1. 노드 class
- 부모노드와 키값, 자식노드를 직접 표현

![Untitled](C:\Users\SSAFY\Desktop\Export-ad6b608b-3c7e-43c4-9777-bff555455294\트리%20정리%20c0b6e5b21dff481587276985f7f946b8\Untitled%201.png)

# 힙(heap) 1

---

힙 성질을 만족하는 이진트

**리스트 표현법**

```python
H = [a, b, c, None, d, e, f]
#    ^  ^--^   ^----------^
#    0    1          2
```

- 부모노드, 자식노드의 위치 상수시간에 계산 가능
- None표시가 자리를 차지 → 레벨을 꽉 채워 낭비를 줄임

### heap

1. 모양성질 : 레벨을 모두 채우고 마지막 레벨은 왼쪽부터

2. heap성질 : 모든 부모노드 key값은 자식노드 key값 이상
   
   - 루트노드의 key값이 가장 큼
- 제공연산
  - `insert`
  - `find_max`
  - `delete_max`

> `insert`, `delete_max`는 연산 이후 heap상태를 유지해주는 연산 필요 - O(log n)

# 힙(heap) 2

---

`A = [2,8,6,1,10,15,3,12,11]`

![Untitled](C:\Users\SSAFY\Desktop\Export-ad6b608b-3c7e-43c4-9777-bff555455294\트리%20정리%20c0b6e5b21dff481587276985f7f946b8\Untitled%202.png)

위와같이 heap성질을 만족하지 않는 리스트를 힙 성질에 맞도록 변경하는 것을 `make_heap`, 이를 위해 `heapify_down`을 반복적으로 수행

- 리스트의 가장 오른쪽 숫자부터 순서대로 진행

→ 자식노드와 비교하여 가장 큰 값을 부모 노드자리로 이동

```python
make_heap(A):
  n = len(A)
  for k in range(n-1, -1, -1):
    #A[k] -> heap 성질 만족하는 곳으로 내려보낸다.
    heapify_down(k, n) # k = A[k], n = heap원소 개수
```

```python
heapify_down(k, n):
  # A[k], n값
  while A[k] != leaf:
    L, R = 2*k+1, 2*k+2
    m = index_max(A[k], A[L], A[R]) # 셋중에 가장 큰 인덱스
    if k != m:
      # A[K], A[m]을 swap
    else:
      break
```

### 성능

`make_heap` 은 `heapify_down` 을 n번 호출

`heapify_down` 의 최악의 입력은 root에서 최하단 leaf까지 → 높이(h)

`make_heap` O(nh)

n개의 노드를 가진 힙의 높이 h는?

- level 0 : 1
- level 1 : 2
- level 2 : 2^2
- level 3 : 2^3
- level h - 1 : 2^(h-1)
- level h : < 2^h

다 더하면 1 + 2 + 2^2 +..... + 2^(k-1) + 1 <= n

1 + 2 + 2^2 +.....+ 2^(k-1) = (2^h -1 / 2 - 1) + 1 = 2^h <= n

`h <= $log$2 n

- `heapify_down`: O(h) = O(log N)
- `make_heap`: o(nh) = O(n log N) (사실은 O(n) 시간에도 된다)

# 힙(heap) 3

---

### insert 연산

`A = [15,12,6,11,10,2,3,1,8]` 에 14를 삽입하면 heap성질 만족 X

```
          15
        /    \
      12       6
     /  \    /   \
    11   10 2      3
   / \   /
  1   8 14
```

14의 부모노드인 10과 자리를 변경, 바뀐 자리에서 부모노드인 12와 변경하면 힙 성질 만족

→ 부모노드로 가면서 자신의 자리를 찾도록 만드는 함수`heapify_up`

```python
insert(14)
  A.append(14)
  A.heapify_up(9)
  # A[k]를 root 방향으로 이동하면서 heapify를 해준다.

heapify(k):   # k = 삽입한 노드의 인덱스
  while k > 0 and A[(k -1)//2)] < A[k]: # 부모노드와 비교
    A[k], A[(k-1) //2] = A[(k-1) //2], A[k]   # 자리 변경
    k = (k - 1) // 2
```

### find_max 연산

```python
find_max:
  return A[0] # O(1)
```

힙성질을 만족하고 있으면 루트노드가 가장 큰 수

### delete_max 연산

- A[0]을 없애면서 가장 마지막 리프노드를 루프로 옮김
- `heapify_down(0, n)` 통해 재정

```python
delete_max: # O(logN)
  if len(A) == 0: return None
  key = A[0]
  A[0], A[len(A) - 1] = A[len(A) - 1], A[0]
  A.pop()
  heapify_down(0, len(A))
  return key
```

### 성능

- `heapify_up` , `insert`: O(logN)
- `find_max`: O(1)
- `delete_max`: O(logN)

힙은 정리가 되어있지 않아 모두 탐색해야 하므로, `search`함수를 지원하지 않음

# 이진트리(Binary tree)

---

이진트리의 표현법

- 리스트, Node class를 이용한 표현

```python
class Node:
  def __init__(self, key):
    self.key = key
    self.parent = self.left = self.right = None
  def __str__(self):
    return str(self.key)
```

```python
a = Node(6)
b = Node(9)
c = Node(1)
d = Node(5)
a.left = b
a.right = c
b.parent = c.parent = a
b.left = d
d.paren = b
```

```
    6
   / \
  9   1
   \
    5
```

### 이진트리 순회(traversal)

```
       F
     /   \
   B       G
  / \       \
 A   D       I
    / \     /
   C   E   H
```

1. **전위 순회(Preorder)**
- **노드 → 왼쪽 서브트리 → 오른쪽 서브트리** 순으로 순회
- F B A D C E G I H
1. **중위 순회(Inorder)**
- **왼쪽 서브트리 → 노드 → 오른쪽 서브트리** 순으로 순회
- A B C D E F G H I
1. **후위 순회(Postorder)**
- **왼쪽 서브트리 → 오른쪽 서브트리 → 노드** 순으로 순회
- A C E D B I H G F

[자료구조 트리](https://velog.io/@kimdukbae/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%8A%B8%EB%A6%AC-Tree#%ED%8A%B8%EB%A6%ACtree-%EC%88%9C%ED%9A%8C)

```python
class Node:
  def __init__(self, key):
    self.key = key
    self.parent = self.left = self.right = None

  def __str__(self):
    return str(self.key)

  def preorder(self): #현재 방문중인 노드 == self
    if self != None: # MLR
      print(self.key)
      if self.left:
        self.left.preorder()
      if self.right:
        self.right.preorder()

  def inorder(self):
    if self != None: # LMR
      if self.left:
        self.left.inorder()
      print(self.key)
      if self.right:
        self.right.inorder()

  def postorder(self):
    if self != None: # LRM
      if self.left:
        self.left.postorder()
      if self.right:
        self.right.postorder()
      print(self.key)
```

# 이진탐색트리(Binary Search Tree)

---

특정 키 값을 찾는 연산을 효율적으로 할 수 있도록 조직화한 트리

이진탐색트리의 정의

- `left node`의 key 값은 부모 노드의 key 값보다 작은 값
- `right node`의 key 값은 노드의 key 값보다 큰

```
      15
    /    \
   4      20
  /      / \
 2     17   32
        \
        19
```

- 일반적으로 리스트의 검색은 O(N), 이진 탐색 트리는 O(log N)
- 리스트보다 이진 탐색 트리의 검색이 훨씬 효율적

### 탐색

`find_loc()`

```python
def find_loc(self, key):
  if self.size == 0: return None
  p = None # p is parent of v
  v = self.root

  while v != None:
    if v.key == key: return v
# v보다 크면 오른쪽 서브트리
    elif v.key < key:
      p = v
      v = v.right
# v보다 작으면 왼쪽 서브트리
    else:
      p = v
      v = v.left
  retern p
```

`search()`

```python
def search(self, key):
  v = self.find_loc(key)
  if v == None:
    return None
  else:
    return v
```

### 삽입

`insert` : O(log n)

```python
def insert(self, key):
  p = self.find_loc(key) # find_loc() 은 O(h)

  if p == None or p.key != key:
    v = Node(key)
    if p == None:
      self.root = v
    else:
      v.parent = p

      if p.key >= key: # left/right
        p.left = v
      else:
        p.right = v
    self.size = self.size + 1
    return v

  else:
    print("key is already in the tree")
    return p # 중복 key를 허용하지 않으면 None 리턴 p == None
```

# 이진탐색트리 연산

---

- deleteByMerging
- deleteByCopying

### **deleteByMerging**

x노드를 지울 때, x 자리에 L을 두고, L의 가장 큰 노드의 자식 노드로 R을 연결

![Untitled](C:\Users\SSAFY\Desktop\Export-ad6b608b-3c7e-43c4-9777-bff555455294\트리%20정리%20c0b6e5b21dff481587276985f7f946b8\Untitled%203.png)

<img title="" src="file:///C:/Users/SSAFY/Desktop/Export-ad6b608b-3c7e-43c4-9777-bff555455294/트리%20정리%20c0b6e5b21dff481587276985f7f946b8/Untitled%204.png" alt="Untitled" width="246" data-align="inline">

경우들

1. 왼쪽 자식노드가 없는 경우 : R로 x 대체
2. x가 루트인 경우 : 루트 노드를 업데이트

```python
deleteByMerging(self, x): # 노드 x 를 삭제
  a = x.left, b = x.right
  pt = x.parent
  # c == x를 대체할 노드
  # m == L에서 가장 큰 노드

# 왼쪽 노드 a가 x를 대체
  if a != None:
    c = a
    m = a

# 왼쪽 노드에서 가장 큰 수
# 오른쪽 노드가 큰 수 이므로 오른쪽끝까지 내려감
    while m.right:
      m = m.right    

# R은 L의 가장 큰 수에 연결
    if b != None:
      b.parent = m
      m.right = b
  else: # a == None (경우1)
    c = b

# 경우 2 : 
  if pt != None:
    if c: c.parent = pt
    if pt.key < c.key:
      pt.right = c
    else:
      pt.left = c

  else:  # pt == None (root == x)
    self.root = c
    if c: c.parent = None
  self.size -= 1
  # return은 다음에 다시 설명하기로 함
```

### deleteByCopying

x 노드를 지울 때, x를 지우는 게 아니라 값을 복사하는 방식으로 변경. L에서 가장 큰 값(m)을 찾아서 x에 복사. 원래 m의 자리에는 m의 왼쪽 서브트리가 들어감

```python
deleteByMerging(self, x): # 노드 x 를 삭제
  a = x.left, b = x.right
  pt = x.parent
  # c == x를 대체할 노드
  # m == L에서 가장 큰 노드

# 왼쪽 노드 a가 x를 대체
  if a != None:
    m = a
# 왼쪽 노드에서 가장 큰 수
# 오른쪽 노드가 큰 수 이므로 오른쪽끝까지 내려감
    while m.right:
      m = m.right   
        c = m
        m.parent = pt

# R은 L의 가장 큰 수에 연결
    if m.left != None:
            a.right = m.left
      m.left.parent = a

  else: # a == None (경우1)
    m = b
        while m.left:
      m = m.left
        c = m
```

### 삭제 연산의 수행 시간

- deleteByMerging: O(h)
- deleteByCopying: O(h)

두 함수 모두 m을 찾는데 드는 수행시간이 대부분을 차지

- insert
- search(find_loc)
- delete(merging, copying)

위 함수 모두 O(h) 시간이 든다.

```python
# case 1
insert(1)
insert(2)
insert(3)
insert(4)

# case 2
insert(2)
insert(1)
insert(3)
insert(4)
```

- 같은 키 값을 저장해도 height의 크기가 다를 수 있음
- 이진탐색트리에서 높이는 수행시간을 결정

어떤 순서로 키값이 삽입되는지와 상관없이 가능하면 작게 유지 → 균형이진탐색트리(balanced binary…)