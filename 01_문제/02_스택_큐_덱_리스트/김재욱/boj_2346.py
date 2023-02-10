import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
_list = list(map(int, input().split()))
ballons = deque()
for idx, l in enumerate(_list): # 풍선의 초기 위치를 알기위해서 enumerate 사용
    ballons.append([idx+1, l])
seq = []
move = ballons.popleft()
seq.append(move[0])
while ballons:
    if move[1] >0: # 풍선안의 숫자가 양수일 때
        for _ in range(move[1]-1):
            ballons.append(ballons.popleft())
        move = ballons.popleft()
        seq.append(move[0])
    else: # 풍선안의 숫자가 음수일 때
        for _ in range(-move[1]-1): 
            ballons.appendleft(ballons.pop())
        move= ballons.pop()
        seq.append(move[0])

print(*seq)