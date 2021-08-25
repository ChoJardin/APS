def solution(brown, yellow):
    answer = []

    total = brown + yellow

    for i in range(1, total // 2):
        # 나누어떨어진다면,
        if total % i == 0:
            column = i  # 세로
            row = total // i  # 가로

            if (column-2) * (row-2) == yellow:
                answer = [row, column]
                break

    return answer