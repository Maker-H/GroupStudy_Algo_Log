from collections import deque

def solution(places):
    answer = []
    
    for place in places:
        # 사람들이 있는 곳을 다 담기
        standards = []
        for f in range(5):
            for s in range(5):
                if place[f][s] == 'P':
                    standards.append([f, s])
        
        # 만약 사람 없으면 거리두기 지키는 것
        if not standards:
            answer.append(1)
            continue
        
        # 기준점 하나 잡고 거기에서 가까운 사람들 체크
        for point_f, point_s in standards:
            
            # 가장 가까운 p 찾기(후보군 p 찾기)
            candids = find_candids(point_f, point_s, place)
            candids = sorted(candids, key=lambda x:x[2])
            
            # 코로나 나오면 더 체크할 이유 없다 
            if is_close_corona(point_f, point_s, candids, place):
                answer.append(0)
                break
        # for 안에서 한번도 안걸렸으면 코로나 아니다
        else:
            answer.append(1)

    return answer


def is_close_corona(point_f, point_s, candids, place):
    
    # 가장 가까운 p 와 맨하튼이면 그냥 바로 0고 아니면 파티션 있는지 검증해야함        
    for candid_f, candid_s, candid_range in candids:
        # 거리 충분히 멀다
        if candid_range > 2:
            return False

        # 가장 가까운 p 와 맨하튼 아니면 그 다음도 아닐 수 있으니까 맨하튼 자리 나올때까지 검증해야함
        # 코로나 맞는 경우 한 번이라도 나온다면 굳이 다음을 볼 필요 없다
        elif candid_range <= 2:
            if is_corona(point_f, point_s, candid_f, candid_s, place):
                return True

    return False




# 전달받은 사람 기준으로 후보군 찾기 f,s,cnt 순으로 변수 저장
def find_candids(f, s, place):
    df = [0, 0, 1, -1]
    ds = [1, -1, 0, 0]
    visited = [[0] * 5 for _ in range(5)] 
    
    Q = deque()
    candids = []
    
    Q.append([f, s, 0])
    visited[f][s] = 1
    
    while Q:
        f, s, cnt = Q.popleft() 
        
        for k in range(4):
            nf = f + df[k]
            ns = s + ds[k]
            if 0 <= nf < 5 and 0 <= ns < 5 and visited[nf][ns] == 0:
                visited[nf][ns] = 1
                Q.append([nf, ns, cnt + 1])
                if place[nf][ns] == 'P':
                    candids.append([nf, ns, cnt + 1])
    return candids


# true이면 코로나 맞음
# 파티션 있는지 찾는 함수 (맨하튼 거리 2 이하의 경우)
def is_corona(point_f, point_s, candid_f, candid_s, place):
    print(point_f, point_s, candid_f, candid_s, place)
    # 같은 행에 있을 경우
    if point_f == candid_f:
        if abs(point_s - candid_s) == 1:
            return True
        elif abs(point_s - candid_s) == 2:
            if place[point_f][(point_s + candid_s) // 2] == 'X':
                return False
            else:

                return True
            
    # 같은 행에 있는 경우
    if point_s == candid_s:
        if abs(point_f - candid_f) == 1:
            return True
        elif abs(point_f - candid_f) == 2:
            if place[(point_f + candid_f) // 2][point_s] == 'X':
                return False
            else:
                return True
            
    # 대각선에 있는 경우        
    else:
        if place[candid_f][point_s] == 'X' and place[point_f][candid_s] == 'X':
            return False
        else:
            return True
        
