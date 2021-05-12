# 코드를 한 줄 씩 받아서 2진법으로 변환한다.
# 모두 0으로 이루어진 코드가 아니라면 == 암호가 들어있다면,
# 리스트에 그 때 저장해주는 걸로..
# 그래서 1을 찾을 때, 맨 위 혹은 위가 1이 아니면 그거슨 처음 나온 암호임 ㅇㅇ

# import sys
# sys.stdin = open('1242_input.txt', 'r')
# sys.stdout = open('1242_output_last.txt', 'w')

# 뒤에서부터 어느 인덱스에 1이 있나 찾아주는 함수입니다 \^0^/
def ilchatgi(code):
    # 코드에 1이 없다면 0을 return해 줍니다..
    if '1' not in code:
        return 0

    for i in range(len(code)-1, -1, -1):
        if code[i] == '1':
            return i


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())  # 세로, 가로

    codes = []
    for _ in range(N):
        barcode = input()
        # 전체가 0으로 이루어진 게 아니면서 // codes에 들어있는 경우가 아니라면 == 처음 등장했음
        if len(barcode) != barcode.count('0') and barcode not in codes:  # 암호가 들어있다는 뜻이다...
            codes.append(barcode)
    # print(codes)  # 들어온 대로 잘 들어있니

    # code 에 있는 애들 그냥 다 이진법으로 바꾸겠습니다.
    hex_word = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
                '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
                'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    binary_codes = []  # 이진법으로 바뀐 스트링을 저장합니다.
    for code in codes:  # 각 줄을 가지고
        binary_code = ''
        for i in range(M):  # 앞/ 뒤 안 잘랐으니까 가로 길이 == M
            binary_code += hex_word[code[i]]  # i 번째를 key 값으로 해서 가져와서 저장합니다.
        binary_codes.append(binary_code)
    # print(binary_codes)  # 일단은 이진법 숫자가 잘 들어있는 것 같습니다..

    # 이 비율을 가지고 답을 알아보겠습니다.
    # 어차피 숫자는 완성될거에요..
    # 숫자가 만들어지고 나서 그게 맞는 암호인지를 검증하는 거거든요
    # 0 비율이 안 맞아서 숫자가 안 될 수는 없을거에요 그래서 맨 앞에 0은 그냥 버릴게용
    num_ratio = {
        (2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4,
        (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9
    }

    found_num = []  # 숫자 8개 만들기
    code_complete = []  # 8개 완성되면 found_num을 여기에 저장하겠다. tc 마다 코드가 여러개 있을 수 있기 때문이죠

    # 2진법으로 만들어 놓은 각 줄을 찬찬히 뜯어봅시다
    # 맨 처음이면 무조건 처음 등장한거 그거 확인하기 위해서 enumerate으로 해주겠습니다.
    # 근데 처음 등장한거 확인을 못했네요..
    for idx, each in enumerate(binary_codes):
        # print('이진숫자: ', each)
        cnt_num = []  # 그래서 몇개니
        cnt = 0  # 몇개까지 세었냐
        now_num = '1'  # 지금 누구를 세고 있나.. 1로 시작합니다..!

        i = ilchatgi(each) +1  # 맨 뒤 1 부터 시작해줄게요

        # 0을 뛰어넘는 걸 못하고 있어요... 외않돼
        while i:  # 0이 되면 종료됩니다.  사실 -1 보다 크다 이렇게 해야 할 거 같은데, 어떤 숫자든 앞에는 무조건 0이라서 무시할거라서 그냥 양수일 때 반복하는 걸로 하겠습니다.
            i -= 1

            # 내가 원하는 비율을 다 찾았는가?
            if len(cnt_num) == 3:
                # print(cnt_num)
                # 그렇다면 비율에 맞춰서 숫자를 찾아줘요
                common_min = min(cnt_num)
                if common_min != 1:  # 1이 아니라면 분명 이걸로 비율 맞춰서 나눠질 것
                    for j in range(3):
                        cnt_num[j] //= common_min  # 제일 작은 걸로 나눈 몫을 저장하겠어요
                # print(cnt_num)
                found_num.append(num_ratio[tuple(cnt_num)])  # 숫자가 found_num에 저장됩니다.
                cnt_num = []
                # 다음 i를 찾아요
                # 이제까지 찾아온 부분의 앞만 확인
                i = ilchatgi(each[:i+1])
                now_num = '1'

                # 만약 숫자를 8개를 다 찾았으면?
                if len(found_num) == 8:
                    if found_num not in code_complete:
                        code_complete.append(found_num)  # 찾은 숫자코드를 저장해줍니다
                    found_num = []

            else:  # 아직 숫자를 다 세지 못했음.  계속 숫자를 셉니다
                if now_num == each[i]:  # 같은 숫자를 세고 있다면, 하나 더 올려준다.
                    cnt += 1

                else:
                    # 다른 숫자로 변했다면, 세던 숫자를 올리고, 다른 숫자 세기 시작
                    cnt_num = [cnt] + cnt_num
                    now_num = each[i]  # 다른 숫자로 바꿔주고
                    cnt = 1
    # print(code_complete)

    ans = 0
    for each in code_complete:
        if ((each[7] + each[5] + each[3] + each[1]) * 3 + each[6] + each[4] + each[2] + each[0]) % 10 == 0:
            ans += sum(each)

    print('#{} {}'.format(tc+1, ans))

