import sys
input = sys.stdin.readline

n = int(input())
nums = list(int(input()) for _ in range(n))
stack = []
count = 0
num = 1
ans = []
for i in range(n):
    while num <= nums[i]: # 입력받은 i번째 숫자보다 작거나 같으면 stack에 append
        stack.append(num)
        ans.append('+') # ans에 + 추가
        num += 1

    if nums[i] == stack[-1]: # stack의 가장위의 숫자와 입력받은 i번째 숫자가 같으면 pop
        stack.pop()
        ans.append('-') # ans에 - 추가
    else: # 그 외의 경우 수열을 만들수 없으므로 NO를 출력하고 break
        print('NO')
        break
else: # 수열을 만들 수 있을 때
    for a in ans:
        print(a)



