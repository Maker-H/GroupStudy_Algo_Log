# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# [안영기] 너비우선탐색 / 단어 변환 / level3
from collections import deque

def solution(begin, target, words):
    if target not in words: # target이 리스트에 없으면 오류
        return 0

    Q = deque()
    Q.append((begin, 0))

    while Q:
        x, answer = Q.popleft()

        for i in range(len(words)): # 리스트의 요소를 하나씩
            cnt = 0                 # 비교하여
            for j in range(len(x)): # 비교대상(x)와 다른 철자 개수 카운팅
                if x[j] != words[i][j]:
                    cnt += 1
            if cnt == 1:            # 다른 철자가 1개이면 Q에 append
                if words[i] == target:
                    return answer+1 # target과 같으면 return
                else:
                    Q.append((words[i], answer + 1))

    return 0    # target이 리스트에는 있었지만 변경 실패면 오류

bigin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(bigin, target, words))


