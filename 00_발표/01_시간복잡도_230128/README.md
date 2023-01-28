# 자료구조 1회차 - 시간복잡도

## 𝐈𝐧𝐟𝐨

 - 📌 발표자 : 진희솜
 - 🗓️ 2023-01-28
    
### QnA

  1. 피보나치 재귀함수는 왜 O( $2^n$ )인가요?
   
        > <img width="245" alt="image" src="https://user-images.githubusercontent.com/83294376/215259866-8c4392e1-0cfe-4445-8121-1b9d80cdedd8.png">
        > <br> 2번씩 트리의 높이 k만큼 반복하는 형태
        > <br><br> 아래의 알고리즘 설명을 보면 worstcase time complexity로 T(n)을 계산한 후 그 최고차항만을 뽑아 빅오를 계산하는데 피보나치 재귀의 w.t.c는 f(n)이 시행되었을때 f(n-1) + f(n-2)을 시행하는 경우이다. 
        > <br><br> 그러한 관점에서 f(n)은 항상 2^1의 연산을 수행하며 그 결과에 대한 f(n-1)도 2^1 f(n-2)도 2^1을 항상 수행함을 전제로 한다.
        ><br><br>그렇기에 단순히 f(n)+f(n-1)로 생각하면 T(n) = c 2^1로 생각할 수 있지만 실상은 f(n) 안에 또 2번씩 시행되는 함수가 무한히 있는 형태로 트리의 높이인 k만큼 O(2^n)이라고 생각할 수 있는 것이다. 
        ><br><br> 또한 위의 그림은 현실의 연산을 나타낸 것이지만 그 코드가 실제로 실행될지 되지 않을지를 고려하지 않는 w.t.c의 관점에서는 2^1이 재귀적으로 시행되는 연산이 if k <= 1: return k에서 리턴됨으로써 재귀적 2^1이 n번 시행되는 것이기에 모든 f()에서 가지가 뻗어나오는 것이 n번 시행되는, 완벽한 대칭을 이루는 트리가 될 것이다. 
        

</aside>

<br>

---

<br>

### 자료구조란?

저장공간(메모리)와 연산(읽기, 쓰기, 삽입, 삭제, 탐색)으로 구성되어 있음

<br>

### 알고리즘이란?

입력 데이터를 가지고 유한한 횟수의 연산을 통해 원하는 정답을 출력하는 논리적인 절차

<br>

<img width="345" alt="image" src= 'https://user-images.githubusercontent.com/83294376/215258892-106eee8c-b15c-4c41-a19e-35ba4ac4e442.png'>

### 가상컴퓨터 + 가상 언어 + 가상코드 

→ 누구나 같은 환경에서 여러 알고리즘을 객관적으로 비교할 수 있음

<br>

가상코드

- 기본연산으로 구성되어 있음
- 기본 연산 : 단위 시간에 수행되는 연산

<br>

기본연산 (기본 1 단위에 이루어는 연산)

- 배정연산, 대입연산, 복사연산 ⇒ 다 같은 `=` 에 대한 이야기
- 산술연산 + = * /  (강의에서는 % 같은것도 단위시간에 돌아간다고 가정하겠음)
- 비교연산 > ≥ < ≤ == ≠ 비교연산은 a<b 가 아니라 a-b<0로 판별함 빼기 한 번이기에 단위시간에 돌아감
- 논리연산 and, or, not
- 비트연산 bit-and, or, not

<br>

가상언어(pseudo/virtual languages)

- 배정연산, 산술연산, 비교연산, 논리연산 등을 표현할 수 있는 언어면 됨
- 비교제어 명령어 포함해야함 : if, if else
- 반복문 포함해야 함

<br>
<br>

# 시간 복잡도

시간복잡도 구하는 방법

1. 모든 입력에 대해 기본 연산 횟수를 더한 후 평균 내기 (현실적으로 불가능)
2. 가장 안좋은 입력에 대한 기본 연산 횟수를 측정 (기본 연산 횟수를 가장 많이 필요로 하는 입력) - worstcase time complexity 
   - 어떤 입력에 대해서도 w.t.c 보다 수행이 크지 않다
    <img width="245" alt="image" src='https://user-images.githubusercontent.com/83294376/215258928-1ba63616-8715-4caa-b1a8-e7dbc60c5405.png'>

<br>

알고리즘 수행시간 = 최악의 입력에 대한 기본 연산 횟수

<br>
<br>

# 빅오 표기법

