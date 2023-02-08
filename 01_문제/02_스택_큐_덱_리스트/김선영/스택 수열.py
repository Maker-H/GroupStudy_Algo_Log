from collections import deque

import sys
input = sys.stdin.readline

n = int(input())
stack = deque()

arr = deque()                    # input 받아서 수열 덱 만들기
for _ in range(n):
    arr.append(int(input()))

result = []                     # 결과 담을 리스트
for num in range(1, n+1):
    stack.append(num)
    result.append('+')
    while stack and stack[-1] == arr[0]:
        stack.pop()
        result.append('-')
        arr.popleft()
if stack:
    print('NO')
else:
    for value in result:
        print(value)