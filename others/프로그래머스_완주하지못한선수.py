def solution(participant, completion):

    completed = {}

    # 참가자 인원 세기
    for each in participant:
        completed[each] = completed.get(each, 0) + 1

    # 완주자 인원 빼기
    for each in completion:
        completed[each] -= 1

        # 모두 다 카운트 끝났으면 리스트에서 없애버린다.
        if completed[each] == 0:
            del completed[each]

    return list(completed.keys())[0]