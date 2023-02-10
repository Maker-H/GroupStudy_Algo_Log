import sys
from collections import deque
sys.stdin = open('풍선터뜨리기_input.txt', 'r')

n = int(input())
arr = list(map(int, input().split()))
balloons = deque()

for idx, num in enumerate(arr):
    balloons.append([idx+1, num])


ans = []
while balloons:
    move = balloons.popleft()
    ans.append(move[0])
    if move[1] > 0:
        balloons.rotate(-move[1]+1)
    elif move[1] < 0:
        balloons.rotate(-move[1])
print(*ans)





