from itertools import permutations


def solution(expression):

    str_num = '0123456789'

    exp_list = []

    one_num = ''
    for each in expression:  # 각각에 대해서
        if each in str_num:  # 숫자라면
            one_num += each
        else:  # 숫자 끝났음
            exp_list.append(one_num)  # 숫자한개 올려주고
            exp_list.append(each)  # 연산자 올려주고,
            one_num = ''  # 초기화
    # 마지막 숫자 올리기
    exp_list.append(one_num)

    calculator = ['+', '-', '*']
    cal_set = list(permutations(calculator))  # 연산자 우선순위 집합..

    max_result = 0  # 이제까지의 최댓값

    for i in range(len(cal_set)):

        temp = exp_list[:]
        now_set = cal_set[i]

        for j in range(3):
            if now_set[j] in exp_list:  # 연산자가 들어있는 경우에만 연산을 수행
                cnt = 0  # 확인할 인덱스 값

                while cnt < len(temp):
                    if temp[cnt] == now_set[j]:  # 찾고 있는 연산자라면,
                        result = str(eval(temp[cnt-1]+temp[cnt]+temp[cnt+1]))  # 계산
                        temp = temp[:cnt-1] + [result] + temp[cnt+2:]  # 반영
                    else:  # 찾고 있는 연산자가 아니라면 다음을 보겠다.
                        cnt += 1

        now_result = abs(int(temp[0]))

        if now_result > max_result:
            max_result = now_result

    return max_result

# ans = solution("100-200*300-500+20")
# print(ans)
#
# ans = solution("50*6-3*2")
# print(ans)
