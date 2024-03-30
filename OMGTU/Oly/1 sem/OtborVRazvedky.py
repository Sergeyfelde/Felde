import math
for tst in range(1, 11):
    if tst < 10:
        tst = '0' + str(tst)
    with open(f'input_s1_{tst}.txt') as f:
        N = int(f.readline())
        d_2 = int(math.log(N,2))
        res = 0
        if d_2 == 0:
            res = 0
        else:
            res = min(abs(2**d_2-N), abs(2**(d_2+1)-N))
    with open(f'output_s1_{tst}.txt') as d:
        d = int(d.readline())
        if res == d:
            print(f'{tst}. Верно')
        else:
            print(f'{tst}. Неверно')
            print(f'{res}')
            print(f'{d}')
