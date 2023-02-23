def inorder(current):
    global cur
    if tree[current][0] != -1:
        # 레벨 설정 후 다시 순회
        level[tree[current][0]] = level[current] + 1
        inorder(tree[current][0])

    cur += 1
    
    if level_min[level[current]] > cur:
        level_min[level[current]] = cur
    if level_max[level[current]] < cur:
        level_max[level[current]] = cur

    if tree[current][1] != -1:
        # 레벨 설정 후 다시 순회
        level[tree[current][1]] = level[current] + 1
        inorder(tree[current][1])

    return



N = int(input())  
parentNode = [-1] * (N+1)
tree = [[0] for _ in range(N+1)]
root = 0

for _ in range(N):
    v, left, right = map(int, input().split())

    tree[v] = [left, right]
    
    if left != -1:
        parentNode[left] = v
    
    if right != -1:
        parentNode[right] = v

# 루트 찾기
for i in range(1, N+1): 
    if parentNode[i] == -1:
        root = i


level_min = [N] * (N+1) 
level_max = [0] * (N+1)
level = [0] * (N+1)

level[root] = 1 # 루트 레벨 1로 선언
cur = 0

# 중위 순회
inorder(root)

result = 0
result_idx = 0

for i in range(1, n+1): # 4) 차이 찾기
    diff = level_max[i]-level_min[i]+1
    if result < diff:
        result = diff
        result_idx = i

print(result_idx, result)
