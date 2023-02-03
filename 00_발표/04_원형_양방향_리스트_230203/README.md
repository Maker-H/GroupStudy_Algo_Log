# 자료구조 4회차 - 원형 양방향 리스트

## 𝐈𝐧𝐟𝐨

- 📌 발표자 : 구본재
- 📌 작성자 : 진희솜, 구본재
- 🗓️ 2023-02-03

### QnA

Q) __iter__가 제대로 돌아가나요 __iter__ 내부에 self.head부터 None을 비교하는데 self.haed에 더미노드가 있어서 실행 후 바로 정지 될 것 같다.
A) self.head로 시작하면 더미노드를 만나서 정지된다. self.head.next에서 시작해야한다. 

Q) split의 시간복잡도는 어떻게 되는가
A) 총 6번의 연결로 이루어짐으로 상수시간 내에 해결되기 때문에 O(1)
 
Q) split(x)을 사용했을 때 노드 사이즈는 어떻게 구해야 하는가
A) x까지 탐색하여 x까지의 노드 개수를 구하여 앞 리스트에 분배하고 전체 리스트 사이즈에서 앞에서 구한 노드의 개수를 뺀 값을 뒷 부분에 분배한다.

Q) split을 사용했을 때 더미데이터가 없는 부분은 어떻게 처리되는가
A) 앞부분을 더미노드를 포함하게하고 뒷 부분은 새로운 양방향리스트 인스턴스를 만들어서 새로운 더미노드 뒤에 나눈 노드를 추가한다. 

<br><br>

# 원형 양방향 연결 리스트

<img width="445" alt="image" src= 'https://user-images.githubusercontent.com/83294376/216527029-e9854347-b3ec-477a-bdb5-97740a99f4fd.png'>

<br>

## 더미 노드

- 원형 연결리스트의 시작 노드를 표현하는 마커
- key를 None으로 만듬으로써 고유성을 부여한다

1. 더미 노드의 next가 스스로를 가리키고 더미노드의 prev이 스스르로를 가리키는 빈 리스트에서 시작한다

    <img width="245" alt="image" src= 'https://user-images.githubusercontent.com/83294376/216527108-05b8987c-90d3-429a-a21c-f562f64358a5.png'>
    
2. 더미 노드(일종의 헤드노드) 뒤에 노드를 연결해준다

    <img width="245" alt="image" src= 'https://user-images.githubusercontent.com/83294376/216527179-dfcc93f2-3d9b-4a1c-9e55-5ff79656f81f.png'>
 
<br>

## 노드와 매직 메서드 구현

```python
class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = self
		sef.prev = self
		
	#노드의 키값 리턴
	def __str__(self):
		return self.key
```

```python
class DoublyLinkedList:
	def __init__(self):
		self.head = Node()
		self.size = 0

	def __iter__(self):
		tmp = self.head
		while tmp != None:
			yield tmp
			tmp = tmp.next

	# 양방향 원형 리스트 전체 출력
	def __str__(self):
		return ", ".join(oneNode for oneNode in self)
	
	def __len__(self):
		return self.size
```
<br>

## splice 연산

- a와 b 사이에 있는 노드를 통째로 잘라서 x다음에 집어넣는 연산이다
- **O(1)** - 모든 경우 6개만 수정해주면 된다

<img width="545" alt="image" src= 'https://user-images.githubusercontent.com/83294376/216527253-aaeaf623-9977-46d0-a13b-f1ad18ca86ce.png'>


**총 6개의 링크를 바꿔주면 된다.**

1. x와 a 연결 → 2개
2. b과 xn 연결 → 2개
3. ap와 bn 다시 연결 → 2개

<br>
    
**조건**
1. a가 나온 후에 b가 나온다
2. a와 b 사이에 x 노드가 오면 안된다
3. a와 b 사이에 head 노드가 없어야 한다 

<br>

**구현**

```python
def splice(self, a, b, x):
	ap = a.prev 
	bn = b.next
	xn = x.next

	# ap와 bn 다시 연결
	ap.next = bn
	bn.prev = ap

	# x와 a연결
	x.next = a
	a.prev = x

	# b와 xn연결
	b.next = xn
	xn.prev = b

	
```

<br><br>

## 이동 연산

### move_after(self, a, x)

- 노드 a를 노드 x 다음으로 이동
- **O(1)** - splice 이용

<img width="345" alt="image" src= 'https://user-images.githubusercontent.com/83294376/216527309-f9dad92f-df7a-4321-b52f-6e877ea53515.png'>

<br>

**총 6회의 노드 연결 발생**

1. x와 a연결 - 2회
2. x.next와 a연결 - 2회
3. a가 빠진 자리 양 옆의 노드 다시 연결 → 2회

<br>

**구현**

```python
move_after(self, a, x):
	# splice(a, a, x)
	an = a.next
	ap = a.prev
	xn = x.next
	
	# x와 a연결
	x.next = a
	a.prev = x
	
	# xn과 a연결
	xn.prev = a
	a.next = xn
	
	# a 양 옆의 노드 다시 연결
	an.prev = ap
	ap.next = an
		
```
<br>

### move_before(self, a, x)

- 노드 a를 노드 x **이전**으로 이동
- **O(1)** - splice 이용

