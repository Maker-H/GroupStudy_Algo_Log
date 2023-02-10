class Stack:
    def __init__(self):
        self.s = [0 for _ in range(100000)]
        self.size = 0
        self.s_max = 100000

    def push(self, val):
        if self.size == self.s_max:
            return
        self.s[self.size] = val
        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        val = self.s[self.size - 1]
        self.size -= 1
        return  val

    def peek(self):
        return self.s[self.size - 1]

    def s_size(self):
        return self.size

IN = list(input())

S = Stack()
cnt = 0
tmp = ''

for c in IN:
    if c == '(':
        S.push(c)
        tmp = '('
    # 전의 값이 ) 면 파이프의 끝
    elif c == ')' and tmp == ')':
        S.pop()
        cnt += 1
        tmp = ')'
    # 전의 값이 ( 면 레이저
    elif c == ')' and tmp == '(':
        S.pop()
        cnt += S.s_size()
        tmp = ')'


print(cnt)