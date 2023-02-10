import queue
import sys

input = lambda : sys.stdin.readline().rstrip()
n = int(input())
q = queue.Queue()
for _ in range(n) :
    com, *num = input().split() # 명령어와 숫자 따로 받기
    if com == "push": # push일 때
        q.put(int(num[0]))
    elif com == "pop": # pop일 때
        print(q.get()if not q.empty() else -1)
    elif com == "size" : # size일 때
        print(q.qsize())
    elif com == "empty" : # empty일 때
        print(1 if q.empty() else 0)
    elif com == "front": # front일 때
        print(q.queue[0] if not q.empty() else -1)
    elif com == "back" : # back일 때
        print(q.queue[-1] if not q.empty() else -1)