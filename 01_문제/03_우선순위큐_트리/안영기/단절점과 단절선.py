# https://www.acmicpc.net/status?user_id=thfl9281&problem_id=14675&from_mine=1
# 14675 [안영기] 트리 / 단절점과 단절선 / 실버

import sys

input = sys.stdin.readline

N = int(input())
tree = [0] * (N + 1)
for i in range(N - 1):
    a, b = map(int, input().split())
    tree[a] += 1
    tree[b] += 1

q = int(input())
for i in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if tree[k] > 1:
            flag = True
        else:
            flag = False

    else:
        flag = True

    if flag:
        print('yes')
    else:
        print('no')