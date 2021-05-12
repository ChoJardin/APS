T = int(input())

for tc in range(T):
    geoseureum = int(input())

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    use = [0, 0, 0, 0, 0, 0, 0, 0]

    for idx, each in enumerate(money):
        while geoseureum >= each:
            geoseureum -= each
            use[idx] += 1

    print('#{}'.format(tc+1))
    for i in use:
        print(i, end=' ')
    print()
