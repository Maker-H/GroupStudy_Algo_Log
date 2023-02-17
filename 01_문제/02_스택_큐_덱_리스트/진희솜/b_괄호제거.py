from sys import stdin
import copy

class Stack:
    def __init__(self):
        self.s = [0] * 205
        self.size = 0
        self.s_max = 205

    def push(self, val):
        if self.size == self.s_max:
            return -1
        self.s[self.size] = val
        self.size += 1

    def pop(self):
        if self.size == 0:
            return  -1
        val = self.s[self.size-1]
        self.size -= 1
        return  val

    def empty(self):
        return self.size == 0

    def __str__(self):
        return "".join(self.s[:self.size])

    def s_size(self):
        return self.size

    def peek(self):
        return self.s[self.size-1]

input_formula = stdin.readline().replace('\n', '')

formula = Stack()
paren_cnt = 0
for c in input_formula:
    if c == '(':
        paren_cnt += 1
    formula.push(c)


repeat = 2 ** paren_cnt - 1

binary = [[0]*paren_cnt for _ in range(repeat)]
# 바이너리로 만든다
for point_i in range(repeat):
    for move_i in range(paren_cnt):
        if point_i & (1 << move_i):
            binary[repeat-1 - point_i][paren_cnt-1 - move_i] = 1
        else:
            binary[repeat-1 - point_i][paren_cnt-1 - move_i] = 0

parenthese = Stack() # 괄호 임시로 저장하는 곳
answer = [0 for _ in range(repeat)] # 수식 옮겨서 저장하는 곳
answer_idx = 0
copy_formula = Stack()

# 괄호 제거 출력
for point_i in range(repeat):

    copy_formula = copy.deepcopy(formula)
    tmp_answer = Stack()
    marker_i = 0
    reversed_answer = Stack()

    for _ in range(copy_formula.s_size()):
        c = copy_formula.pop()
        if marker_i < paren_cnt and binary[point_i][marker_i] == 1 and c == ')':

            tmp_answer.push(c)
            parenthese.push(0) # 0을 더미로 사용
            marker_i += 1
        elif marker_i < paren_cnt and binary[point_i][marker_i] == 0 and c == ')':

            parenthese.push(c)
            marker_i += 1

        if c != ')' and c != '(':
            tmp_answer.push(c)

        elif c == '(':
            if parenthese.peek() == 0:
                tmp_answer.push(c)
                parenthese.pop()
            else:
                parenthese.pop()

    for _ in range(tmp_answer.s_size()):
        reversed_answer.push(tmp_answer.pop())

    answer[answer_idx] = str(reversed_answer)
    answer_idx += 1
answer = set(answer)

answer = sorted(answer)
for oneline in answer:
    print(oneline)







