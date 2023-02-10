'''
List는 O(n), deque는 O(1)의 속도를 가짐

a = [1, 2, 3, 4, 5, 6]
a.rotate(2)     # 오른쪽으로 2만큼 밀기
a = [5, 6, 1, 2, 3, 4]


a = [1, 2, 3, 4, 5, 6]
a.rotate(-2)    # 왼쪽으로 2만큼 밀기
a = [3, 4, 5, 6, 1, 2]
'''


from collections import deque

N = int(input())
arr = deque(range(1, N+1))

while len(arr)>1:
    arr.popleft()
    arr.rotate(-1)

print(arr[0])
