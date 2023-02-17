from sys import stdin

class Dequeue:
    def __init__(self):
        self.d = [0 for _ in range(5003)]
        self.d_size = 0
        self.d_len = 5003
        self.end = 0
        self.start = 0
    
    def push_top(self, val):
        if self.d_size == self.d_len:
            return
        self.d[self.end] = val
        # 항상 다음을 가리킨다
        self.end =  (self.end + 1) % self.d_len
        self.d_size += 1

    def push_bottom(self, val):
        if self.d_size == self.d_len:
            return
        self.start = (self.start - 1 + self.d_len) % self.d_len
        self.d[self.start] = val
        self.d_size += 1

    def pop_top(self):
        if self.d_size != 0:
            self.end = (self.end - 1 + self.d_len) % self.d_len
            val = self.d[self.end]
            self.d_size -= 1
            return val
        else:
            return 
    
    def pop_bottom(self):
        if self.d_size != 0:
            val = self.d[self.start]
            self.start = (self.start + 1) % self.d_len
            self.d_size -= 1
            return val
        else:
            return 
        
    def isempty(self):
        return self.d_size == 0
    
N, K = tuple(map(int, stdin.readline().split()))
D = Dequeue()

for idx in range(1, N+1):
    D.push_top(idx)

answer = [0 for _ in range(5003)]
a_idx = 0
while True:
    if D.isempty():
        break
    for idx in range(K-1):
        val = D.pop_bottom()
        D.push_top(val)
    answer[a_idx] = D.pop_bottom()
    a_idx += 1

print(f'<{", ".join(list(map(str, answer[:a_idx])))}>')
