def solution(genres, plays):

    answer = []

    play_cnt = {}
    genre_sort = {}

    for (idx, genre) in enumerate(genres):
        if genre not in play_cnt:
            play_cnt[genre] = 0
            genre_sort[genre] = []

        genre_sort[genre].append([plays[idx], idx])
        play_cnt[genre] += plays[idx]

    sorted_cnt = sorted(play_cnt.items(), key=lambda x: x[1], reverse=True)

    for each in sorted_cnt:
        genre = each[0]
        list = sorted(genre_sort[genre], key=lambda x: x[1], reverse=True)
        list.sort(key=lambda x: x[0])
        n = 0
        while list:
            to_add = list.pop()
            answer.append(to_add[1])
            n += 1

            if n == 2:
                break

    return answer

