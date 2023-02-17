from sys import stdin


class Queue:
    def __init__(self):
        self.q = [0 for _ in range(105)]
        self.size = 0
        self.start = 0
        self.end = 0
        self.max = 105

    def push(self, val):
        if self.size == self.max:
            return
        self.q[self.end] = val
        self.end = (self.end + 1) % self.max
        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        val = self.q[self.start]
        self.start = (self.start + 1) % self.max
        self.size -= 1
        return val

    def peek(self):
        if self.size == 0:
            return
        return self.q[(self.start - 1 + self.max) % self.max]

    def q_size(self):
        return self.size

    def __str__(self):
        return str(self.q[self.start:self.end])


T = int(stdin.readline())

for test_case in range(T):
    docs_len, target_page = tuple(map(int, stdin.readline().split()))

    tmp = [0 for _ in range(docs_len)]
    tmp = list(map(int, stdin.readline().split()))

    # 제일 높은 중요도 찾기
    imp_max = 0
    for i in tmp:
        if imp_max < i:
            imp_max = i

    original_printer = Queue()
    new_printer = Queue()
    for i in range(0, docs_len):
        original_printer.push((i, tmp[i]))


    original_printer_size = docs_len
    # 중요도에 따라 정렬
    while True:
        none_num = 0
        for _ in range(original_printer_size):
            val = original_printer.pop()

            if val[1] == imp_max:
                new_printer.push(val)
                original_printer.push(None)
                none_num += 1
                original_printer_size -= 1
            elif val[1] < imp_max: 
                original_printer.push(val)
        
        # deleted 이라는 마커 나올때까지 더 돌려준다
        while none_num != 0:
            val = original_printer.pop()
            if val == None:
                none_num -= 1
            else:
                original_printer.push(val)

        imp_max -= 1
        if imp_max == 0:
            break
    

    cnt = 0
    for _ in range(docs_len):
        val = new_printer.pop()
        if val[0] == target_page:
            cnt += 1
            print(cnt)
            break
        else:
            cnt += 1