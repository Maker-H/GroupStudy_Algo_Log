# 자료구조 8회차 - Red-Black Tree, 2-3-4 Tree

[메인으로 돌아가기](https://github.com/Maker-H/GroupStudy_Algo_Log)

## 𝐈𝐧𝐟𝐨

- 📌 발표자 : [@Maker-H](https://github.com/Maker-H)
- 🗓️ 2023-02-17

<br><br>

# Red Black Tree

- 균형이진탐색트리의 일종
- 모든 노드는 빨간색 혹은 검은색이다
- 루트 노드는 검은색이다
- 모든 리프노드는(NIL) 검은색이다
    - NIL : null leaf
- 빨간색 노드는 검은색 자식을 갖는다
    - No Double Red
- 모든 리프노드에서 Black Depth는 같다
    - 리프노드에서 루트노드까지 가는 경로에서 만나는 검은색 노드의 개수가 같다

![image](https://user-images.githubusercontent.com/83294376/219554561-ba338a8a-c04f-4b77-b817-06b0a9ca59a1.png)


- **h(v)** : v의 높이 (또는v의서브트리높이)
- **bh(v)** : v에서 v의 서브트리의 리프노드까지의 경로에 포함된 black 노드 갯수 (black-height)
    - 주의 : **v가 black이면 v는 bh(v)에 포함하지 않는다고 가정**

<br>

# Red Black Tree 높이의 시간복잡도

### 사실 1. **v의 내부노드의 최소 개수 ≥ $2^{bh(v)}-1$**

증명 : h(v)에 대한 귀납법

- base case
    - h(v) 가 가장 작을 때 - 0 (내부 노드가 없는 경우)
    - bh(v)가 가장 작을 때 - 0 ( 내부 노드가 없으므로 자식도 당연히 없다)
    - 0 ≥  **$2^{0}-1$ (성립)**
- hypothesis
    - k**의 내부노드의 최소 개수 h(k) ≥ $2^{bh(k)}-1$ 라고 가정해보자**
    - 최소 개수는 level당 하나의 노드만 있는 경우이다
- Induction
    - **h(v) = k+1 일때 가정 성립하는지 확인**
    - h(v) = k+1 이라면 v의 왼쪽 자식은 h(왼)=k
    - 가정을 차용한다면 h(왼) ≥ $2^{bh(왼)}-1$
    - v 내부노드의 최소 개수 = 왼쪽 subtree + 오른쪽 subtree + 자신
        - **v 내부노드의 최소 개수** ≥  $2^{bh(왼)}-1$ +   $2^{bh(오)}-1$ + 1(v자신)
    - bh(v자식) = bh(v) or bh(v) - 1
        - v가 red인 경우 v자식이 black인 경우 : bh(v자식) = bh(v) - 1
        - v가 red인 경우 v 자식이 red인 경우 : bh(v자식) = bh(v) - 1
        - 즉 bh(v자식) ≥ bh(v) - 1
    - v 내부노드의 최소 개수 ≥ $2*(2^{bh(v)}-1)+1 = 2^{bh(v)}-1$
    

### 사실 2) bh(root) ≥ h/2

- red의 자식은 무조건 black이고 black 아래에는 black이 올 수 있기 때문
- root와 리프는 무조건 black이다

<img width="245" alt="image" src= 'https://user-images.githubusercontent.com/83294376/219554779-6551155b-0f54-46ce-9cb6-4da4698d3da4.png'>


<br>

### 결론 h = O(logN)

root의 subtree 내부노드 개수 

= 전체 red-black tree의 노드개수 ≥ $2^{bh(root)}-1$

= n ≥ 전체 red-black tree의 노드개수 ≥ $2^{h/2}-1$

= n ≥ $2^{h/2}-1$

= n+1 ≥ $2^{h/2}$

= $log^{n+1}$ ≥ h/2

= 2$*log^{n+1}$ ≥ h

결론 : h = O(logN)

<br>

**시간복잡도에서 알 수 있는 사실들**

- red 노드의 자식은 무조건 black 노드
- 그래서 black 노드는 최소 높이의 반 이상 존재한다
- 어떤 노드부터 리프노드까지의 Black 노드 개수가 일정하게 유지된다
- 위의 명제가 Black 노드의 균형을 맞춰준다

**그러므로 트리의 균형이 맞춰진다**

<br>
<br>

# Red-Black Tree의 삽입 연산

- BST의 하위 클래스기에 deletebyMerging deleteByCopying 연산 그대로 사용한다
- BST의 Insert 연산을 사용해 새로운 노드를 삽입한다
- 새로운 노드의 기본색은  빨간색이다
- 삽입시 빨간색 노드가 연속으로 2번 나타나는 Double Red가 발생할 수 있기에 **2가지 방법**을 사용한다
    - 삼촌 노드가 **검은색**이라면 -> **Restructuring**
    - 삼촌 노드가 **빨간색**이라면 -> **Recoloring**
    - 새로 삽입할 노드를 **N**(New), 부모 노드를 **P**(Parent), 조상 노드를 **G**(Grand Parent), 삼촌 노드를 **U**(Uncle)라고 하자. 즉, 삼촌 노드는 말 그대로 부모의 형제라고 생각하면 된다.

<br>

## Restructuring

1. New Node, Parend Node, Grand Parend Node를 오름차순으로 정렬한다
2. 셋 중 중간값을 부모로 만들고 나머지 둘을 자식으로 만든다
3. 새로 부모가 된 노드를 검은색으로 만들고 나머지 자식은 빨간색으로 만든다

<br>

### 경우 1 - G, P, N이 삼각형 모양을 이룰 경우

![image](https://user-images.githubusercontent.com/83294376/219555083-4c6c8a21-7a28-45de-8663-985c63855845.png)

- 삽입된 N은 기본색인 빨간색
- **U가 검은색이기에 Restructuring 선택**

![image](https://user-images.githubusercontent.com/83294376/219555142-3983c8da-905e-4b74-82b2-ffe89953eca3.png)

- 중간값인 3(N)을 부모노드로 **선택 후 그에 맞게 회전**
- **주의 : 이때 값이 2인 노드는 NIL인 리프 노드를 2개 가지고 있고 그 NIL을 검은색으로 만듬으로써 조건을 만족시킨다**

**정확한 회전 방법**

- G, P, N(=x) 가 삼각형을 이루고 있고 U가 까만색이기에 Reconstucting
- N이 중간값이기에 최상단으로 올려주어야 한다
- 그에 맞게 P의 기준에서 left_roration
- 다시 N의 기준에서 right_rotation

<br>

### 경우 2. G, P, N이 일직선상에 있는 경우

<img width="345" alt="image" src= 'https://user-images.githubusercontent.com/83294376/219558985-856f5a7d-23ce-4610-b2db-5ef5bb97dd61.png'>


- 위의 사진에서 삽입된 N은 기본색인 빨간색
- **U가 검은색이기에 Restructuring 선택**
- P가 중간값이기에 P을 최상단으로 올려주어야 한다
    
![image](https://user-images.githubusercontent.com/83294376/219555262-03548f4a-d6fb-4430-98fc-d593c1ee8b77.png)
    
- 그에 맞게 회전 후 root의 경우 색을 변경해준다

<br>

## Recoloring

- Parent Node, Uncle Node을 검은색으로 바꾸고 Grand Parent Node를 빨간색으로 바꾼다
    - Grand Parnet이 root 라면 검은색으로 바꾼다
    - Grand Parent를 빨간색으로 바꿨을 때 또 다시 Double Red가 발생한다면 Restructing 혹은 Recoloring을 문제가 발생하지 않을 때까지 반복한다
    
<img width="445" alt="image" src= 'https://user-images.githubusercontent.com/83294376/219555327-128fdc24-64b6-4016-ad87-d36f5ceb7cb1.png'>

- 삽입된 N은 기본색인 빨간색
- U가 검은색이기에 Recoloring 선택
- G를 빨간색으로 바꾸고 P와 U를 검은색으로 바꾼다
- **하지만 G가 root이므로 G를 검은색으로 다시 바꾼다**

**문제!**

Grand Parent Node가 root가 아니면서 Grand Grand Parent Node와 Double Red가 되는 경우

<img width="445" alt="image" src= 'https://user-images.githubusercontent.com/83294376/219555378-cf8258d5-7f71-4fcf-8358-d2d37ad843c7.png'>


- N을 기준으로 U가 빨간색이기에 Recoloring을 진행
- G를 빨간색 P, U를 까만색으로 만들었지만 G의 부모와 Double Red 발생
- G를 기준으로 다시 Recoloring 진행
- **G를 N으로 만들어서 다시 판별**
- U가 빨간색이기에 Recoloring 진행
- G를 빨간색 P, U를 검은색으로 만든다
- G가 root이기에 검은색으로 만든다

<br><br>

## Red Black Tree 삭제연산
* 추후 업로드 예정

<br><br>

각 트리의 연산에 따른 회전 수

| Operations | AVL | Red-Black |
| --- | --- | --- |
| search O(logN) | - | - |
| insert O(logN) | 2 | 2 |
| delete O(logN) | w.c O(logN) | 3 |

시간은 같지만 회전수가 작다는게 Red Black Tree의 장점이다

<br><br>

# 2-3-4 트리

- 이진트리가 아닌 트리
- 자식 노드 개수 = 2, 3, 4
- **모든 리프노드가 같은 level에 존재**
- 꽉 차 있는 노드를 4-노드 라고 한다
    - ex) [a, b, c]
    - [a보다 작은 노드], [a와 b 사이의 노드], [b와 c 사이의 노드], [c 이상의 노드] 를 자식으로 가지기에 4-노드라고 한다
- 높이(h) : O($log_4^N$) ≤ h ≤ O($log_2^N$)
    - 자식의 개수 고려
    - 균형이진트리의 경우 $2^n$ 이어서 $log_2^N$ 계산해줬지만 2-3-4 트리의 경우 자식의 수를 생각하면 $2^n$, $3^n$, $4^n$ 일 수 있기에 log의 밑이 2와 4가 된다(3은 중간값이므로 무시한다)
    - 하지만 빅오는 log의 밑을 고려하지 않기에 O(logN)이라고 할 수 있다

<br><br>

# 2-3-4 트리의 삽입 연산

### split 하지 않아도 되는 경우

<img width="445" alt="image" src= 'https://user-images.githubusercontent.com/83294376/219555532-3b0f1ef7-8e8b-4448-b836-7b159c5c967e.png'>

- 삽입된 값은 항상 리프노드로 들어간다
- 삽입될 리프 노드까지 내려오면서 만나는 노드 중에 4-노드가 없다
따라서 split할 필요가 없다
- 리프노드[35, , ]도 4-노드가 아니어서 36을 저장할 여유있기에 [35, 36, ]의 형태로 저장된다

<br>

### split 해야하는 경우

![image](https://user-images.githubusercontent.com/83294376/219555629-7fc5dcae-1b85-413b-89cb-27eab3e7c82a.png)

- 4-노드[48, 60, 82]에 도착하면 split!
    - 가운데 key값을(60) 부모 노드로 주고 오른쪽 key값으로(82) 구성된 2-노드, 왼쪽 key값으로(45) 구성된 2-노드를 따로 따로 구성한다
    - 부모 노드에서 자식 노드가 생겼다는 것은 split하지 않았다는 것이고 그렇기에 부모노드에는 항상 자리가 있다
- 다시 4-노드[50, 53, 57]에 도착해서 split
    - 가운데 key값을(53) 부모 노드로 주고 오른쪽 key값으로(57) 구성된 2-노드, 왼쪽 key값으로(50) 구성된 2-노드를 따로 따로 구성한다

root가 4-노드가 되면 root 를 split시켜서 그 중간값으로 새로운 root 만든다 

<br>

### 시간 복잡도

- split 1개 = O(1)
- w.c - 매 level 마다 split 발생할 수 있으므로 O(logN)

<br><br>

# 2-3-4 트리의 삭제 연산

<img width="345" alt="image" src= 'https://user-images.githubusercontent.com/83294376/219555934-f16438c4-1b85-489a-844d-0459adc17a4f.png'>

- 20을 삭제하고 싶다면 20과 가장 가까운 수와 바꿔준 후에 삭제한다

<br>

### 부모가 2-노드인 경우

<img width="345" alt="image" src= 'https://user-images.githubusercontent.com/83294376/219556006-2270f3a4-9bd6-47e1-afa2-2cc40b416dae.png'>

- 자식이 1개만 남으면 안됨으로 조치를 취해야 한다
- 값을 삭제하러 루트에서 리프 노드로 가다 2-노드를 만나면 **2-노드 → 3-노드**로 바꿔준다

<br>

### 형제 노드가 2-노드가 아닌 경우

<img width="345" alt="image" src= 'https://user-images.githubusercontent.com/83294376/219556303-b7a70a5c-dfe3-4520-a8ff-22c631f13414.png'>

- 옆 형제에게 갖고 올 수 있으면 갖고 온다
- root의 값을 가져오고 그 부족한 부분은 root의 자식, 2-노드의 형제에게 빌려서 채운다

<br>

### 형제 노드가 2-노드인 경우

<img width="345" alt="image" src= 'https://user-images.githubusercontent.com/83294376/219556120-45c0ea85-24c7-4f3a-99b2-3e178119639a.png'>

- 나의 왼쪽 형제와 부모의 가장 작은 값과 나를 합쳐서 4-노드를 만든다 (fusion)

<br>

### 루트가 2-노드인 경우

<img width="445" alt="image" src= 'https://user-images.githubusercontent.com/83294376/219556197-ce47e305-2ea0-4571-8332-01ddce6df184.png'>

- 루트가 2-노드인 경우 루트를 fusion을 해주지 않는다
- 루트가 2-노드이고 그 자식들도 2-노드인 경우 3개의 값을 합쳐서 4-노드 만들어주고 새로운 root 만들어준다 (h-1)

<br>

**시간복잡도**

w.c - 레벨마다 fusion 일어날 수 있기에 O(logN)

<br><br>

# Red Black Tree 와 2-3-4 트리

![image](https://user-images.githubusercontent.com/83294376/219556459-45978b61-e6d0-44ec-8a1d-6491784400e9.png)

- 2-노드는(34) 블랙노드로 바꾼다
- 3-노드는([30, 34]) 두 개의 노드로 나눈다
    - 2-3-4 트리의 level 1에서는 중간값이 블랙 노드가 된다
    - 2-3-4 트리의 level 2에서는 중간값이 레드 노드가 된다
    - 레드 노드의 자식은 무조건 블랙이여야 하기에 위의 단계가 번갈아가면서 일어난다
- 2-노드는 level 1 차치 / 3-노드, 4-노드는 level 2 차지
- 2-3-4 트리의 한 노드를 Red-Black Tree의 level 별로 생각해봤을때 블랙 노드의 개수가 전체 높이의 2/h가 넘어서 루트부터 리프 노드까지 블랙 노드의 개수가 일정해진다
    - 2-노드의 경우 레벨 1개 당 블랙 1개
    - 3-노드, 4-노드의 경우 레벨 1개 당 블랙 1개, 레드 1개 (자식 2개가 한 레벨에 있으므로)
    - ⇒ 2-3-4 트리의 한 레벨 당 최소 1개의 블랙 노드가 생긴다

<br>

### 시간 복잡도

- O($log_4^N$) ≤ 2-3-4 트리의 h ≤ O($log_2^N$)
- 2-노드는 level 1 차치 / 3-노드, 4-노드는 level 2 차지
- 3-노드, 4-노드는 level 2를 차지하므로 이러한 관점에서 h의 w.c를 생각해준다
- Red-Black Tree의 h ≤ 2-3-4 트리의 h * 2( 2레벨 차지하므로)
- Red-Black Tree의 h ≤ O($log_4^N$) * 2
- Red-Black Tree의 h ≤ O($log^N$)
