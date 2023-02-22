import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr += list(map(int, input().split()))
    arr = sorted(arr, reverse=True)[:n] # 내림차순 정렬후 n번째 까지 슬라이싱
print(arr[n-1]) # 가장 뒤의 값 출력