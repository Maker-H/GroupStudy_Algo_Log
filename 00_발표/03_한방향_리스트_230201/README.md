# 자료구조 3회차 - 한방향 리스트

## 𝐈𝐧𝐟𝐨

- 📌 발표자 : 김재욱
- 🗓️ 2023-02-01

### QnA

1. **str** 에서 노드를 호출하면 key를 반환하는데 값은 value에 있는거 아닌가요? Key와 value의 다른점이 뭔지 궁금합니다.
- 모두 값을 갖고 있다는 점에서 차이가 없고 key값은 반드시 있어야하지만 value값은 더 담고 싶은 정보가 없으면 없어도 됩니다.
2. Popback에서 remove랑 다르게 prev와 tail을 먼저 정의하는 이유?
- Popback은 tail node를 찾지만 remove는 키값을 찾아 없애는 과정을 하기 때문에 remove의 경우 앞에서 정의하게 되면 첫번째 노드는 건너뛰고 두번째 노드부터 탐색하기 때문에 뒤에서 정의 해야합니다.
  
<br><br>


## 자료구조 3

# Linked List![LLdrawio](https://user-images.githubusercontent.com/102957590/216055414-52c20fcd-a09e-4b3f-bb40-4ac5d09069b9.png)

- 연결리스트는 노드(node)가 링크(link)에 의해 기차처럼 연결된 순차(Sequential) 자료구조로 링크를 따라 원하는 노드의 데이터를 접근하고 수정한다.
- 노드(node) : 실제 값을 위한 data 정보(보통 key 값을 저장)와 인접 노드를 향하는 link 정보로 구성된 클래스

## 한 방향 연결리스트(singly linked list)

- 노드들이 한쪽 방향으로만(next 링크를 따라) 연결된 리스트
  - 가장 앞에 있는 노드를 특별히 head 노드라 부르고, head 노드를 통해 리스트의
    노드를 접근한다
  - 가장 뒤에 있는 노드는 다음 노드가 없기 때문에 그 노드의 next 링크는 None을
    저장함. 즉, next 링크가 None이라면 그 노드가 마지막 노드임
- Node Class

```python
class Node:
    def __init__(self, key=None, value=None):
        self.key = key # 노드를 다른 노드와 구분하는 key 값
        self.next = None # 다음 노드로의 링크 (초기값은 None)
    def __str__(self): # print(node)인 경우 출력할 문자열
        return str(self.key) # str((self.key, self,value))
```

- 한방향 연결 리스트 클래스

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None # 연결리스트의 가장 앞의 노드 (head)
        self.size = 0 # 리스트의 노드 개수

    def __iter__(self): # generator 정의
        v = self.head 
        while v != None:
            yield v #리턴과 비슷
            v = v.next

    def __str__(self): # 연결 리스트의 값을 print 출력
        return " -> ".join(str(v) for v in self)
        # generator를 이용해 for 문으로 노드를 순서대로
        # 접근해서 join 함 (key 값 사이에 ->를 넣어 출력)

    def __len__(self):
        return self.size # len(A) = A의 노드 개수 리턴
```

- Iterator
  
  - 순서대로 다음 값을 리턴할 수 있는 객체. 자체적으로 내장하고 있는 next 메소드를 통해 다음 값을 가져올 수 있다.
    
    <img src="https://user-images.githubusercontent.com/102957590/216055706-adc1613d-59c1-4347-942d-b9d215ab2bb1.png" title="" alt="다운로드" width="403">

- Generator
  
  - iterator를 생성해주는 함수, 함수안에 yield 키워드를 사용함

```python
>>> def test_generator():
...     yield 1
...     yield 2
...     yield 3
... 
>>> gen = test_generator()
>>> type(gen)
<class 'generator'>
>>> next(gen)
1
>>> next(gen)
2
>>> next(gen)
3
>>> next(gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

- pushFront vs pushBack
  - pushFront : O(1)
  - pushBack : O(n)

```python
    def pushFront(self, key, value=None):
        new_node = Node(key, value)  # 새 노드 생성
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pushBack(self, key, value=None):
        new_node = Node(key, value)
        if self.size == 0:  # empty list
            self.head = new_node  # new_node 가 head가 됨
        else:
            tail = self.head
            while tail.next != None:  # tail 노드 찾기
                tail = tail.next
            tail.next = new_node
        self.size += 1
```

- popFront vs popBack
  - popFront : O(1)
  - popBack : O(n)

```python
    def popFront(self):
        if self.size == 0:  # or len(self)==0
            return None  # return None if it’s empty

        else:
            x = self.head
            key = x.key  # value = x.value
            self.head = x.next
            self.size = self.size - 1
            del x  # delete x from memory
            return key  # or return (key, value)

    def popBack(self):
        if self.size == 0:  # 빈 리스트인 경우
            return None

        else:
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if prev == None:  # 리스트에 노드가 하나만 있는 경우
                self.head = None
            else:  # 리스트에 두 개 이상의 노드가 있는 경우를 각각 처리해야 한다.
                prev.next = tail.next
            key = tail.key
            del tail
            self.size -= 1
            return key  # or return (key, value)
```

- search : O(n)

```python
    def search(self, key):
        v = self.head
        while v != None:
            if v.key == key:
                return v
            v = v.next
        return v
```

- remove : O(n)

```python
def remove(self, key):
   if self.size == 0: # 빈 리스트인 경우
       pass

   else:
       prev, tail = None, self.head
       while tail.next != None:
           if prev == None and tail.key == key: # 제거하는 원소가 head에 있을 때
               self.popFront()
               break
           elif tail.key == key: # 제거하고자하는 원소가 다른곳이 있는 경우
               prev.next = tail.next
               del tail
               self.size -= 1
               break
           prev = tail
           tail = tail.next
```
