from sys import stdin

class heap():
    def __init__(self, N):
        self.H = [0] * N
        self.size = 0

    def insert(self, val):
        self.H[self.size] = val
        self.heapify_up(self.size)
        self.size += 1

    
    def heapify_up(self, idx):
        if idx == 0:
            return
        
        parent_idx = (idx - 1) // 2

        # 루트까지 올라가기
        while parent_idx >= 0:
            if self.H[parent_idx] < self.H[idx]:
                self.H[parent_idx], self.H[idx] = self.H[idx], self.H[parent_idx]
                idx = parent_idx
                parent_idx = (idx - 1) // 2
            # 부모가 더 크면 더 올라가지 않아도 된다
            elif self.H[parent_idx] >= self.H[idx]:
                return
            
    

    # 제일 큰 값을 반환하고 지운다
    def delete_max(self):
        if self.size == 0:
            return 0
        h_max = self.H[0]
        
        self.H[0] = self.H[self.size - 1]
        self.size -= 1
        self.heapify_down(0, self.size)
        return h_max

    
    def heapify_down(self, idx, h_len):
        if self.size == 0:
            return
        
        child_idx = idx * 2 + 1

        while child_idx < h_len:
            
            current_val = self.H[idx]

            # 왼쪽 오른쪽 비교
            if self.H[child_idx+1] > self.H[child_idx]:
                child_idx += 1

            # 제일 큰 자식이랑 부모 비교 
            if current_val >= self.H[child_idx]:
                return
            elif current_val < self.H[child_idx]:            
                self.H[child_idx], self.H[idx] = self.H[idx], self.H[child_idx]
                idx = child_idx
                child_idx = idx * 2 + 1


N = int(stdin.readline())
H = heap(N)

for _ in range(N):
    I = int(stdin.readline())

    if I == 0:
        print(H.delete_max())
    elif I != 0:
        H.insert(I)