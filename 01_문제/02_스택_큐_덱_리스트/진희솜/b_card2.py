from sys import stdin

class my_Dequeue:
    def __init__(self):
        self.d = [0 for _ in range(500001)]
        self.d_len = 500001
        self.d_size = 0
        self.start = 0
        self.end = 0

    def push_top(self, val):
        if self.d_size == self.d_len:
            pass
        elif self.d_size != self.d_len:
            self.d[self.end] = val
            self.d_size += 1
            # 넣고 나서 항상 그 다음을 가리킨다
            self.end += 1
    
    def push_bottom(self, val):
        if self.d_size == self.d_len:
            pass
        # start는 end와 다르게 아이템이 있는 자리를 가리킨다
        # 덱에 아이템이 있으면 뒤로 가서 넣어줘야 한다
        else:
            self.start = (self.start - 1 + self.d_len) % self.d_len
            self.d[self.start] = val
            self.d_size +=1
        # 덱에 아이템 없으면 0에 넣어줘도 된다 
        # 다만 이 때 start는 항상 아이템이 있는 자리를 가리키기 때문에 뒤로 밀어주지 않는다

        
    def pop_bottom(self):
        if self.d_size != 0:
            val = self.d[self.start]
            self.start = (self.start + 1) % self.d_len
            self.d_size -= 1
            return val
    
    def pop_top(self):
        if self.d_size != 0:
            self.end = (self.end - 1 + self.d_len) % self.d_len
            val = self.d[self.end]
            self.d_size -= 1
            return val

        
            
    def size(self):
        return self.d_size
    
    def bottom(self):
        return self.d[self.start]
    
    def top(self):
            return self.d[(self.end - 1 + self.d_len) % self.d_len]


    

N = int(stdin.readline())
D = my_Dequeue()

for card in range(1, N+1):
    D.push_bottom(card)

while True:
    if D.size() == 1:
        break

    D.pop_top()
    val = D.pop_top()
    D.push_bottom(val)

    
print(D.top())
