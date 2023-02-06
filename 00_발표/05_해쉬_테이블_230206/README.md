# 자료구조 5회차 - 해쉬 테이블

## 𝐈𝐧𝐟𝐨

- 📌 발표자 : 구본재
- 🗓️ 2023-02-06

### QnA


<br><br>


Q : 발표자료에 해시테이블 삽입,삭제,탐색 연산의 시간복잡도를 O(n)이라고 적어 놓으셨는데 제가 알기로는 해시테이블의 시간복잡도는 O(1)이다 어느 쪽이 맞는것 같나 ?
A : 결론적으로 말하면 해시테이블의 시간복잡도는 O(1)이 맞다. 그런데 이 값은 테이블에서 데이터가 차지하는 정도인 Load factor를 일정하게 유지 시켜주는 방법과 C-universal등의 Collision resolution method들을 통해서 개선이 이루어졌을 때 이뤄진다. 

+ 파이썬의 경우에 데이터가 3/2정도 테이블에 채워지면 슬롯을 2배로 늘려 빈 공간을 3/1이상으로 유지한다.

# 2월 6일 자료구조 발표 자료

# Hash Table

: 해시 테이블은 일종의 사전(dictionary)이고 Python의 dict 자료구조처럼 다음 연산을 빠르게 지원한다. (데이터 아이템(item)은 key값과 value값 쌍으로 구성된다고 가정) 

- Hash Table은 매우 빠른 평균 삽입, 삭제, 탐색 연산을 제공한다.


![%ED%95%B4%EC%8B%9C%ED%85%8C%EC%9D%B4%EB%B8%941](https://user-images.githubusercontent.com/123693844/216985129-93266d3a-4921-4ef1-be1a-0c215e8f7aca.png)
                                                 < Hash table 동작 >


**필요한 메소드**

- insert(key, value) # 삽입 : O(n)
- remove(key) # 삭제 : O(n)
- serch(key) # 탐색 : O(n)

해시 테이블은 보통 정보를 담아 저장할 수 있는 테이블 형태로 구현하며 정보(key)가 저장될 슬롯(slot) 번호를 계산하는 함수 f(x)를 **해시 함수(hash function)**이라 한다. 

### 해시 함수(hash function)

해시 함수를 사용해야 하는데 key 값이 정수가 아니라 해시 함수를 사용할 수 없는 경우

- key값을 정수에 대응 시키는 prehash함수를 정의하고 사용하여 변환 후 해시 함수를 사용한다.
- Python에 내장된 hash(x) 함수는 x를 정수로 대응 시키는 prehash함수이며 __hash__를 통해서 지정할 수 있다.

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

### 좋은 해시 함수의 조건

1. **적은 충돌**
2. **빠른 연산**

# 충돌 회피 방법 (Collision resolution method)

### **open addressing**

: 충돌이 발생하면 그 다음 슬롯을 차례로 탐색하면서 가장 먼저 찾은 빈 슬롯에 저장하는 방법



![%ED%95%B4%EC%8B%9C%ED%85%8C%EC%9D%B4%EB%B8%943](https://user-images.githubusercontent.com/123693844/216985212-bf1a6c1e-27c3-40ca-8173-2a996439e2db.png)
                                        < open addressing search 동작 >


**필요한 연산**

- set
- find_slot
- search
- remove

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


![%ED%95%B4%EC%8B%9C%ED%85%8C%EC%9D%B4%EB%B8%944](https://user-images.githubusercontent.com/123693844/216985392-9afeef6b-48b4-423d-b274-2657cee4c782.png)

                                   < Open addressing remove 동작 >


**open addressing의 종류** 

- linear probing
- quadratic probing
- double hashing

**linear probing**은 클러스터 길이를 증가 시키고 연산 속도는 클러스터 길이에 비례함으로 데이터가 증가 할 수록 연산 속도가 반비례로 감소함으로 좋은 방법은 아니다.

*클러스터 : 연속적인 데이터 집합

**quadratic probing** : k → k+1^2 → k+2^2 → k+3^2 순서로 삽입, 삭제, 탐색 연산을 수행한다.

클러스터가 분할해서 생성됨으로 linear보다는 연산 속도가 감소하는 정도가 적다. 

 **double hashing** : hash fun f와 g 두 가지를 준비해서 f(key)+g(key) → f(key)+2*g(key) → f(key)+3*g(key) 순으로 삽입, 삭제, 탐색 연산을 수행한다.


![%ED%95%B4%EC%8B%9C%ED%85%8C%EC%9D%B4%EB%B8%945](https://user-images.githubusercontent.com/123693844/216985558-9bf36dc5-9748-42cc-9e63-14aed271779b.png)


**cluster size**는 hash function, collision resolution method, load factor에 영향을 받는다. 

연산 속도는 cluster size에 반 비례한다.

**Load factor**는 전체 테이블 크기에서 데이터가 차지하는 공간의 비를 말하며 Load factor의 값이 1에 가까워 질 수록(데이터가 차지하는 공간이 증가 할 수록) 연산 속도가 감소한다. 


![%ED%95%B4%EC%8B%9C%ED%85%8C%EC%9D%B4%EB%B8%946](https://user-images.githubusercontent.com/123693844/216985623-d13a0388-581e-41e0-9f5e-dc337cc33743.png)
                                    <Load factor에 따른 수행시간 그래프 >


그래서 **Load factor**를 일정하게 범위 안에서 유지하기 위해서 테이블의 크기를 일정한 값이 되면 2배로 늘려주는 방법을 사용하기도 하며, 보통 데이터가 50% 이하 공간을 점유하도록 유지하면 연산 속도는 O(1)을 가진다.  


![%ED%95%B4%EC%8B%9C%ED%85%8C%EC%9D%B4%EB%B8%947](https://user-images.githubusercontent.com/123693844/216985703-11adfae3-57ee-4984-8732-c8c01584e504.png)
                           < Load fator 특정값으로 유지 시 각 cluster의 연산속도는 O(1)> 


## **chaining**

: Table에 slot에 값을 하나만 저장하도록 하는 게 아니라, 각 slot마다 연결 리스트를 연결해, 슬롯 하나 당 이론적으로 무한히 많은 값들을 저장하도록 하는 방법


![%ED%95%B4%EC%8B%9C%ED%85%8C%EC%9D%B4%EB%B8%948](https://user-images.githubusercontent.com/123693844/216985880-63007e5d-1a0f-4c52-82c3-e827b62c7432.png)


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
				return self.H[i].remove(v) # 비효율적
```

**C-universal** and **Loaf factor 0.5** 이하 유지 

⇒ 상수 시간 내에 삽입, 삭제, 탐색 연산이 가능하다.

