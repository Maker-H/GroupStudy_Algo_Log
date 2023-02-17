from sys import stdin

class Stack:
    def __init__(self):
        self.s = [0 for _ in range(101)]
        self.s_size = 0
        
    def push(self, val):
        self.s[self.s_size] = val
        self.s_size += 1

    def pop(self):
        if self.s_size == 0:
            return
        else:
            self.s_size -= 1
            return self.s[self.s_size]
    
    def size(self):
        return self.s_size
    
    def peek(self):
        if self.s_size == 0:
            return None
        return self.s[self.s_size - 1]

S = Stack()
N = int(stdin.readline()) # 피연산자 개수
prefix = list(stdin.readline().replace('\n', ''))


# 알파벳을 숫자로 바꾸기
for alpha in range(ord('A'), ord('A') + N):
        u_input = stdin.readline().replace('\n', '')
        for idx in range(len(prefix)):
            if prefix[idx] == chr(alpha):
                prefix[idx] = u_input


pre_len = len(prefix)
for c in prefix:

    if c.isdigit():
        S.push(int(c))

    elif c == '*':
        a = S.pop()    
        b = S.pop()
        S.push(b * a)
    
    elif c == '-':
        if S.size == 1:
            a = S.pop()
            S.push(-a)
            break
        a = S.pop()    
        b = S.pop()
        S.push(b - a)
    
    elif c == '/':
        a = S.pop()    
        b = S.pop()
        S.push(b / a)
    
    elif c == '+':
        if S.size == 1:
            a = S.pop()
            S.push(+a)
            break
        a = S.pop()    
        b = S.pop()
        S.push(b + a)
        
    pre_len -= 1


print(f'{S.peek():.2f}')

    

