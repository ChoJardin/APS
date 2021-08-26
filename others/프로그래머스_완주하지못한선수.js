function solution(participant, completion) {

  const participated = Object

  participant.forEach(each => {
    if (each in participated)
      participated[each] += 1
    else participated[each] = 1
  })

  completion.forEach(each => {
    participated[each] -= 1
    if (participated[each] === 0) {
      delete participated[each]
    }
  })

  return Object.keys(participated)[0]
}

solution(["leo", "kiki", "eden"], ["eden", "kiki"])
