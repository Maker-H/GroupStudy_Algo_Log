from sys import stdin

class min_heap:
    def __init__(self, N):
        self.H = [0] * N
        self.size = 0
        self.N = N

    def insert(self, val):
        # 어차피 정사각형이므로 꽉 차기 전까지는 힙으로 만들 이유 없다
        if self.size < self.N:
            self.H[self.size] = val
            self.size += 1

        # 꽉 차면 처음에 큰 값 넣어주고 위에서 아래로 히피파이 다운한다
        # 시간은 더 걸려도 메모리를 작게 유지해주려면 n번째로 작은 값이 제일 앞으로 와야함
        elif self.size == self.N:
            if val > self.H[0]:
                self.H[0] = val
                self.heapify_down(0)

    def heapify_down(self, idx):
        child_idx = idx*2 + 1

        while child_idx < self.N:
            # 더 작은 자식을 부모랑 비교한다
            if child_idx+1 < self.N and self.H[child_idx+1] < self.H[child_idx]:
                child_idx += 1

            # 부모가 더 크면 바꿔준다
            if self.H[child_idx] < self.H[idx]:
                self.H[child_idx], self.H[idx] = self.H[idx], self.H[child_idx]

            idx = child_idx
            child_idx = (child_idx*2) + 1

    def get_min(self):
        return self.H[0]

    def __str__(self):
        return " ".join(list(map(str, self.H)))

N = int(stdin.readline())

H = min_heap(N)

for _ in range(N):
    arr = list(map(int, stdin.readline().split()))
    for i in arr:
        H.insert(i)

print(H.get_min())

