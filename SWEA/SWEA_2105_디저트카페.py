import sys
sys.stdin = open('SWEA_2105_input.txt', 'r')


def tour():
    # 투어 시작 가능한 위치
    # 가로 -> 1~ N-2
    # 세로 -> 0 ~ N-3

    # 탐색
    dy = []

    # 먹은 디저트 추가
    deserts = set()

    for i in range(0, N-2):
        for j in range(1, N-1):



            deserts.add(cafes[i][j])






T = int(input())

for tc in range(T):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]

