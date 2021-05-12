def Hanoi(n, start, mid, end):  # 시작, 기착, 도착
    # base_case
    if n == 1:
        return results.append((start, end))
    else:
        # 마찬가지로 시작, 기착, 도착 순서대로
        Hanoi(n-1, start, end, mid)
        Hanoi(1, start, mid, end)
        Hanoi(n-1, mid, start, end)


n = int(input())

results = []
# 세개의 점으로 1-3으로 이동
Hanoi(n, 1, 2, 3)

print(len(results))
for result in results:
    print(result[0], result[1])
