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
    stack.append(num)           # stack에 숫자 push
    result.append('+')          # push이므로 +
    while stack and stack[-1] == arr[0]:    # stack에 숫자가 담겨있고, stack[-1]가 수열[0]이면
        stack.pop()                         # stack에서 pop
        result.append('-')                  # pop이므로 +
        arr.popleft()                       # 수열[0]을 지워서 다음 숫자를 비교
if stack:                                   # 마지막에 stack에 값이 남아있으면 NO
    print('NO')
else:
    for value in result:
        print(value)