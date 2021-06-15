import sys
input = sys.stdin.readline

from collections import deque


def ac():
    global arr
    # 배열이 뒤집어졌는지 확인
    is_reversed = False
    # 함수를 각각 확인하면서
    for each in p:
        if each == 'R':
             is_reversed = not is_reversed

        elif each == 'D':
            # 숫자가 없는데 삭제하는 경우
            if not len(arr):
                return 'error'

            # 숫자가 남아있다면,
            # 뒤집어졌는지 여부에 따라서 삭제
            # false -> popleft/ true -> pop
            if is_reversed:
                arr.pop()
            else:
                arr.popleft()

    # 모든 연산이 끝난 경우
    arr = list(arr)

    # 뒤집어 있다면,
    # 정답을 보면 띄어쓰기 없는 애들이라서 그냥 리스트로 출력하면 안되고
    # 별도로 띄어쓰기 없이 출력되도록 만들어줘야 함
    if is_reversed:
        return '[' + ','.join(map(str, arr[::-1])) + ']'
    else:
        return '[' + ','.join(map(str, arr)) + ']'


T = int(input())

for tc in range(T):
    # 수행할 함수
    p = input()
    # 수의 개수
    n = int(input())
    # 배열
    arr = deque()
    num = ''
    for each in input():
        if each.isnumeric():
            num += each
        elif each == ',':
            arr.append(int(num))
            num = ''
    # 아예 배열이 들어오지 않는다면, num이 없음
    if num:
        arr.append(int(num))

    print(ac())


