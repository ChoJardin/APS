data = input()

## 주의 ## 괄호는 stack 밖에서는 우선순위가 3이지만, stack안에 들어가면 0으로 계산된다.
match = {'(': (0, 3), '*': (2, 2), '/': (2, 2), '+': (1, 1), '-': (1, 1)}
stack = []

for ch in data:
    # 알파벳인 경우
    if ch.isalpha():
        print(ch, end='')

    # 닫는 괄호
    elif ch == ')':
        # 여는 괄호 나올 때 까지
        while stack[-1] != '(':
            print(stack.pop(), end='')
            # continue
        # 여는 괄호도 pop
        stack.pop()

    # 연산자 + 여는 괄호
    elif ch in match:
        # 아무것도 없는 경우 push
        if len(stack) == 0:
            stack.append(ch)

        # 채워져 있는 경우 우선순위 비교
        # stack 안의 우선순위 = match[ch][0]
        # stack 밖에서의 우선순위 = match[ch][1]
        else:
            # ch가 더 높은 경우
            if match[stack[-1]][0] < match[ch][1]:
                stack.append(ch)

            # ch가 더 낮거나 같은 경우 == 높거나 같으면 pop
            else:
                while stack and match[stack[-1]][0] >= match[ch][1]:
                    print(stack.pop(), end='')
                stack.append(ch)

# 남아있는 연산자
while stack:
    print(stack.pop(), end='')









