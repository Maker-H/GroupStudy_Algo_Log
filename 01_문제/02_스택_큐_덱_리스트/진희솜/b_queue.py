from sys import stdin

class Queue:
    def __init__(self):
        self.q = [0 for _ in range(2000001)]
        self.end = 0
        self.start = 0
        self.q_size = 0
    
    def push(self, val):
        self.q[self.end] = val
        self.q_size += 1
        self.end += 1
    
    def pop(self):
        if self.q_size == 0:
            return -1

        val = self.q[self.start]
        self.start += 1
        self.q_size -= 1
        
        return val

    def size(self):
        return self.q_size

    def empty(self):
        if self.q_size == 0:
            return 1
        return 0
    
    def front(self):
        if self.q_size == 0:
            return -1
        return self.q[self.start]
    
    def back(self):
        if self.q_size == 0:
            return -1
        return self.q[self.end - 1]

N = int(stdin.readline())
Q = Queue()

for tc in range(N):
    cmd = list(stdin.readline().split())
    
    if len(cmd) == 2:
        cmd, num = cmd[0], cmd[1]
    else:
        cmd = cmd[0]
    
    if cmd == 'push':
        Q.push(num)
    elif cmd == 'pop':
        print(Q.pop())
    elif cmd == 'size':
        print(Q.size())
    elif cmd == 'empty':
        print(Q.empty())
    elif cmd == 'front':
        print(Q.front())
    elif cmd == 'back':
        print(Q.back())
    
