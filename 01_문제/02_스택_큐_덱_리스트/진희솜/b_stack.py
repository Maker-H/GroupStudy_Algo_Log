from sys import stdin

class Stack:
    def __init__(self):
        self.stack = [0 for _ in range(10001)]
        self.stack_size = 0

    def push(self, value):
        self.stack[self.stack_size] = value
        self.stack_size += 1
    
    def pop(self):
        if self.empty():
            return -1
        
        value = self.stack[self.stack_size - 1]
        del self.stack[self.stack_size - 1]
        self.stack_size -= 1

        return value
    
    def size(self):
        return self.stack_size

    def empty(self):
        if self.stack_size == 0:
            return 1
        return 0
    
    def top(self):
        if self.stack_size == 0:
            return -1
        return self.stack[self.stack_size - 1]

N = int(stdin.readline())
S = Stack()

for tc in range(N):
    cmd = stdin.readline().split()
    
    # push만
    if len(cmd) == 1:
        cmd = cmd[0]
    else:
        cmd, num = cmd[0], int(cmd[1])

    if cmd == 'push':
        S.push(num)
    # pop, stack_size, empty, top
    elif cmd == 'pop':
        print(S.pop())
    elif cmd == 'size':
        print(S.size())
    elif cmd == 'empty':
        print(S.empty())
    elif cmd == 'top':
        print(S.top())

    

