from collections import deque

import sys
input = sys.stdin.readline

n = int(input())                    # n장의 카드
_list = deque()
for num in range(1, n+1):           # 순서대로 카드넣기
    _list.append(num)

while len(_list) > 1:               # 1장의 카드만 남을 때까지
    _list.remove(_list[0])          # 제일 위에 있는 카드를 바닥에 버린다.
    _list.append(_list.popleft())   # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
print(_list[0])