from sys import stdin

class Stack:
    def __init__(self):
        self.s = [0] * 55
        self.size = 0
        self.s_max = 55

    def push(self, val):
        if self.size == self.s_max:
            return -1
        self.s[self.size] = val
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1
        val = self.s[self.size - 1]
        self.size -= 1
        return val

    def s_size(self):
        return self.size


T = int(stdin.readline())

for tc in range(T):
    IN = list(stdin.readline().strip())

    S = Stack()

    for c in IN:
        if c == '(':
            S.push(c)
        if c == ')':
            val = S.pop()
            if val == -1:
                break


    if S.s_size() == 0 and val != -1:
        print('YES')
    else:
        print('NO')