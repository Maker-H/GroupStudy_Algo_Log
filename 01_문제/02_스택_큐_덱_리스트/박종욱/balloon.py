from collections import deque                           # 원형큐 만들기 위해 deque 가져옴

T = int(input())
a = deque(enumerate(map(int,input().split())))          # 값과 값에 들어있는 쪽지를 묶기위해 enumerate사용
new_list = []                                           # 터트린 풍선을 넣을 리스트


while T != 0:                                           # T==0이 될때까지 반복
    T -= 1                                              # 반복때마다 -1
    num, k = a.popleft()                                # 가장 처음에 위치한 풍선 팝 튜플로 뽑기 때문에 값두개할당
    new_list.append(num+1)                              # enumerate로 1이아닌 0부터 시작 +1 해줌
    if k > 0:                                           # 만약 풍선내의 값이 양수면
        a.rotate(1-k)                                # 팝을 해서 한칸옮겨감(+1) k만큼 뒤로 추가로 회전
    elif k < 0:
        a.rotate(-k)                                    #음수면 k만큼 뒤로 회전

print(*new_list)
