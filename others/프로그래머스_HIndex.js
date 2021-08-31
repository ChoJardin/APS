function solution(citations) {

  if (Math.min(...citations) >= citations.length) {
    return citations.length
  }

  citations.sort(function(a, b) {return b-a})

  for (let i=0; i < citations.length; i++) {
    if (i+1 > citations[i]) {
      return i
    }
  }
}

console.log(solution([3, 0, 6, 1, 5]))