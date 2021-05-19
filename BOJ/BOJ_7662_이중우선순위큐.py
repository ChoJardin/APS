import sys
import heapq

T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline())

    min_sort = []  # 최소힙
    max_sort = []  # 최대힙
    element = 0  # 들어온 원소의 개수
    del_min = dict()  # 최소힙에서 삭제된 기록
    del_max = dict()  # 최대힙에서 삭제된 기록

    for i in range(N):
        w, num = sys.stdin.readline().strip().split()
        num = int(num)

        # 입력
        if w == 'I':
            element += 1
            # 최소힙, 최대힙 동시에 넣어주기
            heapq.heappush(min_sort, num)
            heapq.heappush(max_sort, -num)

        else:  # 삭제
            # 들어온 원소가 없다
            if not element:
                continue

            # 최소힙에서 삭제한다 & 최소힙에 남은 원소가 있음
            if num == -1 and min_sort:
                # 최소힙에서 하나 뽑아서 확인
                get = heapq.heappop(min_sort)
                while del_max.get(get):  # 이미 최대힙에서 삭제된 숫자라면,
                    del_max[get] -= 1  # 삭제된 개수 하나 없애주고,
                    if del_max[get] == 0:  # 만약 삭제된 애 전부 뺐다면,
                        del del_max[get]  # 최대힙 삭제 기록에서 제거

                    # 최소힙에 남은 원소가 없다면,
                    if not min_sort:
                        break

                    # 다음애 뽑아서 다시 확인
                    get = heapq.heappop(min_sort)

                # while 반복 종료 == 최소힙에 남은 원소 있었다
                else:
                    # 최소힙 삭제 기록 갱신
                    del_min[get] = del_min.get(get, 0) + 1
                    # 남은 원소 개수 갱신
                    element -= 1

            # 최대힙
            elif num == 1 and max_sort:
                get = -heapq.heappop(max_sort)
                while del_min.get(get):
                    del_min[get] -= 1
                    if del_min[get] == 0:
                        del del_min[get]

                    if not max_sort:
                        break

                    get = -heapq.heappop(max_sort)

                else:
                    del_max[get] = del_max.get(get, 0) + 1
                    element -= 1

    # 남은 원소가 하나도 없음
    if not element:
        print('EMPTY')
    else:
        # 최댓값 == 최대힙에서 팝
        # 최소힙에서 삭제된 애랑 비교하면서 확인
        max_num = -heapq.heappop(max_sort)
        while del_min.get(max_num):
            del_min[max_num] -= 1
            if del_min[max_num] == 0:
                del del_min[max_num]
            max_num = -heapq.heappop(max_sort)

        # 최솟값
        min_num = heapq.heappop(min_sort)
        while del_max.get(min_num):
            del_max[min_num] -= 1
            if del_max[min_num] == 0:
                del del_max[min_num]
            min_num = heapq.heappop(min_sort)

        print(max_num, min_num)



