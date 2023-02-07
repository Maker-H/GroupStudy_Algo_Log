import sys
sys.stdin = open('큐_input.txt', 'r')

N = int(sys.stdin.readline())
queue = []
for i in range(N):
    input_order = sys.stdin.readline().split()
    order = input_order[0]

    if order == 'push':
        queue.append(input_order[1])

    elif order == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))

    elif order == 'size':
        print(len(queue))

    elif order == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif order == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif order == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

