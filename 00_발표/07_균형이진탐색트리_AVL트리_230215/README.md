# 자료구조 7회차 - AVL 트리 (균형이진트리)

[메인으로 돌아가기](https://github.com/Maker-H/GroupStudy_Algo_Log)

## 𝐈𝐧𝐟𝐨

- 📌 발표자 : [@hjhj-kk](https://github.com/hjhj-kk)
- 📌 작성자 : [@hjhj-kk](https://github.com/hjhj-kk), [@Maker-H](https://github.com/Maker-H)
- 🗓️ 2023-02-15


<br><br>

# 균형 이진 트리

- 이진탐색트리(최대 2개의 자식 + 오른쪽은 큰거 왼쪽은 작은거)의 연산 시간은 오직 트리 높이 h에 의해 결정되는데, 문제는 최악의 경우엔 h = O(n)이 되어 탐색, 삽입, 삭제 연산이 매우 느려진다.
- 연산 속도를 빠르게 하기 위해선 트리 높이를 되도록 작게 유지하는게 중요하다
- 모든 노드가 빠짐없이 있다면 삽입, 삭제 연산을 반복하더라도 n개의 노드를 갖는 이진트리의 높이를 항상 O(log n)이 되도록 유지할 수 있다.
- 이렇게 유지할 수 있는 이진탐색트리를 균형이진탐색트리라 부른다

## 균형이진탐색트리 ( Balanced BST )

- AVL 트리
- Red-Balck 트리
- (2, 3, 4 트리)
- Splay 트리

### 

## Rotation

- **균형 이진 탐색 트리의 주요한 연산**
- 트리의 종류에 따라 Rotation의 횟수, 모양 다르게 반복 수행한다
- 트리의 일부를 회전시켜서 h = O(log n)이라는 높이 조건을 만족할 수 있도록 해주는 연산
- 트리를 회전 시켜 전체 트리 높이를 줄여준다
- 회전 후에도 BST의 값의 순서가 그대로 유지되어야 한다
- 링크 교환이 항상 6번이기에 **O(1)**



![rotation](https://user-images.githubusercontent.com/123444953/218942666-b6002231-2166-4888-b15f-0a82476f709b.jpeg)

- right rotation 전의 순서는 AxBzC이고, 회전 후의 순서
역시 AxBzC이므로 같다
- b에 유의해야 한다. b는 a의 부트리였는데 right rotation 이후에는 **a보다 크고 z보다는 작기 때문에** z의 부트리가 되었다
- 링크 교환(right rotation시)
    - z의 부모 노드와 x 간의 링크 → 1, 2
    - x와 z의 관계 → 3, 4
    - b와 z의 새로운 관계 → 5, 6

```python
def right_rotation(self,z): # z를 중심으로 오른쪽 방향으로 회전# z는 그림과 동일하게 사용

  if z == None: # 중심이 되는 노드 없음
    return 

  x = z.left
  if x == None: # 왼쪽 부트리 없음
    Return 

  # b가 자리 이동하는 특수한 노드이기에 선언
  b = x.right

#---- 회전 전의 트리 구성

  # 1번 링크 수정
  # z의 부모 노드와 x간의 링크
  x.parent = z.parent	

  # 2)z의 부모 노드와 x간의 링크
  # z.parent가 없으면 z는 루트	
  if z.parent != None:
    # z.parent 입장에서 x를 오른쪽으로 넣을지 왼쪽으로 넣을지
    if z.parent.left == x:
      z.parent.left = x
    elif z.parent.right == x:
      z.parent.right = x

  # x와 z의 관계
  x.right = z # 3번 링크
  z.parent = x # 4번 링크
  z.left = b # 5번 링크

  if b != None:
    b.parent = z # 6번 링크

  if self.root == z:
    self.root = x
```

<br>

![rotation](https://user-images.githubusercontent.com/123444953/218942666-b6002231-2166-4888-b15f-0a82476f709b.jpeg)

방법은 right rotation과 다르지 않다

``` python
# z는 그림과 동일하게 사용
def left_rotation(self, x):
  if x == None: # 중심이 되는 노드 없음
    return 

  z = x.right
  if z == None: # 오른쪽 부트리 없음
    Return 

  # b가 자리 이동하는 특수한 노드이기에 선언
  b = z.left

#---- 회전 전의 트리 구성

  # 1번 링크 수정
  # z의 부모 노드와 x간의 링크
  z.parent = x.parent	

  # 2)z의 부모 노드와 x간의 링크
  # z.parent가 없으면 z는 루트	
  if x.parent != None:
    # x.parent 입장에서 z를 오른쪽으로 넣을지 왼쪽으로 넣을지
    if x.parent.left == z:
      x.parent.left = z
    elif x.parent.right == z:
      x.parent.right = z

  # x와 z의 관계
  z.left = x # 3번 링크
  x.parent = z # 4번 링크
  x.right = b # 5번 링크
  if b != None:
    b.parent = z # 6번 링크

  if self.root == z:
    self.root = x
```

<br><br>

# AVL 트리
- 1962년에 소련의 수학자 2명이 제안
- 가장 오래된 **균형이진탐색트리**

<br>

### 정의

모든 노드에 대해서 왼쪽 부트리와 오른쪽 부트리의 **높이 차가 1 이하인** 균형이진탐색트리(최대 2개의 자식 + 왼쪽은 작은거 오른쪽은 큰거, 균형 - 모든 레벨이 꽉 차있는 트리) 

![image](https://user-images.githubusercontent.com/83294376/219269344-4a0f37b8-fde2-4f4e-a9ce-5bbbfcb3601f.png)

- J의 입장 : +1
    - 왼쪽 서브트리 높이 : 2
    - 오른쪽 서브트리 높이 : 3
- F의 입장 : -1
    - 왼쪽 서브트리 높이 : 1
    - 오른쪽 서브트리 높이 : 0
- P의 입장 : +1
    - 왼쪽 서브트리 높이 : 1
    - 오른쪽 서브트리 높이 : 2

<br>

## AVL 트리 O(logN) 증명

모든 노드에 대해서 노드의 왼쪽 부트리와 오른쪽 부트리의 높이 차이가 1 이하인 이진탐색트리

$N_k$ = 높이가 h인 AVL트리 중에서 최소 노드 개수

$N_0 = 1$, $N_1 = 2$, $N_2 = 4$, $N_3 = 7$

$N_h = N_{h-1} + N_{h-2} + 1> 2N_{h-2}+1 > 2N_{h-2}$

<br>

**N(h) = 1(root) + N(h-1) + N(h-2)**
- N(h-1) : root level을 제외한 나머지 높이
- N(h-2) : root level을 제외한 나머지 높이 중 최소 노드 개수를 만들어주기 위해 높이차 1을 지켜준 높이

<br>

**N(h-1) ≥ N(h-2) 이므로**
- N(h) ≥ 2N(h-2) + 1 ≥ **2N(h-2) = 2N(h-3) + 2N(h-4)**

<br>

**N(h-3) ≥ N(h-4) 이므로**
- N(h) ≥ 2N(h-2) ≥ 2N(h-4) + 2N(h-4) = $2^2$N(h-4)
  - h가 -2 될수록 x2 되므로 h=0까지  $2^{h/2}N(0)$ 가 된다

<br>

즉 $N_h>2N_{h-2}>2^2N_{h-4}>...>2^{h/2}N_0=2^{h/2}$

<br>

높이가 h이고 노드 개수가 n인 AVL 트리에서

$n ≥ N_h ≥ 2^{\ h/2}$ →  **logN ≥ h/2**



ABL Class : 기존의 BST를 상속하여 만든다

<br><br>

# AVL 트리의 삽입연산
Node와 BST 구현 이후 AVL 구현 시작

- BST는 insert, delete by merging, search 동일하게 사용
- AVL 트리는 **BST를 상속받은** 이진탐색트리
- AVL 트리는 **Node 클래스에** 높이 표현해주는 **height 정보** 포함되어야 한다
- AVL 트리는 **높이가 변할 수 있는 메소드의 경우** height를 고려해 **오버라이딩** 해주어야 한다

``` python 
# Node와 함께 구현하여 Node 사용
class avl_Node(object):
    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.height = 0

  #def postorder(self):
  def __iter__(self):
    if self != None:

      # 왼쪽 트리에 있는 노드들 재귀적으로 호출
      if self.left:
        self.left.postorder()

      # 오른쪽 트리에 있는 노드를 재귀적으로 호출
      if self.right:
        self.right.postorder()

      yield self.key


#BST를 상속받은 avl 트리
class AVL(BinarySearchTree):
  # __init__ 없어도 부모 생성자 자동으로 콜

  def __len__(self):
    return self.size


  def __iter__(self):
    # root이 가리키는 Node의 __iter__
    # __iter__가 postorder라면 post로 노드를 읽는다
    return self.root.__iter__()

  # heigth 포함해서 오버라이딩
  def find_location(self, key):
    # 부모노드랄게 존재하지 않다면 None 반환
    if self.size == 0:
      return None
	
    # target의 부모
    parent = None
    target = self.root

    # target이 리프 노트까지 내려가 더 내려갈 곳 없다면 None 만남
    while target != None:
      if target.key == key:
        return target

      # 찾아야 하는 key가 더 크다면
      # 이진탐색트리의 규칙에 따라 오른쪽 subtree로 찾으러 간다
      elif target.key < key:
        parent = target
        target = target.right

      # 찾아야 하는 key가 더 작다면
      # 이진탐색트리의 규칙에 따라 왼쪽 subtree로 찾으러 간다
      else:
        parent = target
        target = target.left

      # avl
      # level 0부터 시작해 아래로 내려갈때마다 +1 해준다
      target.height += 1

    return parent


  # 아래의 insert 구현에서 super 사용하기에
  # 확인차 bst의 insert 코드 가져옴
  # 오버라이딩 한 거 아님
  def insert(self, key):
    # 일치하는 key가진 노드 없다면 삽입할 자리 부모노드 받아온다
    parent_node = find_location(key)	

    # find_location의 결과가 내가 넣으려고 한 key와 다르다면
    # 노드 만들어서 삽입해야 한다는 뜻
    if parent_node == None or parent_node.key != key:
      # 노드 생성
      target_node = avl_Node(key)	

      # parent가 None이면 내가 삽입할 key가 루트에 들어가야 한다는 뜻	
      if parent_node == None:
        self.root = target_node

      # parent.key가 내가 찾는 key가 아니면 삽입될 부모 노드 받아왔다는 것		
      elif: parent_node.key != key:
      target_node.parent = parent_node

      # 부모보다 key가 작으면 왼쪽으로 넣는다
      if parent_node.key >= key:
        parent_node.left = target_node

      # 부모보다 key가 크면 오른쪽으로 넣는다
      elif parent_node.key < key: 
        parent_node.right = target_node


      self.size += 1
      return target_node

    else:
      print('key is already in tree')
      return None 
```

<br>

### insert 구현

- 삽입은 BST와 동일하게 하나 높이차가 1 이상 발생할 경우 추가적인 연산이(Rotation) 필요하다
  - 삽입된 노드 때문에 높이차 균형이 깨진 노드가(z) 존재한다면 찾아간다
  - z가 루트였다면 root 재설정 해주어야 하기 때문에 rebalance(z, y, x)한 **후의** z 위치에 온 노드를 반환해준다
- **O(logN)**
  - 노드 삽입까지 O(h) = **O(logN)**
  - z, y, x 찾기의 w.c는 start가 root의 경우이므로 O(h) = **O(logN)**
  - rotation 자체는 **O(1)**
  - 만약 z가 root라면 root 조정 **O(1)**

<br>

### **발생할 수 있는 경우의 수 2개**

**case 1**
z, y, x가 직선상에 있는 경우 **(balance_F가 계속 양수 or 음수)**

- z을 기준으로 rotation
- z의 balance_F가 +1 이상이 되면 right_rotation
- z의 balance_F가 -1 이하가 되면 left_rotation

 ![insert_case1](https://user-images.githubusercontent.com/123444953/218942944-e80e9670-2448-42b0-af86-63abf0dae3b1.png)

![image](https://user-images.githubusercontent.com/83294376/219271140-e5348337-ed63-4307-a24f-a0d585cdcdc9.png)

![image](https://user-images.githubusercontent.com/83294376/219271168-67c15689-49ce-4e7a-93e7-56db0ab4d8b2.png)

<br>

**case 2**
z, y, x가 삼각형 모양인 경우 **(balacne_F가 양수 혹은 음수로 번갈아 나올때)**

- y를 기준으로 ratation 해준 후 z을 기준으로 한 번 더 rotation해준다
- z의 balance_F가 +1 이상이면
  - y 기준 left_rotation → z 기준 right_rotation
- z의 balance_F가 -1 이하이면
  - y 기준 right_rotation → z 기준 left_rotation


![image](https://user-images.githubusercontent.com/83294376/219271279-a0f19bcd-97c1-44aa-a1b5-64ae2c9c2539.png)

![image](https://user-images.githubusercontent.com/83294376/219271307-fce80f59-8477-4482-bf5a-6f265b7256e9.png)

![image](https://user-images.githubusercontent.com/83294376/219271349-2e6fda45-6aff-4547-874b-bd2174be649b.png)

<br>

**avl_height 구현**

``` python 
# balance_factor에서 높이차 계산할 때 
# 왼쪽 자식이 존재하고 오른쪽 자식이 None이라도 1로 계산해야 하기에
# None의 높이를 0으로 간주해야 한다
def avl_heigth(self, target):
  if target == None:
    return 0
  return target.height

```

**balance_factor 구현**
높이차 계산해주는 메소드
``` python

def balance_factor(self, target):
  if target == None:
    return 0

  return self.avl_height(target.left) - self.avl_height(target.right)

```

**insert 구현**
``` python
# BST class method overwriting
def insert(self, key):

 #super에서 AVL의 객체 정보 넘겨주었기에 AVL트리객체에 key값 insert 됨
 #BST class 메소드 결과값인 삽입된 노드를 반환받음
 target = super(AVL.self).insert(key)


  # 삽입한 노드의 부모 노드의 높이가 달라질 일은 없다
  x = None
  y = target
  z = target.parent


  # 높이값이 다른 곳을 찾아 root까지 간다
  balance_F = self.balance_factor(z)
  while  -1 <= balance_F <= 1 :
    x = y
    y = z
    z = z.parent
    balance_F = self.balance_factor(z)

    # root에 도달하면
    if target.parent == None:
      break

  rebalance(z, y, x)
```

**rebalance 구현**
``` python
def rebalnce(z, y, x):

  z_bal = self.balance_fator(z)
  y_bal = self.balance_factor(y)

  # 높이차 있는 경우
  if not( -1 <= z_bal <= 1 ):

    # z, y, x가 직선상에 있는 경우
    if z_bal < -1 and y_bal < 0:
      tmp_root = self.left_rotation(z)		
    elif z_bal > 1 and y_bal > 0:
      tmp_root self.right_rotation(z)


    # z, y, x가 삼각형 모양의 경우
    elif z_bal < -1 and y_bal > 0:
      tmp_root = self.right_roatation(y)
      tmp_root = self.left_rotation(z)
    elif z_bal > 1 and y_bal < 0:
      tmp_root = self.left_roatation(y)
      tmp_root = self.right_rotation(z)	

    # 만약 회전 후 가장 높이 있는 노드가 root라면 연결해준다
    if tmp_root.parent == None:
      self.root = tmp_root

    return tmp_root
```
<br>

Pseudo code

```python
def insert(self, key):
  1. v = super(AVL, self).insert(key)
  2. find x, y, z 
  3. w = rebalance(x, y, z)
  4. if w.parent == None:
        self.root = w
```

<br><br>

# AVL 트리 삭제 연산

- deleteByMerging이나 deleteByCopying을 이용해서 삭제
- 균형을 맞추기 위해서, v가 속한 부트리의 높이를 증가시키고, 이를 위해서 y와 x를 z에서 v가 속하지 않은 부트리에 속하는 노드로 정의
  
  ![delete](https://user-images.githubusercontent.com/123444953/218943071-bb74526c-429e-4f6d-ae70-c464d56677be.png)

- z-y-x의 균형은 맞췄지만, y의 새로운 부모 노드인 w에서 균형이 깨진다.
- 삽입 연산과 다르게 더 무거운 쪽 서브트리를 기준으로 rotation 시켜야 한다. 균형을 맞추기 위해선, 삭제된 노드가 있는 부트리의 높이를 증가시켜야 하기 때문이다
- 회전 이후에는 루트노드로 올라가며 균형 깨진 부모노드 있는지 살펴야 한다. 회전을 통해 z-y-x의 균형을 맞췄지만, y의 새로운 부모 노드인 w에서 균형이 깨지게 되기 때문이다
  
  ⇒ 루트 노드까지 올라가면서 계속 같은 작업을 반복

<br>

- 시간 복잡도 : $O(logn)$
    - w.c 는 O(logN) rotation root로 올라가며 계속 rotation 해야할 수도 있기 때문 

**delete 구현**
``` python 
def delete(self, have_to_delete_node):
  # delete by copying, delete bu merging 다 상관x
  # 반환값은 target 지워서 균형이 깨질 수 있는 가장 깊은 곳에 있는 노드
  # 즉 삭제된 노드의 부모노드가 반환된다
  target_node = super(AVL.self).delete_by_copying(have_to_delete_node)

  # root까지 가보자
  while target_node != None:
    # 균형 깨지면
    if not (-1 <= balance_factor(target_node) <= 1):
      z = target_node
      if z.left.height >= z.right.height:
        y = z.left
      elif z.left.height < z.right.height:
        y = z.right

      if y.left.height >= y.right.height:
        x = y.left
      elif y.left.height < y.right.height:
        x = y.right
		
    target_node = rebalance(z, y, x)

    # rebalance한 노드의 최상단 리턴 받아서 원래 있던 노드의 부모 노드와 링크
    result_root = target_node
    if result_root.parent == None:
      self.root = result_root

    elif result_root.parent != None
      if target_node.parent.key < result.node.key:
        target_node.parent.right = result.node
      elif target_node.parent.key > result.node.key:
        target_node.parent.left = result.node			

      result_node.parent = target_node.parent
```

<br>

Pseudo code
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

<br>

AVL 트리

- 높이 O(logn)
- insert
  - 노드 삽입 : O(logn)
  - rebalance - 1회/ 2회 회전 : O(1)
- delete
  - 노드 제거 : O(logn)
  - rebalance - 매 level에서 O(logn) 회전
