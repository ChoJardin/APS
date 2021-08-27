import heapq


def solution(operations):

    # 최소힙
    min_queue = []
    # 최대힙
    max_queue = []
    # 숫자 개수 세기
    cnt = dict()

    for operation in operations:
        # 큐에 삽입
        if operation[0] == 'I':
            num = int(operation[2:])

            heapq.heappush(min_queue, num)
            heapq.heappush(max_queue, -num)
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1

        # 삭제
        elif operation[0] == 'D':
            if not len(cnt):
                continue
            # 최솟값
            if operation[2] == '-':

                while True:
                    to_delete = heapq.heappop(min_queue)

                    # 숫자 하나 지우고,
                    # 만약 다 지워졌으면 완전 없애버린다.
                    if to_delete in cnt:
                        cnt[to_delete] -= 1
                        if cnt[to_delete] == 0:
                            del cnt[to_delete]
                        break

            # 최댓값
            else:
                while True:
                    to_delete = -heapq.heappop(max_queue)

                    if to_delete in cnt:
                        cnt[to_delete] -= 1
                        if cnt[to_delete] == 0:
                            del cnt[to_delete]
                        break

    # 연산이 모두 끝났을 때,
    # 남은 숫자가 없다면,
    if not len(cnt):
        max_num = 0
        min_num = 0

    # 남은 숫자가 있다면 최대/ 최소 반환
    else:
        # 최댓값 찾기
        while max_queue:
            max_num = -heapq.heappop(max_queue)

            if cnt.get(max_num):
                break

        # 최솟값 찾기
        while min_queue:
            min_num = heapq.heappop(min_queue)

            if cnt.get(min_num):
                break

    return [max_num,min_num]

