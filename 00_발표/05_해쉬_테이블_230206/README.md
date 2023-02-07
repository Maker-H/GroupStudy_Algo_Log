# 자료구조 5회차 - 해쉬 테이블

## 𝐈𝐧𝐟𝐨

- 📌 발표자 : 구본재
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

# 2월 6일 자료구조 발표 자료

<br>

# Hash Table

: 해시 테이블은 일종의 사전(dictionary)이고 Python의 dict 자료구조처럼 다음 연산을 빠르게 지원한다. (데이터 아이템(item)은 key값과 value값 쌍으로 구성된다고 가정) 
- Hash Table은 매우 빠른 평균 삽입, 삭제, 탐색 연산을 제공한다.
</br>

<img width="800px" alt="image" src= 'https://user-images.githubusercontent.com/123693844/217145931-745ec01b-7112-49f6-8347-74bdca457f68.png'>
<br>

### 필요한 메소드

- insert(key, value) # 삽입 : O(n)
- remove(key) # 삭제 : O(n)
- serch(key) # 탐색 : O(n)
</br>
해시 테이블은 보통 정보를 담아 저장할 수 있는 테이블 형태로 구현하며 정보(key)가 저장될 슬롯(slot) 번호를 계산하는 함수 f(x)를 **해시 함수(hash function)**이라 한다. 

<br>
### 해시 함수(hash function)

해시 함수를 사용해야 하는데 key 값이 정수가 아니라 해시 함수를 사용할 수 없는 경우

- key값을 정수에 대응 시키는 prehash함수를 정의하고 사용하여 변환 후 해시 함수를 사용한다.
- Python에 내장된 hash(x) 함수는 x를 정수로 대응 시키는 prehash함수이며 __hash__를 통해서 지정할 수 있다.
</br>
<br>

### 해시 함수의 종류

1. 완전(perfect) 해시 함수 : 슬롯과 key를 1 대 1로 대응 시키는 이상적인 해시 함수
2. c-universal 해시 함수 : 서로 다른 임의의 두 key값 x, y에 대해 prob(f(x) == f(y)) = c/size(H)가 성립하는 함수  :  완전 해시 함수보다 현실적인 해시 함수
3. 자주 사용하는 해시 함수
- Division : f(k) = (k mod p) mod m
- Multiplication : f(k) = ((ak) mod 2w ) >> (w-r)
- Folding : key 값의 digit를 나눠 연산하는 형식
- Mid-squares : key 값을 적당히 연산한 후, 그 결과의 중간 부분을 떼어내 주소로 이용
- Extraction : key 값의 각 파트마다 임의의 digit을 떼어내 연결해 계산
- Additive : key[i]의 단순 합
- Rotating : <<, >> (비트 이동) 연산과 ^(exclusive or) 연산을 반복
- Universal : key값에 모든 digit에  h = ((h*a) + key[i]) % p 연산을 수행한 후 h % m
</br>

### 좋은 해시 함수의 조건

1. **적은 충돌**
2. **빠른 연산**
</br>

## 충돌 회피 방법 (Collision resolution method)

### **open addressing**

: 충돌이 발생하면 그 다음 슬롯을 차례로 탐색하면서 가장 먼저 찾은 빈 슬롯에 저장하는 방법

<img src='https://user-images.githubusercontent.com/123693844/216984027-8df88b95-92e6-4059-8233-e21ceeca04d1.png' width = 500>
                                    <open addressing search 동작 >
<br>

**필요한 연산**

- set
- find_slot
- search
- remove
</br>


**open addressing method psudo code** 

```python
def set(key, value=None): 
    i = find_slot(key) 
    if i == FULL: # find_slot의 결과 FULL이 리턴되면 가득차서 넣을 수 없음        return None 
    if H[i] is occupied: # key값이 존재하면 기존 값 수정 
        H[i].value = value # value 값 update 후 리턴 
    else: # H[i]가 비어있는 경우, 즉 key가 없다면 새로 저장 H[i].key = key 
        H[i].value = value 
    return key

def find_slot(key): 
    i = f(key) 
    start = i 
    while ( H[i] is occupied ) and ( H[i].key ≠ key ): 
        i = (i + 1) % m    # 비어있거나 key를 찾은경우 그 테이블의 위치 i를 리턴
        if i == start: return FULL 
    return i

def remove(key): 
    i = find_slot( key ) 
    if H[i] is unoccupied: # 비어 있으면 None을 반환
        return None 
    j = i 
    while True: 
        mark H[i] as unoccupied 
        while True 
		        j = (j+1) % m # 테이블 아래로 이동
		        if H[j] is unoccupied: # 비어 있으면 key값을 반환 
		            return key  
		        k = f(H[j].key) # 아래로 이동하면서 만난 키들의 테이블 대응 값
		        # 아래 세 가지 경우의 k인 경우 이동 
		        # | i..(k)..j | 
		        # |...j..i..(k)..| or|..(k)..j..i..| 
		        if (i <k<= j or j <i< k or \ k <= j < i): 
		            break # if 조건문의 의미 : 해시테이블이 원형 리스트와 같기 때문에 i > j일 수도
                      # 있으므로, ..j..i..k.. 순서라거나, ..k..j..i..인 경우에도 같은 이유로 옮기면 안된다
                      # 원형 리스트임으로 i k j 순서가 되면 k가 이동가능  

        H[i] = H[j] # H[j]를 H[i]로 이동 
        i = j

def search(key): 
    i = find_slot(key) 
    if H[i] is occupied: # key is in table 
        return H[i].value 
    else: # key is not in table 
        return None # not found
```

