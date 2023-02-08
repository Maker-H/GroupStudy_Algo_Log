from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
balloon = deque()
for i in range(1, n+1):
    balloon.append(i)   # 순서대로 풍선 저장
num = deque(map(int, input().split()))  # 풍선 안 숫자 저장
result = []
while len(balloon)>1:   # 풍선이 하나 남을 때까지
    if num[0] > 0:      # 풍선 안 숫자 양수
        count = num[0]    # 몇 칸 이동할 지 저장
        result.append(balloon.popleft())  # 해당 풍선 제거 후 result에 저장
        num.popleft()
        for _ in range(count-1):    # 숫자 -1 만큼 왼쪽으로 밀기
            balloon.append(balloon.popleft())
            num.append(num.popleft())
    else:               # 풍선 안 숫자 음수
        count = -num[0]
        result.append(balloon.popleft())  # 해당 풍선 제거 후 result에 저장
        num.popleft()
        for _ in range(count):      # 숫자만큼 오른쪽으로 밀기
            balloon.appendleft(balloon.pop())
            num.appendleft(num.pop())
print(*result, *balloon)            # result와 마지막 풍선 출력


