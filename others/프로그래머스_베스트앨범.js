function solution(genres, plays) {
  const answer = [];

  // 장르 별 재생 횟수 더하기
  const playCnt = Object()
  // 각 장르마다 재생횟수/ idx 리스트로 저장
  const genreSort = Object()

  genres.forEach(function(genre, idx) {
    if  (!(genre in playCnt)) {
      playCnt[genre] = 0
      genreSort[genre] = Array()
    }

    playCnt[genre] += plays[idx]
    genreSort[genre].push([plays[idx], idx])
  })

  // 재생 많이 된 순으로 정렬
  const sortedCnt = Object.entries(playCnt).sort(function (a, b) { return b[1]-a[1]})

  // 재생 많이 된 장르 순으로 2개씩 앨범에 추가
  sortedCnt.forEach(genre => {
    const toAdd = genreSort[genre[0]].sort(function(a, b) {return b[0]-a[0]})

    for (let i=0; i < 2; i++) {
      if (toAdd.length === i) {
        break
      }
      else {
        answer.push(toAdd[i][1])
      }
    }
  })

  return answer;
}

console.log(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))