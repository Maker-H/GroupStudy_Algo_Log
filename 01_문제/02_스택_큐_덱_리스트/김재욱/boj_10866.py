import sys 
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

n = int(input())
dq = deque()
for _ in range(n) :
    
    com, *num = input().split() # 명령어와 숫자 따로 받기
    
    if com == "push_front" : # 정수 X를 덱의 앞에 넣는다
        dq.appendleft(int(num[0]))
    elif com == "push_back" : # 정수 X를 덱의 뒤에 넣는다
        dq.append(int(num[0]))
    elif com == "pop_front" : # 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다
        print(dq.popleft() if len(dq)>0 else -1)
    elif com == "pop_back" :
        print(dq.pop() if len(dq)>0 else -1) # 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif com == "size" : # 덱에 들어있는 정수의 개수를 출력한다.
        print(len(dq))
    elif com == "empty" : # 덱이 비어있으면 1을, 아니면 0을 출력한다.
        print(1 if len(dq) ==0 else 0)
    elif com == "front" : # 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        print(dq[0] if len(dq)>0 else -1)
    elif com == "back" : # 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        print(dq[-1] if len(dq)>0 else -1)