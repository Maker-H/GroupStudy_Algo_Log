# 자료구조 5회차 - 해쉬 테이블

## 𝐈𝐧𝐟𝐨

- 📌 발표자 : [@Bonjae9](https://github.com/Bonjae9)
- 📌 작성자 : [@Bonjae9](https://github.com/Bonjae9), [@Maker-H](https://github.com/Maker-H)
- 🗓️ 2023-02-06

<br>

## Q&A

</br>
Q : 발표자료에 해시테이블 삽입,삭제,탐색 연산의 시간복잡도를 O(n)이라고 적어 놓으셨는데 제가 알기로는 해시테이블의 시간복잡도는 O(1)이다 어느쪽이 맞나 ?

<br>

A : 결론적으로 말하면 해시테이블의 시간복잡도는 O(1)이 맞다. 그런데 이 값은 테이블에서 데이터가 차지하는 정도인 Load factor를 일정하게 유지 시켜주는 방법과 C-universal등의 Collision resolution method등을 통해서 개선이 되었을때 나온다. 

</br>
<hr>

</hr>


<br>

요약

1. 해쉬 함수를 이해하기 위한 시프트 연산자
2. 해쉬 테이블 구성 요소
3. 이상적인 해쉬 함수의 조건
4. 해쉬 함수의 종류
5. 클러스터와 충돌 발생의 연관 관계
6. Opend addresing - 빈칸 찾기 (충돌 해결 방법)
7. Chaining - 연결 리스트 활용 (충돌 해결 방법)

<br>

## 해쉬 함수를 이해하기 위한 시프트 연산자 (>>, <<)

### Left Shift(<<) 연산

간단하게 `2 << 1`를 생각해보자

2에서 4가 된다

`2 << 2`를 생각해보자

2에서 8이 된다

즉 왼쪽으로 한  칸을 갈때마다 2배가 커진다.

그러므로 **n << k** 의 연산은 **$n*2^k$ 와 같다** 

<br>

기억해야 하는 두가지

1. 결과 값의 크기는 피연산자의 타입에 의해 결정된다
2. 결과 값의 범위 밖으로 넘치는(overflow) 비트는 소멸, 새로운 비트는 ‘0’으로 채워진다

<br>

### Right Shift(>>) 연산

간단하게 `8 >> 1`를 생각해보자

8에서 4가 된다

`8 >> 2`를 생각해보자

8에서 2가 된다

즉 오른쪽으로 한 칸을 갈때마다 1/2 만큼 작아진다

그러므로 **n >> k**의 연산은 $n/2^k$와 같다

<br>

기억해야 하는 두가지

1. 결과 값의 크기는 피연산자의 타입에 의해 결정된다
2. 피연산자가 음수라면 최상위 비트가 1이므로 새로운 비트가 1로 채워진다


<br><br>


# Hash Table

### 해시 테이블의 구성 요소

1. Table (list)
2. Hash function
3. Collision resolution method

해시 테이블은 일종의 사전(dictionary)이고 Python의 dict 자료구조처럼 다음 연산을 빠르게 지원한다. (데이터 아이템(item)은 key값과 value값 쌍으로 구성된다고 가정) 
</br>

<img width="800px" alt="image" src= 'https://user-images.githubusercontent.com/123693844/217145931-745ec01b-7112-49f6-8347-74bdca457f68.png'>
<br>

해시 테이블은 보통 정보를 담아 저장할 수 있는 테이블 형태로 구현하며 정보(key)가 저장될 슬롯(slot) 번호를 계산하는 함수 f(x)를 **해시 함수(hash function)**이라 한다. 
-  f(key) = key % m 라면  `key % m`이 해시 함수
- 저장하고 싶은 인덱스에 다른 아이템이 이미 저장해있는 경우에는 **충돌(collision)** 발생
- 충돌 발생 시 **해결하는 규칙**을 **collision resolution**이라고 하고 이걸 **해결하는 방식**을 **collision resolution method**라고 한다
- collision resolution method에 따라 해시 **함수의 성능**이 결정된다

<br><br>

# 해시 함수(hash function)
`H(hash table) = m(slot)`

- H의 크기는 m의 개수와 같다
- m은 $2^n$개가 일반적이다

<br>

**효율적인 Hash function의 조건**

1. Less collision - 낮은 충돌
2. Fast computation - 빠른 계산
→ 위의 요소들은 상충된다

<br>

**key 값이 정수가 아니라 해시 함수를 사용할 수 없는 경우**

- key값을 정수에 대응 시키는 **prehash함수**를 정의하고 사용하여 변환 후 해시 함수를 사용한다.
- Python에 내장된 hash(x) 함수는 x를 정수로 대응 시키는 prehash함수이며 __hash__를 통해서 지정할 수 있다.

<br><br>

# 해시 함수의 종류
## 이상적인 해시 함수

### **Perfect hash function**

- 슬롯과 key를 1 대 1로 대응 시키는 함수
- 이상적인 형태의 함수 (비현실적)

<br>

### **Universial hash function**

- $Pr(f(x) == f(y))$ = $1/m$
- 서로 다른 키 값이 충돌이 발생할 확률이 size of hash table에 반비례하는 함수
- (Pr은 probability의 약자)
- 여전히 구현하기 매우 어렵고 비현실적

<br>

### **C-Universial hash function**

- $Pr(f(x) == f(y))$ = $c/m$
- c = 상수
- Universial hash function 만들기가 어렵기 때문에 상수 c 추가해서 약화된 함수 사용

<br>

## 현실에서 자주 사용되는 해시 함수

### **Division hash function**

- % 사용 하는 해시 함수
- key값들의 성질이 잘 알려져 있지 않은 경우에 유용
- f(k) = k % m(size of hash table) - 간단하게 사용
- f(k) = (k % p(prime num)) % m(size of hash table) - 보통 소수 사용
- 소수 사용해야 충돌이 적어진다

<br>

### **Multiplication hash function**

- 시프트 연산 사용하는 해시 함수
- f(k) = ((ak) % 2$log^k$) >> ($log^k$- $log^m$)
- a = random num
- 결과의 범위 내에서 ((ak) % 2$log^k$)에 $2^{(log^k - log^m)}$를 **나눈 값**

<br>

### **Folding hash function**

- key값의 **digit을 일정한 규칙**으로 나눠 연산하는 해시 함수
- **shift folding**
    - 두 digit씩 나눠 모두 더한 후 % m
    - 계좌번호 k=1234-567-890
    - (12 + 34 + 56 + 78 + 90) % m
- **boundary folding**
    - 여러 digit으로 나눠 모두 더한 후 % m, 이때 짝수번은 거꾸로 더한다
    - 계좌번호 k=1234-567-890
    - (12 + **43** + 56 + **87** + 90) % m

<br>

### **Mid-square hash function**

- 연산 후 중간값을 주소로 이용하는 해시 함수
- key를 연산한 후, 그 결과의 중간 부분을 떼어내 주소로 이용
- m=2, k=3121 → $3121^2$ = 9740641
- 중간 3 digit을 떼어낸 306이 주소가 된다

<br>

### **Extraction hash function**

- key의 각 파트마다 **임의의 digit을 떼어내** 연결해 계산
- 계좌번호 k=1234-567-890
- 1234에서 12, 567에서 7, 890에서 9를 떼어내 1279라는 주소를 만든다

<br><br>

## 키 값이 string 일때 사용하는 해쉬 함수

### **Additive hash function**

- key[i]의 단순 합을 계산하여 사용하는 해시 함수
- $\sum key[i]$ % m

```python
h = initial_value
	
for i in range(len(key)): 
	h += key[i]

return h % p(prime num) % m(size of hash table)
```

<br>

### **Rotating hash function**

- <<, >>연산과 ^연산을 반복하여 계산하는 해쉬 함수

```python
h = initial_value

for i in range(len(key)):
	h = (h<<4)^(h>>28)^key[i]

return h % p(prime num) % m(size of hash table)
```

- h에 $2^4$를 곱한 값 ^ h에서 $2^{28}$를 나눈 값 ^ 키의 아스키

<br>

### Universial hash function 

- C++ STL(STLPORT 4.6.2 hash)에서 사용
    - `h = 0`, `a = 5`
- JAVA(java.lang.String.hashCode)에서 사용
    - `h = 0`, `a = 31`
- Bernstein hash에서 사용 (Daniel J.Bernstein 수학자, **아직 살아있음**)
    - `h = 5381`, `a = 33`
- (1:1 대응하는 해쉬함수)
- key값에 모든 digit에  h = ((h*a) + key[i]) % p 연산을 수행한 후 h % m

```python
h = initial_value

for i in range(len(key)):
	h = ((h * a) + key[i]) % m(size of hash table)

return h % m(size of hash table)
```

<br><br>

# Collision resolution method

<br>

**Collision resolution method의 종류** 
- open addressing
    - linear probing
    - quadratic probing
    - double hashing
- chaining

<br>

## **Cluster**

- 키 값들이 모여 있는 곳을 클러스터라고 한다
- 바로 아래의 경우  저장 후 [A2, A3, B2, A5, B5, C1]를 클러스터라고 할 수 있다
- 클러스터가 많이 있을수록, 사이즈가 클수록 삽입/탐색에 시간이 오래 걸린다
    - **Hash function** (collision 발생 가능성)
    - **Collision resolution method**
    - **load factor** = n(아이템 개수)/m(slot 개수)
        - n/m 이 1이면 다 차있으니 테이블 전부가 클러스터이다
        - n/m 이 0.5면 반쯤 차있으니 클러스터 크기가 작다
<br>
- c-universial hash function을 사용한 상태에서 평균적으로 m(슬롯 개수) ≥ xn(아이템 개수)이면 (최소 x% 이상 빈 슬롯이면) 더 큰 테이블을 만들어서 옮겨준다. 그러므로 항상 ?% 이상 빈 슬롯이 되게 유지해준다. → **그래야 해쉬의 시간 복잡도가 O(1)이 된다**
    - **파이썬의 경우** 8개의 슬롯으로 시작. 
    - 3m≥2n이면 테이블을 2배로 늘려 **1/3은 항상 비어 있도록 유지**한다

<br>

- collision 횟수 /  n(아이템 개수) = 충돌 비율
- 세로축이 수행시간, 가로축이 Load factor인 그래프 그려서 성능 평가 할 수 있다

<br>

## Load factor
**Load factor**는 전체 테이블 크기에서 데이터가 차지하는 공간의 비를 말하며 Load factor의 값이 1에 가까워 질 수록(데이터가 차지하는 공간이 증가 할 수록) 연산 속도가 감소한다. 
</br>


<img width="400" alt="image" src= 'https://user-images.githubusercontent.com/123693844/216984281-59a98ffc-b206-42c1-84f1-882d70697a83.png '>

<Load factor에 따른 수행시간 그래프 >

<br>

그래서 **Load factor**를 일정하게 범위 안에서 유지하기 위해서 테이블의 크기를 일정한 값이 되면 2배로 늘려주는 방법을 사용하기도 하며, 보통 데이터가 50% 이하 공간을 점유하도록 유지하면 연산 속도는 O(1)을 가진다. 

<img width="400" alt="image" src= 'https://user-images.githubusercontent.com/123693844/216984368-a2505fc3-b5f4-4e6a-95ef-10a64abe9162.png'>

<br>

< Load fator 특정값으로 유지 시 각 cluster의 연산속도는 O(1)> 

<br>

**C-universal** and **Loaf factor 0.5** 이하 유지 

⇒ 상수 시간 내에 삽입, 삭제, 탐색 연산이 가능하다.


<br><br>

## **open addressing**

- 충돌이 발생하면 그 다음 슬롯을 차례로 탐색하면서 가장 먼저 찾은 빈 슬롯에 저장하는 방법
- **파이썬의 dict가 사용하는 방식**. (f(k)에서 충돌 발생할 경우 5f(k)+1에 있는 슬롯을 검사하는 방식과 유사한 방법을 사용한다.

<br>

**open addressing의 종류** 

- linear probing
- quadratic probing
- double hashing


### Linear probing

- 충돌이 일어나면 한 칸씩 아래로 내려가면서 빈 칸을 찾고, 빈 칸이 있다면 그곳에 저장
- 충돌 일어나면 클러스터의 길이가 무조건 1씩 늘어나기에 좋은 충돌 해결 방법이 아님
- 해쉬 함수의 성능 → 클러스터의 사이즈가 연산의 효율을 결정한다

**linear probing**은 클러스터 길이를 증가 시키고 연산 속도는 클러스터 길이에 비례함으로 데이터가 증가 할 수록 연산 속도가 반비례로 감소함으로 좋은 방법은 아니다.

<br>

**예제**
H = 10
key = A5, A2, A3, B5, A9, B2, B9, C2
f(k) = k % 10
![image](https://user-images.githubusercontent.com/83294376/218029664-13daa875-fde5-478b-a347-a9142e4d7707.png)


**Search(C2)** 때를 가정

- 2 자리 먼저 탐색 → A2 존재 (한 칸 아래로)
- 3 자리 탐색 → A3 존재 (한 칸 아래로)
- 4 자리 탐색 → B2 존재 (한 칸 아래로)
- 5 자리 탐색 → A5 존재 (한 칸 아래로)
- 6 자리 탐색 → C2 존재

→해시 테이블에 없는 값 찾기 위해서는 전체를 다 살펴야 한다

<br>

**`find_slot(key)` - 탐색 연산**

- key값이 있으면 slot 번호 리턴
- key값이 없다면 **key값이 삽입될** slot 번호 리턴
- None 대신 EMPTY 사용하는 이유는 그래야 해쉬 테이블 안에 None을 저장 할 수 있기 때문이다. [자세히 보기](https://just-taking-a-ride.com/inside_python_dict/chapter2.html)

```python
h_index = f(key) 
start = h_index

while H[h_index] != EMPTY and H[h_index] != key:
	# 마지막 인덱스까지 갔을 경우 다시 처음으로 돌아가야한다
	h_index = (h_index + 1) % m 
	
	# 한바퀴 돌았다면 내가 찾는 값이 없다는 것
	if h_index = start:
		return FULL # 정하기 나름

return h_index
```

- 처음 찾는 그 자리에 아이템이 있어야 하는데 계속 아래로 내려가다 None을 발견했다면 아이템이 이 테이블에 없다는 것을 의미한다. 그렇기에 None이 있는 자리의 인덱스를 리턴한다
- (h_index + 1) % m에서 m인 이유는 해쉬 테이블 인덱스의 시작이 0부터 이기 때문이다. m을 사용해야 마지막 인덱스 다음 인덱스 값을 가리킬 수 있다

<br>

`search(key)` - 탐색 연산

- key 값을 갖는 아이템을 찾아 value값을 리턴하고, 없다면 None을 리턴

```python
h_index = find_slot(key)

if H[h_index] != EMPTY:
	return H[h_index].value

return None
```

- (h_index + 1) % m에서 m인 이유는 리스트 인덱스의 시작이 0부터 이기 때문이다. m을 사용해야 마지막 인덱스 다음 인덱스 값을 가리킬 수 있다

<br>

`set(key, value=None)` - 삽입 연산

```python
h_index = find_slot(key)

# 다 차있다면 테이블 키워야 한다
if h_index == FULL:
	return None # 실패!

# 아이템 찾은 경우
if H[h_index] != EMPTY:
	H[h_index].value = value

# 아이템 못 찾은 경우
elif H[h_index] == EMPTY:
	H[h_index], H[h_index].value = key, value

return key
```

<br>

`remove(key)` - 삭제 연산

- 클러스터 중간에 있는 아이템을 삭제해서 EMPTY으로 만들었다고 가정했을때 ‘find_slot 함수’가 찾는 아이템이 그 아래에 있음에도 불구하고 삭제연산의 결과인 EMPTY을 **아이템이 없다**로 인식할 수 있다는 문제가 존재
- 아이템 삭제로 EMPTY을 만들지 않고 채워주기 위해 클러스터 안의 모든 아이템을 위로 한 칸씩 옮긴다. **다만 이때 밀려서 내려간 것이 아닌 아이템들을 움직여서는 안된다.**
- remove(A3) 후 search(B2) search(A5)를 하는 과정을 생각해보면 아래의 A5, B5를 움직여서는 안된다. B2, C2는 움직인다

![image](https://user-images.githubusercontent.com/83294376/218033514-070efd6f-8e6c-4863-a396-4f2e200f3bc6.png)

간단하게 생각

- f(k)가 blank의 앞에 있으면 black에 아이템이 있었기 때문에 밀려내려왔다는 것.
- 즉 f(**k) < blank ≤ item**

<br>

문제 1. **f(k)가 인덱스 마지막에 위치하는 경우**

- 인덱스는 blank → item → f(k) 순서
- f(k) → item → blanck 순서로 읽어내려간다
<img width="205" alt="image" src= 'https://user-images.githubusercontent.com/83294376/218034371-8066c8b8-1dfd-4b12-a407-bb74efdb32a9.png'>


문제 2. **blank가 인덱스 마지막에 위치하는 경우**

- 인덱스는 item → f(k) → blank 순서
- f(k) → item → blanck 순서로 읽어내려간다
<img width="345" alt="image" src= 'https://user-images.githubusercontent.com/83294376/218034276-1e3ac31a-9ed7-4035-86b9-ac6f175bc3ed.png'>


<br>

**다른 그림으로 살펴 보는 remove 함수**
<img src = https://user-images.githubusercontent.com/123693844/216984101-c4d383e3-3d2f-4cd3-a01c-56c09e1fa2c1.png width = 800 >
< Open addressing remove 동작 >


<img src = https://user-images.githubusercontent.com/123693844/217253728-f077b427-748a-4ff5-883b-d1e5946f2507.png width = 500 >
< k가 i위치로 이동 가능한 경우 >

<br>
					  
remove method에서는 key값을 찾기 위해서 에서 알맞은 위치로 조정하는 작업을 하는데 그중 탐색중인 위치의 해쉬함수 대응값(k)가 이동 할 수 있는 경우는 위 그림을 보면 i k j / j i k / k j i로 세가지가 존재 한다. 하지만 이것들은 실제로는 한 가지이다. 테이블도 원형구조를 가지기에 마지막이 처음과 연결되어 있기 때문이다. 따라서 위 3가지 경우는 동일한 경우이며 i와 j 사이에 k가 있어야 이동 가능함을 알 수 있다.

```python
def remove(key):
	remove_index = find_slot(key)
	
	# 값이 존재하지 않을때
	if H[remove_index] == EMPTY:
		return None

	# H[remove_index] - 삭제된 아이템
	# H[moving_index] - 움직여야 하는 아이템
	moving_index = remove_index 

	while True:
		H[remove_index] = EMPTY
		
		while True:
			moving_index = (moving_index + 1) % m

			# 삭제한 이후에 EMPTY 만나면 삭제로 인한 EMPTY이 아니기에
			# 움직여줄 아이템 없음
			# 테이블이 다 차있다면 자기 자신의 EMPTY이기에
			# 더 찾을 필요 없음
			if H[moving_index] == EMPTY:
				return key
			
			k = f(H[moving_index])

			if k <= remove_index < moving_index or
					moving_index < k <= remove_index or
					remove_index < moving_index < k:
				break
		
		# 빈 슬롯을 채워주면 현재 있는 슬롯을 채워야 하기에 loop 돌린다
		H[remove_index] = H[moving_index]
		remove_index = moving_index
```

<br>

### Quadratic hashing
- Quadratic - 제곱이라는 뜻
- 충돌이 일어나면 여러 칸씩 아래로 내려가면서 빈 칸을 찾고, 빈 칸이 있다면 그곳에 저장
- k → k + $1^2$ → k + $2^2$  → k + $3^2$ → k + $4^2$
- Linear probing 보다 클러스터 사이즈가 덜 커진다
- 삭제 연산이 더 복잡해진다

<img src = https://user-images.githubusercontent.com/123693844/216984233-8aad6e2d-b3c9-49a7-b768-317c14d141af.png width = 800 >
< linear probing과 quadratic probing 동작 >

<br>


### Double hashing

- Hash func을 두 개 사용해서 빈 칸을 찾는다
- f(k) → f(k) + g(k) → f(k) + 2g(k) → f(k) +3g(k)
- Linear porbing보다 좋지만 Hash func이 두 개 필요하고 연산도 두 번 해야 한다는 단점이 있다

<br><br>

## Chaining

- 하나의 슬롯에 한방향 연결 리스트를 만들어 여러개의 아이템 저장하는 방식

<img width="245" alt="image" src= 'https://user-images.githubusercontent.com/83294376/218035280-24fcd4d0-40b0-4658-b0cc-0cfd20abec51.png'>

<br>

### 삽입 연산 - 시간 복잡도

- f(k) = k % 10 이라고 했을 때 set(23)을 해준다고 가정하면 f(k) = 3이다.
- 이때 23을 저장해주기 위해 한방향 연결리스트인 pushfront(23)을 해준다.
- 그러면 head 노드는 23을 가리키고 23의 next는 13을 가리키게 된다.
- **pushfront = O(1)**이기에 **Chaining의 삽입 연산도 O(1)이 된다.**

<img width="245" alt="image" src= 'https://user-images.githubusercontent.com/83294376/218035643-94013551-2f95-4332-b97a-8187d60ae4f8.png'>

<br>

### 탐색 연산, 삭제 연산 - 시간 복잡도

- f(k) = k % 10 이라고 했을 때 search(66)을 해준다고 가정하면 f(k) = 6이다.
- 인덱스 6으로 간 뒤 한방향 연결 리스트의 탐색 연산을 시작한다.
- 한방향 연결 리스트 탐색 연산의 w.c는 충돌한 아이템의 개수 (=연결 리스트의 길이)이기에 **O(충돌 발생 횟수)** 이다.
- 탐색 연산을 시행한 이후 삭제 연산을 해줄 수 있기에 삭제 연산도 마찬가지로 O(충돌 발생 횟수)이다
- **c-universal hash function을 사용**하면 충돌하는 키들의 개수가 상수를 유지하기 때문에 **O(1)**이다
    - c-universal hash func - Pr(f(x) == f(y)) = c/m
![image](https://user-images.githubusercontent.com/83294376/218035904-12b6777c-87f5-4481-9ec2-5d4b200ae7fe.png)


`find_slot(key)`

```python
def find_slot(key):
	return f(key)
```

`set(key, value)`

```python
def set(self, key, value=None):
	h_index = self.fint_slot(key)
	# 한방향 리스트의 search
	linked_node = self.H[h_index].search(key)
	
	if linked_node == None
		self.H[h_index].pushfront(key, value)

	else:
		linked_node.value = value
	
```

`search(key)`

```python
def search(key):
	h_index = find_slot(key)
	linked_node = self.H[h_index].search(key)
	
	if linked_node != None:
		return linked_node.value

	return None
```




