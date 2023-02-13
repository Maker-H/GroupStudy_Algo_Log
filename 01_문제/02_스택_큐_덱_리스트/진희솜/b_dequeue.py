from sys import stdin

class Dequeue:
    def __init__(self):
        self.d = [0 for _ in range(10005)]
        self.d_len = 10005
        self.d_size = 0
        self.start = 0
        self.end = 0

    def push_back(self, val):
        if self.d_size == self.d_len:
            return
        self.d[self.end] = val
        self.end = (self.end + 1) % self.d_len
        self.d_size += 1

    def push_front(self, val):
        if self.d_size == self.d_len:
            return
        self.start = (self.start - 1 + self.d_len) % self.d_len
        self.d[self.start] = val
        self.d_size += 1

    def pop_front(self):
        if self.d_size == 0:
            return -1
        else:
            val = self.d[self.start]
            self.start = (self.start + 1) % self.d_len
            self.d_size -= 1
            return val

    def pop_back(self):
        if self.d_size == 0:
            return -1
        else:
            self.end = (self.end - 1 + self.d_len) % self.d_len
            val = self.d[self.end]
            self.d_size -= 1
            return val 

    def size(self):
        return self.d_size
    
    def empty(self):
        return 1 if self.d_size == 0 else 0

    def front(self):
        if self.d_size == 0:
            return -1
        return self.d[self.start]

    def back(self):
        if self.d_size == 0:
            return -1
        return self.d[self.end - 1]
    
def len(n_l):
    n = 0
    for one in n_l:
        n += 1
    return n

T = int(stdin.readline())
D = Dequeue()
for _ in range(T):
    cmd = stdin.readline().split()
    val = 0

    if len(cmd) == 1:
        cmd = cmd[0]
    else:
        cmd, val = cmd[0], int(cmd[1])

    if cmd == 'push_back':
        D.push_back(val)
    elif cmd == 'push_front':
        D.push_front(val)
    elif cmd == 'front':
        print(D.front())
    elif cmd == 'back':
        print(D.back())
    elif cmd == 'pop_front':
        print(D.pop_front())
    elif cmd == 'pop_back':
        print(D.pop_back())
    elif cmd == 'size':
        print(D.size())
    elif cmd == 'empty':
        print(D.empty())


