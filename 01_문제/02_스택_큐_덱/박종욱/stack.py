# class Stack:

#     def __init__(self):
#         self.name = []

#     def push(self,num):
#         self.name.append(num)

#     def pop(self):
#         if len(self.name) >= 1:
#             self.name.remove(self.name[-1])
#             return self.name.remove(self.name[-1])
#         else:
#             return -1
    
#     def size(self):
#         return len(self.name)
    
#     def empty(self):
#         if len(self.name) == 0:
#             return 1
#         else:
#             return 0

#     def top(self):
#         if len(self.name) == 0:
#             return -1

#         else:
#             return self.name[-1]

import sys
list = []
T = int(sys.stdin.readline())
for _ in range(T):

    K = sys.stdin.readline().split()

    if K[0] == 'push':
        list.append(int(K[1]))

    elif K[0] == 'pop':
        if len(list) >= 1:
            print(list[-1])
            list.pop()
        else:
            print(-1)

    elif K[0] == 'size':
        print(len(list))
    
    elif K[0] == 'empty':
        if len(list) >= 1:
            print(0)
        else:
            print(1)

    elif K[0] == 'top':
        if len(list) == 0:
            print(-1)
        else:
            print(list[-1])
