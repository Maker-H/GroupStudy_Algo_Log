from sys import stdin


class Stack:
    def __init__(self):
        self.s = [0 for _ in range(100005)]
        self.s_size = 0

    def push(self, val):
        if self.s_size == 100005:
            return
        self.s[self.s_size] = val
        self.s_size += 1

    def pop(self):
        if self.s_size == 0:
            return 0
        val = self.s[self.s_size - 1]
        self.s_size -= 1
        return val

    def peek(self):
        if self.s_size == 0:
            return 0
        return self.s[self.s_size - 1]

    def size(self):
        return self.s_size

    def __str__(self):
        return str(self.s[:self.s_size])


T = int(stdin.readline())
my_answer = Stack()  # 내 정답
match_tmp = Stack()
basic = Stack()  # 1~8 차례대로
tmp = Stack()  #

for num in range(T, 0, -1):
    basic.push(num)

for _ in range(T):
    match_tmp.push(int(stdin.readline()))

# 거꾸로 넣어주기
goal = Stack()  # 이렇게 정렬해야 되는 결과값
for _ in range(T):
    goal.push(match_tmp.pop())

goal_size = T
operator = [0 for _ in range(500000)]
idx = 0


while goal_size != 0:
    goal_num = goal.peek()
    answer_num = my_answer.peek()
    if answer_num > goal_num:
        operator[idx] = 'NO'
        break

    while goal_num != answer_num:
        answer_num = basic.pop()
        my_answer.push(answer_num)
        operator[idx] = '+'
        idx += 1
        goal_num = goal.peek()
        answer_num = my_answer.peek()


    my_answer.pop()
    goal.pop()
    operator[idx] = '-'
    idx += 1
    goal_size = goal.size()

if operator[idx] == 'NO':
    print('NO')
else:
    for c in operator[:idx]:
        print(c)