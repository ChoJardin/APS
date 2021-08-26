from itertools import combinations, permutations

# import sys
# sys.stdin = open('4012_input.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())

    synergy = list(list(map(int, input().split())) for _ in range(N))

    ingredients = [i for i in range(N)]
    possibles = list(combinations(ingredients, N//2))

    # 확인이 끝나면 여기에 넣어줍니다.
    checked = set()

    min_difference = 999999999999

    for each in possibles:
        # 아직 확인하지 않은 조합이라면,
        if each not in checked:
            # 2개씩 뽑아서
            food1 = 0
            for dish in list(permutations(each, 2)):
                food1 += synergy[dish[0]][dish[1]]

            # 이번에 선택되지 않은 친구들..
            another = []
            for i in range(N):
                if i not in each:
                    another.append(i)

            food2 = 0
            for dish in list(permutations(another, 2)):
                food2 += synergy[dish[0]][dish[1]]

            difference = abs(food1-food2)

            if difference < min_difference:
                min_difference = difference

            checked.add(each)
            checked.add(tuple(another))

    print('#{} {}'.format(tc+1, min_difference))








