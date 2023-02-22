def binary(L,M,R,C): # L : left, M : parent, R : right, C : 단계
    global ans
    if C == 1: # 리프 노드 일 때
        ans[K-1].append(L[0]) 
        ans[K-1].append(R[0])
        ans[K-2].append(M)
    else:
        _len = 2**C-1
        ans[K-C-1].append(M)
        binary(L[:_len//2],L[_len//2],L[_len//2+1:],C-1)
        binary(R[:_len // 2], R[_len // 2], R[_len // 2 + 1:], C - 1)


K = int(input())
nums = list(map(int,input().split()))
_len = 2**K-1
ans = [[] for _ in range(K)]
binary(nums[:_len//2],nums[_len//2],nums[_len//2+1:],K-1)
for a in ans:
    print(*a)