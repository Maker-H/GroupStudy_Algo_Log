import sys
sys.stdin = open('AC_input.txt', 'r')

T = int(input())
for testcase in range(T):
    command = list(input())
    N = int(input())
    if N == 0:
        arr = input()
    else:
        arr = list(map(int, input()[1:-1].split(',')))
    cnt = 0
    if N == 0:
        arr = list()
    while command:
        order = command[0]
        if order == 'R':
            cnt += 1
        elif order == 'D':
            if len(arr) > 0:
                if cnt % 2:
                    arr.pop()
                else:
                    arr.pop(0)
            else:
                arr = 'error'
                break
        command.pop(0)
    if cnt % 2:
        arr.reverse()
    print(arr)



# [1,2,3,4]
# T = int(input())
# for testcase in range(T):
#     command = list(input())
#     N = int(input())
#     arr = input()
#     if arr == '[]':
#         arr = 'error'
#     else:
#         arr = list(map(int, arr.strip('[]').split(',')))
#         while command:
#             order = command[0]
#             if order == 'R':
#                 arr.reverse()
#             elif order == 'D':
#                 if len(arr) > 0:
#                     arr.pop(0)
#                 else:
#                     arr = 'error'
#                     break
#             command.pop(0)
#     print(arr)