<img src = https://user-images.githubusercontent.com/123693844/216984101-c4d383e3-3d2f-4cd3-a01c-56c09e1fa2c1.png width = 800 >
                                 < Open addressing remove 동작 >


<img src = https://user-images.githubusercontent.com/123693844/217253728-f077b427-748a-4ff5-883b-d1e5946f2507.png width = 500 >
                                  < k가 i위치로 이동 가능한 경우 >

<br>
					  
remove method에서는 key값을 찾기 위해서 에서 알맞은 위치로 조정하는 작업을 하는데 그중 탐색중인 위치의 해쉬함수 대응값(k)가 이동 할 수 있는 경우는 위 그림을 보면 i k j / j i k / k j i로 세가지가 존재 한다. 하지만 이것들은 실제로는 한 가지이다. 테이블도 원형구조를 가지기에 마지막이 처음과 연결되어 있기 때문이다. 따라서 위 3가지 경우는 동일한 경우이며 i와 j 사이에 k가 있어야 이동 가능함을 알 수 있다.

</br>
					 
<br>

**open addressing의 종류** 

- linear probing
- quadratic probing
- double hashing

**linear probing**은 클러스터 길이를 증가 시키고 연산 속도는 클러스터 길이에 비례함으로 데이터가 증가 할 수록 연산 속도가 반비례로 감소함으로 좋은 방법은 아니다.

</br>

<br>
클러스터 : 연속적인 데이터 집합

**quadratic probing** : k → k+1^2 → k+2^2 → k+3^2 순서로 삽입, 삭제, 탐색 연산을 수행한다.

클러스터가 분할해서 생성됨으로 linear보다는 연산 속도가 감소하는 정도가 적다. 

 **double hashing** : hash fun f와 g 두 가지를 준비해서 f(key)+g(key) → f(key)+2*g(key) → f(key)+3*g(key) 순으로 삽입, 삭제, 탐색 연산을 수행한다.

<img src = https://user-images.githubusercontent.com/123693844/216984233-8aad6e2d-b3c9-49a7-b768-317c14d141af.png width = 800 >
                                            < linear probing과 quadratic probing 동작 >

**cluster size**는 hash function, collision resolution method, load factor에 영향을 받는다. 

연산 속도는 cluster size에 반 비례한다.

**Load factor**는 전체 테이블 크기에서 데이터가 차지하는 공간의 비를 말하며 Load factor의 값이 1에 가까워 질 수록(데이터가 차지하는 공간이 증가 할 수록) 연산 속도가 감소한다. 
</br>

<imag src =https://user-images.githubusercontent.com/123693844/216984281-59a98ffc-b206-42c1-84f1-882d70697a83.png width = 800 >
                                             <Load factor에 따른 수행시간 그래프 >

그래서 **Load factor**를 일정하게 범위 안에서 유지하기 위해서 테이블의 크기를 일정한 값이 되면 2배로 늘려주는 방법을 사용하기도 하며, 보통 데이터가 50% 이하 공간을 점유하도록 유지하면 연산 속도는 O(1)을 가진다.  

<imag src = https://user-images.githubusercontent.com/123693844/216984368-a2505fc3-b5f4-4e6a-95ef-10a64abe9162.png width = 800 >
                               < Load fator 특정값으로 유지 시 각 cluster의 연산속도는 O(1)> 

<br>				       
				       
## **chaining**

: Table에 slot에 값을 하나만 저장하도록 하는 게 아니라, 각 slot마다 연결 리스트를 연결해, 슬롯 하나 당 이론적으로 무한히 많은 값들을 저장하도록 하는 방법

</br>
	
<imag src = https://user-images.githubusercontent.com/123693844/216984413-f8d0a02e-11ea-4f7d-b2f2-6625cc599f1a.png width = 800 >
                                                  < chaining 동작 > 
				       
**chaining method psudo code** 

```python
class HashChain: 
		def __init__(self, m): 
				self.size = m 
				self.H = [SinglyLinkedList() for _ in range(m)]

def find_slot(self, key): 
				return self.hash_function(key) # chaining의 경우 무조건 존재한다면 그자리 에 있음으로 키값을 해시함수 처리한 값을 리턴해준다.

def set(self, key, value=None): 
		i = self.find_slot(key) # key값에 대응되는 슬롯 값 
		v = self.H[i].search(key) # key값이 해당 슬롯 연결 리스트에 있는지 탐색해서 있다면 value 없다면 None
		if v == None: # key 값 노드 없다면 삽입연산 
				self.H[i].pushFront(key, value) 
		else: # 기존의 key값을 있으므로 value값 수정연산 
				v.value = value

def search(key): 
    i = find_slot(key) 
    if H[i] is occupied: # key is in table 
         v = self.H[i].head # H[hash_function(key)] 연결 리스트를 탐색하여 있다면, value 값을 없다면 None을 리턴한다
         while v != None:
            if v.key == key :
                return v.value
            v = v.next 
            return v # 마지막까지 없으면 None을 반환

def remove(self, key): 
		i = self.find_slot(key) 
		v = self.H[i].search(key) 
				return self.H[i].remove(v) # 효율적인 코드 아님
```
<br>
							  
**C-universal** and **Loaf factor 0.5** 이하 유지 

⇒ 상수 시간 내에 삽입, 삭제, 탐색 연산이 가능하다.

 </br>
