import sys
sys.stdin = open('큐2.txt', 'r')

n = int(input())
queue = []
cnt = 0
for i in range(n):
    input_order = sys.stdin.readline().split()
    order = input_order[0]
    if order == 'push':
        queue.append(input_order[1])
    elif order == 'pop':
        if len(queue)-cnt == 0:
            print(-1)
        else:
            print(queue[cnt])
            cnt += 1
    elif order == 'size':
        print(len(queue)-cnt)
    elif order == 'empty':
        if len(queue)-cnt == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(queue)-cnt == 0:
            print(-1)
        else:
            print(queue[cnt])
    elif order == 'back':
        if len(queue)-cnt == 0:
            print(-1)
        else:
            print(queue[-1])