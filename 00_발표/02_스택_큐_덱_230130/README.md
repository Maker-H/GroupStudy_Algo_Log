# 자료구조 2회차 - 스택, 큐, 덱

## 𝐈𝐧𝐟𝐨

 - 📌 발표자 : 진희솜
 - 🗓️ 2023-01-30

    
</aside>

<br>

---

<br>

- RAM (Random Access Memory)
    - [Wikipedia](https://en.wikipedia.org/wiki/Random-access_memory)
        
        Form of computer memory that can be read and changed in any order. 
        
        Allows data items to be read or written in almost the same amount of time irrespective of the physical location of data inside the memory. 
        
        In contrast with order direct-access data storage media(hdd, cd, dvd, magnetic tapes) vaires significantly depending on their phusical locaitons on the recording medium, due to mechanical limitations such as media ratation speeds and arm movement
        
    
    물리적으로 어느 위치에 있던지 읽기와 쓰기에 걸리는 시간이 같음을 전제하는 메모리의 일종, 시디나 hdd 등 거기까지 디스크를 돌려서 읽어야 하기 때문에 데이터의 물리적 저장 위치에 따라 읽기와 쓰기에 걸리는 시간이 다르다. RAM을 전제하기에 읽기와 쓰기의 시간이 동일하다고 가정할 수 있다

<br><br>

# 배열과 리스트

<br>

## 배열

배열을 A라는 변수로 선언하면 A에는 배열의 주소가 저장되어 있다. 

<br>

![image](https://user-images.githubusercontent.com/83294376/215624210-0a29ad5a-1595-4186-b45d-4b492af253bf.png)
![image](https://user-images.githubusercontent.com/83294376/215624236-a6342f21-a17c-444d-a937-365fcbdb1b19.png)

<br>

`A[2] = A[2] + 1` 

- 쓰기와 읽기가 일어난다
    - A[2]를 읽고 +1 해서 다시 A[2]에 써야 하기 때문
    - 읽기와 쓰기는 계산의 편의상 단위시간에 편입시키지 않았으나 사실은 들어가야함
- 대입과 산술 연산도 일어난다

<br>

`A[n]` = **O(1)** 

- **이 연산이 상수시간인 이유**
    - A[2]의 값을 읽기위해선 주소를 알면 바로 읽으면 됨. (이게 가능한 이유는 우리가 RAM(random access memory)를 사용한다고 가정하기 때문)
- A[2]의 주소 = A[0]의 주소 +2 * 4byte
    - 이 때 연산 2번 밖에 일어나지 않기에 상수시간 내에 값을 읽어올 수 있음

⇒ 모든 시간 합쳐도 상수시간 내이기 때문에 O(1)이라고 생각. 

⇒ 값을 읽고 쓰는 것이 모두 상수시간 내에 이루어지는 것을 우리는 배열이라고 한다.

<br><br>

## 리스트

<br>

### 배열과의 차이점

1. **읽기와 쓰기로 이루어진 배열과 달리 강력한 연산을 제공**
2. **원소 저장 방법**
3. **용량 자동 조절(dynamic array)**

<br>

### 리스트 원소 저장 방법
<img width="345" alt="image" src= 'https://user-images.githubusercontent.com/83294376/215624540-6fd69092-8e54-4779-8a40-532e5821c7b4.png'>


모든 원소가 각각의 주소에 저장되어 있음. 배열처럼 주소가 연결되어 있지 않음 

그렇기에 리스트의 배열은 각각의 원소들이 저장되어 있는 주소값을 가짐

<br>

`A[2] = A[2] + 1` 하면 
<img width="345" alt="image" src= 'https://user-images.githubusercontent.com/83294376/215625045-55a6ff45-44a9-47ff-aeba-2b5018ac1349.png'>


1이라는 객체가 새로 생기고 A[2]가 새로 생긴 객체의 주소를 담음

<br>

### 강력한 삽입과 삭제 연산

`A.append(6)`하면 맨 뒤에 6을 삽입하는 것. 근데 6이 들어가는게 아니라 6이라는 객체가 어딘가에 저장되고 주소값만 A[4]에 들어감.

- **O(1)** - 아래에서 설명 [append 구현](https://www.notion.so/append-e5632d0f9d554944b6385db48e3ccf82)

`A.pop( )`은 맨 뒤의 값을 지우고 리턴. 그러면 6이 리턴되고 연결이 끊김

- **O(1)** - 끝에 있는 애만 지우면 되기 때문에 상수시간 내 해결

`A.pop(1)`을 해서 인덱스를 주면 A[1]을 제거하고 리턴. A[1]이 사라지면 **오른쪽에 있는 애들이 자리를 매꿈** 이 경우에는 A[2], A[3]가 그 자리를 매꿈. 

- **O(n)** - w.c는 pop(0)의 케이스로 그러면 오른쪽에 있는 모든 원소들이 당겨와야 하기 때문

`A.insert(1, 10)` : A[1]에 10을 삽입. 이미 값이 있을때는 **이미 있는 값 오른쪽으로 옮겨서** 1에 삽입.

- **O(n)** - w.c는 insert(0, value)의 케이스로 그러면 오른쪽에 있는 모든 원소들이 움직여야 하기 때문

`A.remove(value)` : A에서 value 제거. **오른쪽에 있는 애들이 당겨와서 자리를 매꿈.**

- **O(n)** - w.c는 remove(value = 0의 자리)의 케이스로 그러면 오른쪽에 있는 모든 원소들이 움직여야 하기 때문

`A.index(value)` : value가 처음으로 등장하는 인덱스 리턴

- **O(n)** - w.c는 index(value = 마지막 자리)의 케이스로 그러면 마지막까지 모든 원소를 확인해야 하기 때문

`A.count(value)` : value가 나오는 횟수 연산해줌

- **O(n)** - w.c는 count(value = 마지막 자리)의 케이스로 그러면 마지막까지 모든 원소를 확인해야 하기 때문

<br>

### 용량 자동 조절 (동적 배열)

**배열**은 코드로 큰 메모리 할당해준 다음 배열 복사해줘야한다
<img width="305" alt="image" src= 'https://user-images.githubusercontent.com/83294376/215625131-b7635d70-176a-4039-a666-366a78965536.png'>

<br>

파이썬의 **동적 배열(리스트)**는 모자라면 늘리고 넘치면 줄이는걸 자기 마음대로 함
<img width="345" alt="image" src= 'https://user-images.githubusercontent.com/83294376/215625169-f717dd53-a05e-4d14-9efd-e7e7c6303cbe.png'>


<br>

### 리스트 내부 동작 방식

**변수**

`capacity`(용량) : 리스트의 총 크기

`n`(저장된 값의 개수) : 리스트 안에 저장된 값의 개수

→ python 내부적으로 현재 capacity와 n를 항상 알고 있어야 하기에 이런 추가 정보를 위한 메모리가 필요하므로 빈 리스트 A는 0바이트보다 클 수 밖에 없다

<br>

**append 구현**

```python
**A.append(x)**:

	if A.n < A.capacity: -> 저장공간이 더 크면
		A[n] = x -> n을 인덱스로 사용
		A.n = n + 1 -> 원소 추가로 n+1

	elif A.n == A.capacity: -> 용량이 다 참
		B = (**A.capacity * 2 크기의 리스트 할당**)

			for i in range(n): -> O(n)
				B[i] = A[i] -> 이사

			del A -> A 지우기
			A = B -> 새로운 A 선언 후 B 넣기
			A[n] = x -> 새A에 x 저장
```

**용량이 다 찬다면 (n = capacity)** 리스트를 복사해줘야하기 때문에 A에 저장된 값의 개수만큼 시간이 걸린다 → **O(n)**

**저장 공간이 더 크다면 (capacity > n)** append만 해주면 된다 → **O(1)**

그러나 용량이 다 차는 경우는 리스트의 크기가 커질 수록 드물게 발생하다. O()의 그래프에서 n이 무한대로 커질수록 드물게 발생한다. (크기가 $2^1$, $2^2$, $2^3$, $2^4$, $2^5$ … $2^n$ 일때만 발생한다.) 그렇기에 O(n) 시간보다는 훨씬 작으며 O(1)임을 알 수 있다고 함

* 강의에서는 설명하기 편하게 2배로 커진다고 했지만 실제로는 파이썬이 알아서 늘렸다 줄였다 한다고 한다. 자세한 부분은 hashtable을 알아야 이해할 수 있다고 함 


  
  <br>

>왜 비어 있는 칸을 가리키는데 n을 인덱스로 사용할까?

> * n은 원소 개수인데 개수를 그대로 인덱스로 사용하면 항상 마지막 값이 저장된 인덱스+1을 가리킴. 배열의 인덱스는 0부터 시작한다.

<br><br>

## list 보다 메모리 효율 높은 `numpy`

list는 원소 객체의 주소가 연속적이지 않다. 그렇지만 이 주소값을 연속적인 배열에 저장하여 사용한다.

![image](https://user-images.githubusercontent.com/83294376/215625866-2fe68793-3456-4977-8623-42e4a2fd9e5a.png)

→ 원소 객체의 id값이 다 다르다

<br>

그렇지만 NumPy의 경우 c의 배열 형식을 사용하기 때문에 **원소객체의 주소가 연속적이다** 

![image](https://user-images.githubusercontent.com/83294376/215626138-a5e1ca00-54ed-43f0-9d19-0a2f18a8854e.png)

→ 배열변수에 주소값이 저장되고 그 주소값을 따라 원소값을 읽는 형식을 사용한다.

→ 또한 동적으로 크기를 조절하는 list와 달리 NumPy 배열은 생성되면 고정된 크기를 갖는다. 그래서 append를 하면 c와 같이 무조건 메모리 공간이 큰 배열 생성 후 복사하는 식으로 append 해 배열에 데이터 추가시에는 list보다 훨씬 느리다.

<br><br>

# 순차적 자료구조

1. **배열과 리스트** (index로 임의의 원소를 접근)
- 연산자 [] : 배열의 원소에 접근 - O(1)
- 삽입(append, insert)
- 삭제(pop, remove)

2. **스택, 큐, 덱** (제한된 접근만 허용)
- stack - LIFO (Last In First Out), 버킷 구조, 먹은 곳으로 뱉는 말미잘…
- queue - FIFO (First In First Out), 선착순, 위에서 먹고 아래로 뱉는 사람…
- dequeue - stack + queue

3. **연결 리스트** (index로 접근 안됨)
- 원소들이 연속되지 않은 메모리 공간에 존재
- 배열은 연속된 메모리 공간에 존재

![image](https://user-images.githubusercontent.com/83294376/215626518-eb1ce399-6c42-4c4e-a1a7-27fe3bc142df.png)

<br><br>

# 스택

모든 자료구조는 삽입과 삭제 그리고 탐색이 가능해야함

<br>


딱 두가지 연산만 사용 가능

- 삽입 : push
- 삭제 : pop

있으면 편한 연산

- top : 가장 위에 있는 값 리턴
- len : 스택의 값의 개수 리턴

<br>

## 스택 구현

```python
S = Stack()
s.push(10)
print(s.pop())
print(s.top())
print(len(s)) # s.__len__()
```

```python
Class Stack:

	def __init__(self):
		self.items = []
	
	def push(self, val): **O(1)**
		self.items.append(val) 
		-> items에 val 들어간다

	def pop(self):  **O(1)**
		try:
			return self.items.pop()
			-> items 끝의 원소를 삭제 후 리턴

		except IndexError:
			print("Stack is empty")

	def top(self):  **O(1)**
		try:
			return self.items[-1]
			-> 리스트 끝에 있는 원소값 리턴
		except IndexError:
			print("Stack is empty")

	def __len__(self):  **O(1)**
		return len(self, items)

```

→ append, pop 등 모두 list의 메소드이다.

→ self는 생성된 객체 자체를 의미한다.

<br>

## 스택 함수

- `push(self, val)`  - **O(1)**
- `pop(self)` - **O(1)**
- `top(self)` - **O(1)**
- `len(self)` - **O(1)**
    
    → len이 O(1)인 이유는 list의 n 변수를 바로 받아오기 때문이다. 
    
<br>

## 스택 활용 - 괄호 맞추기

입력 : 왼쪽 오른쪽 괄호가 포함된 문자열

출력 : 괄호쌍이 맞춰져 있으면 True 아니면 False

<br>

<img width="145" alt="image" src= 'https://user-images.githubusercontent.com/83294376/215626753-1dccd013-e7ae-4e62-86a1-40d449ce5c8f.png'>

1번 오른쪽이라 push

2번 오른쪽이라 push

2번 왼쪽이라 기존 스택 마지막에 있는 원소 pop

3번 오른쪽이라 push

3번 왼쪽이라 기존 스택 마지막에 있는 원소 pop

1번 왼쪽이라 기존 스택 마지막에 있는 원소 pop

⇒ 스택이 다 비워짐으로 True 리턴

<br>

<img width="145" alt="image" src= 'https://user-images.githubusercontent.com/83294376/215627702-b93df88f-798f-4ae6-b819-9033f129a372.png'>

1번 오른쪽이라 push

1번 왼쪽이라 기존 스택 마지막에 있는 원소 pop

2번 왼쪽이라 기존 스택 마지막에 있는 원소 pop (에러)

⇒ 괄호 쌍이 안맞음으로 False 리턴

<br>

<img width="145" alt="image" src= 'https://user-images.githubusercontent.com/83294376/215626876-8021ca63-0e39-4d56-b1f0-afa9355fc903.png'>

1번 오른쪽이라 push

1번 왼쪽이라 기존 스택 마지막에 있는 원소 pop

2번 오른쪽이라 push

⇒ 스택에 괄호가 남아 있음으로 False 리턴


```python
S = Stack()

for p in parseq:
	if p == '(':
		S.push(p)

	elif p == ')':
		try: 
			S.pop() -> 에러면 오른쪽 괄호가 더 많음
		except:
			return False

	else:
		print("not allowed symbol")

if len(S) > 0: -> 왼쪽 괄호가 더 많다
	return False
else:
	return True

```

<br><br>

## 스택 활용 - 계산기

입력 : +, -, *, /, (, ), 숫자(영문자)로 구성된 infix 수식

출력 : Postfix 수식

<br>

**infix → postfix로 변경하는 법**

1. 괄호치기
2. 연산자의 오른쪽 괄호 다음으로 연산자 이동
3. 괄호 지우기

<br>

ex) **a + b * c** → **a b c * +**

![image](https://user-images.githubusercontent.com/83294376/215628113-a6b4d352-fc05-4ca6-a20e-10f5bb7380da.png)

<br>

ex) **( a + b ) * c** → **a b + c ***

![image](https://user-images.githubusercontent.com/83294376/215628245-c83123cb-1631-4dba-a6b9-8adf7e95e415.png)

<br>

**postfix로 전환** 

```python
answer = []
opStack = Stack()

expression = input()

for token in expresssion:
	# token이 숫자라면
	if token.isdigit() or token.isalpha(): 
		answer.append(token)
	
	if token == '(':
		opStack.push(token)
	
	if token == ')':
		# (를 pop할때까지 pop 그리고 산술연산자 더한다
		operator = ''
		while operator != '(':
			operator = opStack.pop()
			if operator != '(':
				answer.append(operator)

	# 토큰이 연산자라면
	if token in '+*-/':
		if opStack.top() in '+-':
			s_pri = 1 
		elif opStack.top() in '*/':
			s_pri = 2
		else:
			s_pir = 0
		t_pri = 1 if token in '*/' else 2

		# 스택의 연산자 우선순위가 토큰보다 낮으면
		while s_pri < t_pri:
			answer.append(opStack.pop())
			if opStack.top() in '+-':
				s_pri = 1 
			elif opStack.top() in '*/':
				s_pri = 2
			else:
				s_pir = 0
		
		# 스택에 있는 우선순위 높은 연산자 다 빼낸 뒤 자신이 들어감
		opStack.push(token)

# opStack에 뭔가 남아있으면 모두 pop
while len(opStack) != 0:
	answer.append(opStack.pop())
			 
```

<br>

**계산**

```python
S = Stack()

def calculate(answer): 
	for token in answer:
		# 숫자라면
		if token.isdigit():
			S.push(token)
	
		if token in '+-/*':
			a = S.pop() -> 나중에 넣은 숫자
			b = S.pop() -> 먼저 넣은 숫자
			
			if token == '-':
				result = b - a
			elif token == '*':
				result = b * a
			elif token == '+':
				result = b + a
			elif token == '/':
				result = b / a
			
			S.push(result)
		
	return result
```

<br>

**6 + (3 - 2) * 4**  → **6 3 2 - 4 * +**

- `infix → postfix`
<img width="345" alt="image" src= 'https://user-images.githubusercontent.com/83294376/215628383-4aaea02b-9872-45db-9fd0-6cef2e738ba6.png'>


- `postfix → 계산`
<img width="345" alt="image" src= 'https://user-images.githubusercontent.com/83294376/215628431-58fb850e-266c-4bce-aa67-03b9ce4e7f15.png'>


<r><br>

# 큐

FIFO(First-In First-Out) 규칙의 순차적 자료구조

- 삽입 : enqueue
- 삭제 : dequeue
<img width="245" alt="image" src= 'https://user-images.githubusercontent.com/83294376/215628478-9bea13f4-eba6-42af-bb93-5cabc7eed31e.png'>

<img width="245" alt="image" src= 'https://user-images.githubusercontent.com/83294376/215628495-06b82fbc-2459-49fc-816a-4f748a43a19a.png'>


<br>

**구현**
```python
class Queue:
	def __init__(self):
		self.items = []
		**self.front_index = 0**
	
	def enqueue(self, val):
		self.items.append(val)

	def dequeue(self):
		# front_index는 항상 큐의 첫번째 ele의 index 가리킨다
		if self.front_index == len(self.items):
			print('Q is empty')
			return None
		else:
			x = self.items[front_index]
			self.front_index += 1
			return x

```

→ 큐의 리스트에 있는 원소는 지우지 않은 상태에서 first_index를 활용하여 없는거처럼 흉내낸다. 그런 관점에서 self.front_index를 이해하면 된다.

→ 이렇게 하는 이유는 시간복잡도 때문. 리스트의 pop( )의 빅오가 **O(n)**인 것과 다르게 dequeue의 빅오는 **O(1)**이다

<br>

## 큐 활용 - Josephus problem

입력

- n : range(n)
- k : k 번째의 숫자를 차례로 제외 시킨다

`Josephus(n, k): return 최종 병사의 번호`

<img width="245" alt="image" src= 'https://user-images.githubusercontent.com/83294376/215628718-be425baa-185f-49a3-81f7-b431f84d0c7d.png'>

<br>

큐를 활용해서 풀기
<img width="245" alt="image" src= 'https://user-images.githubusercontent.com/83294376/215628763-de1ac1c2-6d72-4776-8e41-a684621fa417.png'>


<br>

**구현**
```python
Q = Queue()
def Joshephus(n, k):
	# 큐에 숫자를 다 넣는다
	for i in range(n):
		Q.enqueue(i)
	
	while len(Q) != 1:
		# k번째까지는 디큐 후 인큐
		for i in **range(1, k+1)**:
			Q.enqueue(Q.dequeue())
		# K+1번째는 디큐(죽인다)
		Q.dequeue()
	
	return Q.dequeue()
```

<br><br>

# 덱

**circular queue**의 연장선

- append( )
- pop( )
- appendleft( ) - 리스트 처음에 append
- popleft( ) - 리스트 처음

<img width="285" alt="image" src= 'https://user-images.githubusercontent.com/83294376/215628909-10812c52-d101-4242-b2c2-54504c79d93e.png'>



<br>

**구현**
```python
class Deque:
		def __init__(self, k):
		self.items = [0 for _ in range(k)]
		self.max = k
		self.front_index = 0
		self.rear_index = 0
		
		def append(self, val):
			if len(self.items) != self.max:
				self.items[self.rear_index] = val
				**self.rear_index = (self.rear_index + 1) % self.max**
			elif len(self.items) == self.max:
				print('deque is full')

		def append_left(self, val):
			if len(self.items) != self.max:
					self.items[self.front_index] = val
					**self.front_index = (self.front_index - 1 + self.max) % self.max**
			elif len(self.items) == k:
					print('deque is full')

		def pop(self):
			if len(self.items) != 0:
				tmp = self.items[self.rear_index]
				self.items[self.rear_index] = None
				**self.rear_index = (self.rear_index - 1 + self.max) % self.max**
				return tmp
			elif len(self.items) == 0:
				print('deque is empty')

		def popleft(self):
			if len(self.items) != 0:
				tmp = self.items[self_front_index]
				self.items[self_front_index] = None
				**self.front_index = (self.front_index + 1) % self.max**
				return tmp
			elif len(self.items) == 0:
				print('deque is empty')
				
			
		
```

→ append_left에서 self.front_index = self.front_index -1 % self.max만 해주면 front이기에 front가 0일때 계산후 front는 -1이 되어 에러가 난다, 그렇기에 + self.max 해줘야 한다

→ 모든 인덱스가 0일때 에러가 날지 안날지를 생각해보면 명확해진다.

→ 모든 함수에 대한 시간복잡도 - **O(1)**

- 다른 스택이나 큐와 달리 인덱스 사용하기 때문에 모든 함수의 빅오는 상수시간 내에 이루어진다.





