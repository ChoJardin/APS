def solution(citations):
    # 최솟값이 논문 수 보다 크다면,
    # 논문 개수 그대로 반환
    if min(citations) >= len(citations):
        return len(citations)

    # 내림차순 정렬
    citations.sort(reverse=True)

    # 인용 많은 순으로 확인하면서 내려간다
    for (idx, citation) in enumerate(citations):
        if idx + 1 > citation:
            return idx