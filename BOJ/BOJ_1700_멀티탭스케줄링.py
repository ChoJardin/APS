import sys
input = sys.stdin.readline


def change_tab():

    # 플러그를 빼는 횟수
    cnt = 0

    # 현재 멀티탭 상황
    current_tab = set()
    for i in range(K):
        current_tab.add(tabs[i])
        if len(current_tab) == N:
            break

    # K 를 끝까지 돌았음 == 코드를 뽑을 필요가 없다.
    else:
        return cnt

    # 기기 사용되는 순서 인덱스 저장
    schedule = dict()
    # 현재 콘센트에 꼽혀 있는 애들은 적어주면 안된다.
    for idx, each in enumerate(tabs[i+1:]):
        idx += (i+1)
        if not schedule.get(each):
            schedule[each] = list()

        schedule[each].append(idx)

    # 뽑을 코드 찾아보자
    # 여기도 마찬가지로 현재 콘센트 뒤부터 확인해준다.
    for j in range(i+1, K):

        next_tab = tabs[j]

        schedule[next_tab] = schedule[next_tab][1:]
        # 다음에 더 오지 않는다면, 없애버리자
        if not schedule[next_tab]:
            schedule.pop(next_tab)

        # 필요한 전자제품이 꽂혀있지 않다면
        if not current_tab.__contains__(next_tab):
            # 하나 뺀다
            cnt += 1

            latest = j
            tab_out = 0
            for tab in current_tab:
                # 스케쥴에 들어있지 않음 == 다음에 다시 꼽지 않는다 -> 얘를 뽑는다.
                if not schedule.get(tab):
                    tab_out = tab
                    break

                # 그렇지 않으면 제일 나중에 꼽히는 애를 뽑아준다.
                if schedule[tab][0] > latest:
                    latest = schedule[tab][0]
                    tab_out = tab

            current_tab.discard(tab_out)
            current_tab.add(next_tab)

    return cnt


# 멀티탭 크기, 전기용품 사용 횟수
N, K = map(int, input().split())
tabs = list(map(int, input().split()))

print(change_tab())

