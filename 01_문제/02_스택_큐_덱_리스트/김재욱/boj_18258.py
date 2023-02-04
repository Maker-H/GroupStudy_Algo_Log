import sys

input = lambda : sys.stdin.readline().rstrip()
queue = []
n = int(input())
size = 0
front = 0
for _ in range(n):
	com, *num = input().split()
	if com == 'push':
		queue.append(int(num[0]))
		size += 1

	elif com == 'pop':
		if size > 0:
			print(queue[front])
			front += 1
			size -= 1
		else:
			print(-1)

	elif com == 'size':
		print(size)

	elif com == 'empty':
		if size == 0:
			print(1)
		else:
			print(0)

	elif com == 'front':
		if size == 0:
			print(-1)
		else:
			print(queue[front])

	elif com == 'back':
		if size == 0:
			print(-1)
		else:
			print(queue[-1])