worstcase time complexity 채택하기 때문에 N을 무한히 커진다고 가정한다면 그래프는 최고차항에 따라 발산한다. 그렇기에 함수값을 결정하는 최고차항만으로 간단하게 표기

1. 최고차항만 남긴다
2. 최고차항 계수(상수)는 생략한다
3. 표기방식 : BIg O(최고차항)

<br><br>

### O(1)시간 알고리즘

```python
def increment_one(a):
	return a+1
```

<br><br>

### O(logn) - 비트수 계산 알고리즘

```python
def number_of_bits(n):
	count = 0 -> a(=)

	while n > 0:
		n = n // 2 -> b(=), c(//)
		count += 1 -> d(=), e(+)
	
	return count
```

n = $n/2$  (1번째) → n = $n/2^2$(2번째) → n = $n/2^3$ (3번째) → … → n = $n/2^c$ (count번째)
 
<img width="235" alt="image" src='https://user-images.githubusercontent.com/83294376/215259117-3983b8bd-0d3d-49ee-9909-32376686135c.png'>

<br>

→ n = $n/2^c$  이 1이 되면 그 다음에는 break된다 

→ 즉 count번만큼 while문이 돈다고 생각하면 된다

→ 그 count가 $log^n_2$이기 때문에 while도 $log^n_2$만큼 돈다

<br>

T(n) = 4 * $log^n_2$ + 1 = c * $log^n_2$ +1 = O( $log^n_2$ )

<br>

> **log의 밑을 2로 설정한 이유**

<img width="245" alt="image" src='https://user-images.githubusercontent.com/83294376/215259172-8721c7c4-3a9b-4bb8-bc86-b099dd46f565.png'>
    

<br><br>

### O(nlogn)

```python
def number_of_bits(n):
		number = n -> a(=)

		for i = 1 to n-1 do

			while number != 0
				number = number / 2 -> b(=), c(/)
```

while만 보면 

n = $n/2$  (1번째) → n = $n/2^2$(2번째) → n = $n/2^3$ (3번째) → … → n = $n/2^c$ (count번째)

<img width="275" alt="image" src='https://user-images.githubusercontent.com/83294376/215259248-bcd717dd-014b-460f-871c-e9740b67c41c.png'>

<br><br>

### O(n) - 최대값 찾는 알고리즘

```python
algorithm arrayMax(A, n)
	currentMax = A[0] ->a(=)
	
	for i = 1 to n-1 do
		if currentMax < A[i]: ->b(<)
			currentMax = A[i] ->c(=)

	return currentMax
```

(b, c) * n-1 + a = 2n -1번 수행됨

알고리즘 수행시간:T(n) = 2n - 1 = O(n)이 됨

<br><br>

### O( $n^2$ ) - 두 배열 곱의 합을 계산하는 알고리즘

```python
algorithm sum2(A, n):
	sum = 0 -> a(=)
	for i = 0 to n-1 do 
		for j = i to n-1 do
				sum += A[i] * A[j] 
				-> c(*), d(+), e(=)

	return sum
```

T(n) = $n(n+1)/2$ * (c, d, e) + a 

<br>

<img width="245" alt="image" src='https://user-images.githubusercontent.com/83294376/215259452-1319c601-fb35-4e57-8c8d-a6da78b99d4c.png'>

→ 반복문 총 $n(n+1)/2$ 번 돈다

<br>

<img width="245" alt="image" src='https://user-images.githubusercontent.com/83294376/215259480-4d43fb04-8dc9-4c82-aedb-68a9d6cb5d3a.png'>

<br><br>

### O( $n^3$ ) - 2차원 행렬의 곱을 계산해 행렬 c를 리턴하는 알고리즘

```python
algorithm sum3(A, B, n):
	C = [n][n]
	for i = 1 to n do 
		for j = 1 to n do
			for k = 1 to n do
				C[i][j] += A[i][k] * B[k][j] 

	return sum
```

T(n) = $3n^3$ +1 = O( $n^3$ )

<br><br>

### O( $2^n$ ) - 피보나치 수 계산하는 재귀 알고리즘

```python
algorithm fibonacci(k):
	if k <= 1: return k

	return fibonacci(k-1) + fibonacci(k-2)
```

T(n) = c $2^n$ = O( $2^n$ )


<br><br>


<img width="345" alt="image" src='https://user-images.githubusercontent.com/83294376/215259518-e347bee6-c60d-46c6-9232-80f976986662.png'>