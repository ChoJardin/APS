function solution(board, moves) {
    var answer = 0;

    const basket = [];

    for (let i = 0; i < moves.length; i++) {
        // 이번 턴에서 제거할 바스켓..
        const turn = moves[i] - 1;

        for (let j = 0; j < board.length; j++) {
            // 비어있으면 아랫줄 확인하러 이동
            if (board[j][turn] === 0) {
                continue;
            }

            // 인형 옮기기
            if (basket.length && basket[basket.length - 1] === board[j][turn]) {
                answer += 2;
                basket.pop();
            } else {
                basket.push(board[j][turn]);
            }

            board[j][turn] = 0;

            break;
        }
    }

    return answer;
}
