'''
0 = 0001101
1 = 0011001
2 = 0010011
3 = 0111101
4 = 0100011
5 = 0110001
6 = 0101111
7 = 0111011
8 = 0110111
9 = 0001011
'''

def find_code():
    # 코드가 끝나는 부분의 인덱스를 저장
    for i in range(N):
        for j in range(M - 1, -1, -1):  # 뒤부터 확인
            if arr[i][j] == 1:  # 암호의 끝
                return (i, j)

def decode():

    # 암호규칙
    regle = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }

    y, x = code[0], code[1]

    nums = []
    change = 0
    num = ''
    for i in range(56):  # 7 * 8 만큼 반복
        change += 1

        num = str(arr[y][x-i]) + num
        if change % 7 == 0:
            nums.append(num)
            num = ''

    print(nums)

    found = []  # 슷자 변환 암호 저장
    for num in nums:
        found = [regle[num]] + found

    # 홀수 자리의 합 * 3 + 짝수자리의 합 + 검증코드 == 10의 배수
    if not ((found[0]+found[2]+found[4]+found[6]) * 3 + (found[1]+found[3]+found[5]) + found[7]) % 10:
        return sum(found)

    return 0  # 만약 암호를 찾지 못했다면 -1 이


# 정상적인 암호 코드들에 포함된 숫자들의 합을 출력

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    arr = [list(map(int, input())) for _ in range(N)]

    code = find_code()

    # 암호는 7개가 한 숫자를 이루고, 총 8개의 숫자로 이루어져 있다. 즉 64개의 숫자를 사용하게 됨
    # code 에 저장된 각 인덱스를 가지고, 56개를 확인해서 하나의 암호를 구성한 후, 그 암호가 유효한지 확인하자
    # 이건 중간에 찐 암호 찾으면 끝내야 하니까 함수 활용한다.

    ans = decode()

    print('#{} {}'.format(tc+1, ans))