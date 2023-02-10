import sys
sys.stdin = open('후위표기식2.txt', 'r')

# https://www.acmicpc.net/problem/1935
# 스택 /

N = int(input())
s = list(input())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_dict = {}
for _ in range(N):
    num = int(input())
    num_dict[_+65] = num

while len(s) != 1:
    for i in range(len(s)):
        if str(s[i]) in alphabet:
            s[i] = num_dict[ord(s[i])]

        else:
            if s[i] == '*':
                s[i] = s[i-2] * s[i-1]
                s.pop(i-1)
                s.pop(i-2)
                break
            elif s[i] == '+':
                s[i] = s[i-2] + s[i-1]
                s.pop(i-1)
                s.pop(i-2)
                break
            elif s[i] == '/':
                s[i] = s[i-2] / s[i-1]
                s.pop(i-1)
                s.pop(i-2)
                break
            elif s[i] == '-':
                s[i] = s[i-2] - s[i-1]
                s.pop(i-1)
                s.pop(i-2)
                break
print(f'{s[0]:.2f}')

