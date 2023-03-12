from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin, 0))
    visited = [0]*len(words)
    while q:
        word, cnt = q.popleft()
        if word == target:
            # 단어가 같은지 확인
            answer = cnt
            break
        for i in range(len(words)):
            temp = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        # 다른 알파벳 수 체크
                        temp += 1
                if temp == 1:
                    # 알파벳이 다른게 하나라면 q에 append
                    q.append((words[i], cnt+1))
                    visited[i] = 1
    return answer