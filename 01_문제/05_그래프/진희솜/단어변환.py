from collections import deque

    
def solution(begin, target, words):
    answer = 0
    
    # words 안에 목표하는 단어 있는지 확인    
    is_init = check_init(target, words)
    if not is_init:
        return 0
    
        
    # 가까운 값 순회하면서 글자 하나만 다른지 확인하고 target 만나면 min_cnt 확인한 후 빠져나오는거로 만들기
    # 첫 후보 찾기
    first_idx = find_candid(begin, words)
    answer = bfs(target, first_idx, words)

    return answer
    
    
def check_init(target, words):
    if target in words:
        return True
    else:
        return False
    

def find_candid(begin, words):
    for i in range(len(words)):
        if check_diff(begin, words[i]) == 1:
            return i

    
    
def bfs(target, first_idx, words):
    Q = deque()
    visited = [0] * len(words)
    Q.append([words[first_idx], 1])
    visited[first_idx] = 1
    
    while Q:
        print(Q)
        begin, cnt = Q.popleft()
        
        if begin == target:
            return cnt
        
        for idx in range(len(words)):
            if begin != words[idx] and visited[idx] == 0 and check_diff(begin, words[idx]) == 1:
                visited[idx] = 1
                Q.append([words[idx], cnt + 1])
    
    return 0

# 한글자만 달라야 한다
def check_diff(w1, w2):
    w1 = list(w1)
    w2 = list(w2)
    
    cnt = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            cnt += 1
        if cnt > 1:
            return -1
        
    if cnt == 0:
        return 0
    elif cnt == 1:
        return 1
                

