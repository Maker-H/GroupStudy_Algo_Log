from sys import stdin

class Dequeue:
    def __init__(self):
        self.d = [0] * 1005
        self.d_max = 1005
        self.size = 0
        self.start = 0
        self.end = 0

    # start는 항상 숫자가 들어가야 하는 곳 앞을 가리킨다
    def push_front(self, val):
        if self.size == self.d_max:
            return
        self.start = (self.start - 1 + self.d_max) % self.d_max
        self.d[self.start] = val
        self.size += 1

    def push_back(self, val):
        if self.size == self.d_max:
            return
        self.d[self.end] = val
        self.end = (self.end + 1) % self.d_max
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            return
        val = self.d[self.start]
        self.start = (self.start + 1) % self.d_max
        self.size -= 1
        return val

    def pop_back(self):
        if self.size == 0:
            return
        self.end = (self.end - 1 + self.d_max) % self.d_max
        val = self.d[self.end]
        self.size -= 1
        return val

    def d_size(self):
        return self.size

    def front_peek(self):
        return self.d[self.start]

    def back_peek(self):
        return self.s[(self.end - 1 + self.d_max) % self.d_max]

    def __str__(self):
        return " ".join(list(map(str, self.d[self.start : self.end])))


N = int(stdin.readline())
D = Dequeue()

balloon = list(map(int, stdin.readline().split()))

for idx in range(N):
    D.push_back((idx+1, balloon[idx]))


answer = [0] * 1005
ans_idx = 0
while D.d_size() != 0:
    i, tmp = D.pop_front()
    answer[ans_idx] = i
    ans_idx += 1
    
    # 자연수 pop_front + push_back N-1번
    if tmp > 0:
        if D.d_size() == 0:
            break
        for repeat in range(tmp-1):
            D.push_back(D.pop_front())
    
    # 음수 pop_back + push_front N번
    else:
        if D.d_size() == 0:
            break
        for repeat in range(-tmp):
            D.push_front(D.pop_back())

print(" ".join(list(map(str, answer[:N]))))
