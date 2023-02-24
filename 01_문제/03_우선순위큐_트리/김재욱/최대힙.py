class Heap: # 힙 구현
    def __init__(self, L = []):
        self.A = L

    def heapify_down(self, k, n):
        while 2 * k + 1 < n:  
            L, R = 2 * k + 1, 2 * k + 2  
            if self.A[L] > self.A[k]:
                m = L
            else:
                m = k
            if R < n and self.A[R] > self.A[m]:
                m = R
            # m = A[k], A[L], A[R] 중 최대값의 인덱스
            if m != k:  # A[k]가 최대값이 아니면 힙 성질 위배
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else:
                break

    def heapify_up(self, k):
        while k > 0 and self.A[(k - 1) // 2] < self.A[k]:
            self.A[k], self.A[(k - 1) // 2] = self.A[(k - 1) // 2], self.A[k]
            k = (k - 1) // 2  # 부모 노드

    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A) - 1)

    def delete_max(self):
        if len(self.A) == 0: return 0
        key = self.A[0]
        self.A[0], self.A[len(self.A) - 1] = self.A[len(self.A) - 1], self.A[0]
        self.A.pop()
        self.heapify_down(0, len(self.A))  # len(A) = n-1
        return key


heap = Heap()
n = int(input())
ans = []
for _ in range(n):
    com = int(input())
    if com == 0: # 0이면 최대값
        if heap:
            ans.append(heap.delete_max())
    else:
        heap.insert(com) # 그외의 값이면 insert
for a in ans:
    print(a)