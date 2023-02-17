from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    command = list(input())
    n = int(input())
    nums = deque(input().rstrip()[1:-1].split(","))
    count = 0
    if n==0:
        nums = deque()
    for com in command:
        if com == 'R': # R이 나올때마다 뒤집으면 시간초과 발생
            count += 1
        elif com == 'D':
            if nums: 
                if count % 2 == 1: # 카운트가 홀수이면 뒤집어져 있는 상태이므로 오른쪽 pop
                    nums.pop()
                else:
                    nums.popleft() # 카운트가 짝수이면 원래 상태이므로 왼쪽 pop
            else:
                print('error')
                break

    else:
        if count % 2 ==1: # 카운트가 홀수이면 뒤집어줌
            nums.reverse()
        print('[' + ','.join(nums)+']')