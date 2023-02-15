# 균형 이진 트리

## 균형이진탐색트리 ( Balanced BST )

- AVL 트리
- Red-Balck 트리
- (2, 3, 4 트리)
- Splay 트리

### 

### rotation

트리를 회전 시켜 전체 트리 높이를 줄여줌
![rotation](https://user-images.githubusercontent.com/123444953/218942666-b6002231-2166-4888-b15f-0a82476f709b.jpeg)

```python
def rotateRight(self,z): # z를 중심으로 오른쪽 방향으로 회전
    if not z: return
    x = z.left
    if x = None: return # z의 왼쪽 트리가 아무것도 없을 때
    b = x.right
    x.parent = z.parent # 1번 링크 수정
    if z.parent: # 2 번 링크 수정
        if z.parent.left == z:
            z.parent.left = x
        else:
            z.parent.right = x
    x.right = z # 3번 링크 
    z.parent = x # 4번 링크
    z.left = b # 5번 링크
    if b:
        b.parent = z # 6번 링크

    if self.root == z: 
        self.root = x
```

```python
def rotateLeft(self, x): # x를 중심으로 왼쪽 방향으로 회전
    if not x: return
    z = x.right
    if z == None: return
    b = z.left
    z.parent = x.parent
    if x.parent:
        if x.parent.left = x:
            x.parent.left = z
        else:
            x.parent.right = z
    z.left = x
    x.parent = z
    x.right = b
    if b:
        b.parent = x

    if self.root == x:
        self.root = z
```

## AVL 트리

모든 노드에 대해서 노드의 왼쪽 부트리와 오른쪽 부트리의 높이 차이가 1 이하인 이진탐색트리

$N_k$ = 높이가 h인 AVL트리 중에서 최소 노드 개수

$N_0 = 1, N_1 = 2, N_2 = 4, N_3 = 7$

$N_h = N_{h-1} + N_{h-2} + 1> 2N_{h-2}+1 > 2N_{h-2}$

$N_h>2N_{h-2}>2^2N_{h-4}>...>2^{h/2}N_0=2^{h/2}$

높이가 h이고 노드 개수가 n인 AVL 트리에서

$n = N_h > 2^{\ h/2} → h < 2logn$

$log(n+1) ≤ h < clogn + b$

ABL Class : 기존의 BST를 상속하여 만든다

### 

### 삽입 : Insert(key)

- v = super(AVL, self).insert(key)

- v로 인해 v의 조상노드의 균형이 깨질 수 있음 → rebalancing
  
  - balanceFactor = -2 또는 2인 조상 노드 조정
  
  - case 1
    
     ![insert_case1](https://user-images.githubusercontent.com/123444953/218942944-e80e9670-2448-42b0-af86-63abf0dae3b1.png)
  
  - case 2
    
    ![insert_case2](https://user-images.githubusercontent.com/123444953/218943008-9d28a8b0-6393-4428-b438-a29a29f010d8.png)

- pseudo code

```python
def insert(self, key):
        1. v = super(AVL, self).insert(key)
        2. find x, y, z 
        3. w = rebalance(x, y, z)
        4. if w.parent == None:
                        self.root = w
```

### 

### 삭제 : delete(u)

- deleteByMerging이나 deleteByCopying을 이용해서 삭제

- u라는 노드를 제거해서 balance가 깨질수 있는 가장 깊은 곳에 있는 노드를 return

- 균형을 맞추기 위해서, v가 속한 부트리의 높이를 증가시키고, 이를 위해서 y와 x를 z에서 v가 속하지 않은 부트리에 속하는 노드로 정의
  
  ![delete](https://user-images.githubusercontent.com/123444953/218943071-bb74526c-429e-4f6d-ae70-c464d56677be.png)

- z-y-x의 균형은 맞췄지만, y의 새로운 부모 노드인 w에서 균형이 깨진다.
  
  ⇒ 루트 노드까지 올라가면서 계속 같은 작업을 반복

- 시간 복잡도 : $O(logn)$

- Pseudo code

```python
def delete(self, u):
        v = super(AVL,self).deleteByCopying(u)
        while v != None:
                update v.height
                if v is not balanced:
                        z = v
                        if z.left.height >= z.right.height:
                                y = z.left
                        else:
                                y = z.right
                        if y.left.height >= y.right.height:
                                x = y.left
                        else:
                                x = y.right
                        v = rebalance(x, y, z)
                    w = v
                    v = v.parent
            # v == None
            # w == root
            self.root = w
```

AVL 트리

- 높이 O(logn)
- insert
  - 노드 삽입 : O(logn)
  - rebalance - 1회/ 2회 회전 : O(1)
- delete
  - 노드 제거 : O(logn)
  - rebalance - 매 level에서 O(logn) 회전
