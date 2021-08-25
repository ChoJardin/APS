function solution(brown, yellow) {
    let answer = [];

    brown = parseInt(brown)
    yellow = parseInt(yellow)

    const total = brown + yellow

    for (let i = 1; i < parseInt(total / 2); i++) {
        if (total % i == 0) {
            const column = i
            const row = parseInt(total / i)

            if ( (column-2) * (row-2) === yellow) {
                answer = [column, row]
                break
            }
        }
    }

    return answer;
}