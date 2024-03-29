# 자료구조 12회차 - 리스트,딕셔너리

## 𝐈𝐧𝐟𝐨

- 📌 발표자 : [@jongwook123](https://github.com/jongwook123)
- 🗓️ 2023-03-22

#### 

# Dictionary

### Dictionary

1. dict는 key 값과 value 값의 쌍을 저장하는 자료구조

```py
D ={}
D[2019317] = "신찬수"
D[2019209] = "홍길동"
# key는 학번 value는 이름
print(D)
# {2019317 : 신찬수" , 2019209 : "홍길동"}
```

2. 해시 테이블 크기
   1. 8개 slot으로 시작, 테이블의 슬롯이 2⁄3 이상 차면 2배씩 슬롯을 늘려 resize 함. 즉, 해시 테이블의 1⁄3 이상은 항상 비어 있도록 유지된다
   2. 2배씩 증가하거나 감소하므로 해시 테이블의 크기는 항상 2^k 유지
3. 해시 함수
   1. 해시 테이블 사이즈가 m = 2^k 이라면, 우선 key 값의 하위 k 비트를 그대로 기본 해시 함수값으로 사용한다 (예: m = 2^4 , f(0) = 0, f(15) = 15, f(16) =0)
   2. key 값이 k 비트보다 크다면, 상위 비트가 함수 값에 반영이 안될 수 있지만, collision resolution에서 반영되도록 설계되어 있다
4. 충돌 회피 방법(open addressing)
   1. Linear Probing : 충돌이 발생했을 때, 그 옆자리가 비었는지 살펴보고, 비었을 경우 그 자리에 대신 저장하는 것이 Linear Probing이다.
      1. 예를들어 key % 7의 해쉬 함수가 있다면 키 9 를 저장할 때 인덱스 2에 저장할 것이다. 이어서 키가 2인 데이터가 등장했을때도 해쉬 값이 2라서 인덱스 2에 저장할 텐데, 충돌이 발생하므로옆자리를 살펴 비어있으므로 인덱스 3에 저장한다. **f(k) + 1** -> **f(k) + 2** -> **f(k) + 3** ...
   2. Quadratic Probing : 충돌의 횟수가 증가함에 따라 클러스터 현상이 발생한다. 즉, 특정 영역에 데이터가 집중적으로 몰리는 단점이 있다. 그 대안으로 나온것이 좀 더 멀리서 빈 공간을 찾자는 아이디어를 가진 Quadratic Probing이다.
      1. **f(k) + 1제곱** -> **f(k) + 2제곱** -> **f(k) + 3제곱**



# List

### Array(배열),List(리스트)

1. 데이터를 연속적인 메모리 공간에 저장하고, 저장된 곳의 주소(address, reference)를 통해 매우 빠른 시간에 접근할 수 있는 가장 많이 쓰이는 기본적인 자료구조
2. C 언어에서의 배열 A
   1. 배열의 시작주소, 저장된 값의 종류, 몇 번째에 저장되어 있는지를 나타내는 인덱스 세가지 정보만으로 값이 저장된 곳의 주소를 계산할 수 있다.
      ex) A[2]의 시작 주소 = A[0]의 시작 주소 + 2*4 (index=2, sizeof(int)=4)
   2. 읽기와 쓰기 연산 : O(1)
   3. 배열은 읽기/쓰기 연산만 제공하는 제한된 자료구조
3. Python 언어에서의 list A
   1. Python리스트의 셀에는 데이터가 아닌 데이터가 저장된 곳의 주소(address 또는 reference)가 저장된다
   2. 항상 객체의 주소만 저장하기 때문에, 리스트의 셀의 크기를 메모리의 주소를 표현할 수 있는 (4 바이트 또는) 8 바이트로 고정하면 된다. 모든 셀의 크기가 같기 때문에 index에 의해 O(1) 시간 접근이 가능하다

### List 연산

- A.append(5)
  
  ```py
  if A.capacity == A.n: # resize 필요!
  		allocate a new list B with larger memory and
  				update B.capacity and B.n
  		for i in range(A.n):
  						B[i] = A[i]
  		dispose A
  		A = B # B 이름을 A로 바꿈
  A[n] = value
  A.n += 1
  
  # resize가 일어나지 않을때 O(1) 일어날때 O(n)
  ```

| 연산                     | 시간복잡도 |
| ---------------------- |:----- |
| A[i] = A[j] +1         | O(1)  |
| A.pop()                | O(1)  |
| A.pop(n)               | O(n)  |
| A.insert(0,10)         | O(n)  |
| A.remove(9)            | O(n)  |
| A.index(9), A.count(9) | O(n)  |
