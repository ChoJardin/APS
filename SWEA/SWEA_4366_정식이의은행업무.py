def search_deux():
    for i in range(len(deux)):  # 이진법의 경우 0->1/ 1->0
        dix = 0

        # 일단 i 번째 자리 바꿔줬고요
        if deux[i] == 1:
            deux[i] = 0
        else:
            deux[i] = 1

        # 계산합니다.
        for j in range(len(deux)):  # 0, 1, 2, 3 ...
            dix += 2**(len(deux)-j-1) * deux[j]
        deux_set.append(dix)

        # 원상복구
        if deux[i] == 1:
            deux[i] = 0
        else:
            deux[i] = 1


def search_trois():
    copy_trois = trois[:]

    for i in range(len(trois)):  # 이진법의 경우 0->1/ 1->0
        dix = 0

        # 일단 i 번째 자리 바꿔줬고요..
        # 단순하게 바꾸면 안되겠네요 경우마다 계산이 필요해 보입니다..
        if trois[i] == 1:
            trois[i] = 2
        elif trois[i] == 2:
            trois[i] = 0
        else:  # 0일 때는 1로
            trois[i] = 1

        # 계산합니다.
        for j in range(len(trois)):  # 0, 1, 2, 3 ...
            dix += 3**(len(trois)-j-1) * trois[j]
        trois_set.append(dix)

        # 삼진법은 두번 교체가 가능하지..
        if copy_trois[i] == 1:  # 원래가 1 그러면 2로 바뀌었음 지금은 0
            trois[i] = 0
        elif copy_trois[i] == 2:
            trois[i] = 1
        else:
            trois[i] = 2

        dix = 0
        for j in range(len(trois)):  # 0, 1, 2, 3 ...
            dix += 3**(len(trois)-j-1) * trois[j]
        trois_set.append(dix)

        # 원상복구
        trois[i] = copy_trois[i]


def find_common():
    for each in deux_set:
        if each in trois_set:
            return each


T = int(input())

for tc in range(T):
    deux = list(map(int, list(input())))  # 이진수 [1, 0, 1, 0 ]
    trois = list(map(int, list(input())))  # 삼진수

    deux_set = []
    trois_set = []

    # 함수 활용해서 각각 만들어질 수 있는 십진수를 확인하고,
    # 그 중 공통되는 걸 출력하면 되겠습니다..
    search_deux()
    search_trois()
    # print(deux_set)
    # print(trois_set)

    print('#{} {}'.format(tc+1, find_common()))  # find_common == 두 리스트에서 공통요소 찾아 반환
