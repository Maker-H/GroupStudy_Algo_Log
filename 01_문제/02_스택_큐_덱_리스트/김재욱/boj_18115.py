from collections import deque

n = int(input())
commands = list(map(int, input().split()))
commands.reverse() # 명령어 뒤에서부터 보기
dq = deque()
num = 1
for com in commands:
    if com == 1: # 가장 위의 것을 빼기 때문에 appendleft()
        dq.appendleft(num)
        num+=1
    elif com == 2: # 두번째 것을 빼기 때문에 두번째에 삽입
        dq.insert(1,num)
        num+=1
    else: # 가장 밑의 것을 빼기 때문에 append()
        dq.append(num)
        num+=1

print(*dq)