```python
def move_before(self, a, x):

	# splice(a, a, x.prev)
	ap = a.prev
	an = a.next
	x = x.prev.next
	
	# xp와 a연결
	xp.next = a
	a.prev = xp
	
	# a와 x연결
	x.prev = a
	a.next = x
	
	# a의 양쪽의 노드 다시 연결
	ap.next = an
	an.prev = ap
	

```

<br><br>

## 삽입 연산

### insert_after(self, x, key)

- 노드 x 뒤에 데이터가 key인 새 노드를 생성해 삽입
- **O(1)** - splice 이용

```python
def insert_after(self, x, key):
	move_after(Node(key), x)
	= splice(Node(key), Node(key), x)

	self.size += 1
```

<br>

### insert_before(self, x, key)

- 노드 x 뒤에 데이터가 key인 새 노드를 생성해 삽입
- **O(1)** - splice 이용

```python
def insert_before(self, x, key)
	move_before(Node(key),x)
	= splice(Node(key), Node(key), x.prev)

	self.size += 1
```

<br>

### push_front(self, key)

- 데이터가 key인 새 노드를 생성해 head 다음(front)에 삽입
- 현재 head는 더미 노드 가리키고 있음으로 더미 노드 다음에 삽입된다
- **O(1)** - splice 이용

```python
def push_front(self, key):
	insert_after(self.head, key)
	= move_after((Node(key), self.head)
	= splice((Node(key), Node(key), self.head)

	self.size += 1
```

<br>

### push_back(self, key)

- 데이터가 key인 새 노드를 생성해 head 이전(back)에 삽입
- 현재 head는 더미 노드 가리키고 있음으로 더미 노드 이전에 삽입된다
- **O(1)** - splice 이용

```python
def push_bach(self, key):
	insert_before(self.head, key)
	= move_before(Node(key), self.head)
	= splice(Node(key), Node(key), self.head.prev)

	self.size += 1
```

<br><br>

## 탐색 연산

### search(self, key)

- key 값 갖는 노드를 리턴하고, 없으면 None 리턴
- **O(n)** - w.c의 경우 없다면 끝까지 탐색해야 한다

```python
def search(self, key):
	# 더미노드부터 출발~
	tmp = self.head

	whlie tmp.next != self.head:
		if tmp.key == key:
			return tmp
		tmp = tmp.next

	return None
```

<br><br>

## 삭제 연산

### remove(self, x)

- **노드 x**를 삭제
- key를 이용해서 노드 삭제하려면 search를 같이 사용해준다
- **O(1)** - 노드 앞 뒤의 연결만 끊어주면 되니 상수시간 내에 해결

<img width="345" alt="image" src= 'https://user-images.githubusercontent.com/83294376/216527399-842c2b1a-68fe-4827-90ca-ba4469d5efbf.png'>


```python
def remove(x):
	# 지우고자 하는 노드가 이상할 경우
	if x == None or x == self.head
		return
	
	x.prev.next = x.next
	x.next.prev = x.prev
	
	del x
	self.size -= 1
```

<br>

### pop_front(self)

- head(더미노드) 다음의 노드를 삭제하고 값을 리턴, 없으면 None 리턴
- **O(1)** - remove 사용

<img width="295" alt="image" src= 'https://user-images.githubusercontent.com/83294376/216527442-11e131d8-6767-4241-bab5-25aa9c21537a.png'>


```python
def pop_front(self):
	if self.size == 0: 
		return None 

	key = self.head.next.key 
	self.remove(self.head.next)

	return key
```

<br>

### pop_back(self)

- head(더미노드) 이전의 노드를 삭제하고 값을 리턴, 없으면 None 리턴
- **O(1)** - remove 사용

```python
def pop_back(self):
	if self.size == 0:
		return None

	key = self.head.prev.key
	self.remove(self.head.prev)

return key
```

<br><br>

## 기타연산

### join(self, a)

- 리스트 뒤에 a 리스트 결합
- **O(1)** - splice 사용

<img width="145" alt="image" src= 'https://user-images.githubusercontent.com/83294376/216527499-ca4faab1-6e2d-4277-8141-3c1d8c3052fb.png'>

```python
def join(self, a):
	if a.size == 0:
		return None

	splice(a.head, a.head.prev, self.head.prev)
	self.size += a.size
```

<br>

### split(self, x)

- self를 노드 x 이전과 x 이후의 노드들로 구성된 두 개의 리스트로 분할
- 노드 x 찾기 위해서는 search 메서드 같이 사용
- **O(1)** - 총 6번의 연결로 이루어짐으로 상수시간 내에 해결

<img width="145" alt="image" src= 'https://user-images.githubusercontent.com/83294376/216527531-675d39c4-105f-4efe-9fb7-310d50936696.png'>

```python
def split(self, x):
	tail = self.head.prev	
	
	# 기존 리스트 분리 후 양 끝단 연결
	x.prev = self.head
	self.head.prev = x.prev

	# 분리된 리스트를 새로운 리스트로 만들어준다
	new_doublylinkedlist = DoublyLinkedList()
	
	new_doublylinkedlist.head.next = x.next
	x.next.prev = new_doublylinkedlist.head

	new_doublylinkedlist.head.prev = tail
	tail.next = new_doublylinkedlist.head

	# size 조정은 아래로
```

size 수정 방법 (생각해본 방법)

1. 각 리스트 안 노드의 개수가 몇 개 인지 찾은 다음에 빼기 혹은 더하기. → w.c에 따르면 O(n)이 된다
2. 위의 기능을 search_idx 함수로 분리

<br><br>