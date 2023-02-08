from collections import deque

n = int(input())
equation = input()
nums = [int(input()) for _ in range(n)]
operator = ['+','-','/','*']

stack = deque()
i = 0
for e in equation:
	if e in operator:
		a = stack.pop() # 두개의 숫자 스텍에서 뽑아오기
		b = stack.pop() 
		if e == '+': 
			stack.append(b+a)
		elif e == '-':
			stack.append(b-a)
		elif e == '*':
			stack.append(b*a)
		else:
			stack.append(b/a)

	else:
		i = ord(e) - ord('A') # 문자열을 아스키코드를 이용하여 인덱스화
		stack.append(nums[i])


print('{:.2f}'.format(stack.pop())) # 소수점 둘째 자리까지 출력
