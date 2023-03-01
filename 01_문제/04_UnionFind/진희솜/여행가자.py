import sys
sys.setrecursionlimit(10**6)

def union(f, s):
    if f == s:
        return
    
    f = find(f)
    s = find(s)
    if f < s:
        city[s] = f
    elif f > s:
        city[f] = s

def find(num):
    if city[num] != num:
        city[num] = find(city[num])
    
    return city[num]


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
city = [i for i in range(N)]

for f in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for s in range(len(tmp)):
        if tmp[s] == 1:
            union(f, s)
    


plans = list(map(int, sys.stdin.readline().split()))

first_plan = find(plans[0]-1)
is_pos = True

for plan in plans:
    tmp = find(plan-1)
    if tmp != first_plan:
        is_pos = False
        break

if is_pos:
    print('YES')
else:
    print('NO')
