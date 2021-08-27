function solution(operations) {

  let arr = []
  let before

  operations.forEach(operation => {

    // 삽입
    if (operation[0] === 'I') {
      const num = parseInt(operation.split(' ')[1])

      arr.push(num)
      before = 'I'

    }

    // 삭제
    else {
      if (before === 'I') {
        arr.sort(function(a, b) {return a-b})
      }
      if (arr.length !== 0) {
        if (operation[2] === '-') {
          // 최솟값
          arr.shift()
        } else {
          // 최댓값
          arr.pop()
        }
      }
      before = 'D'
    }
  })

  // 출력하기 전에 한번 정렬해주기
  arr.sort(function(a, b) {return a-b})

  if (arr.length === 0) {
    return [0,0]
  }
  else {
    return [arr[arr.length-1], arr[0]]
  }
}
