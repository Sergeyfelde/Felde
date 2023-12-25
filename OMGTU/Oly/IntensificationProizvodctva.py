import datetime
for tst in range(1, 9):
    with open(f'input_s1_0{tst}.txt') as f:
        date1 = [int(x) for x in f.readline().split('.')]
        date2 = [int(x) for x in f.readline().split('.')]
        P = int(f.readline())
        date1.reverse()
        date2.reverse()
    days_delta = (datetime.date(*date2) - datetime.date(*date1)).days
    res = int(sum(range(P, P + days_delta + 1)))
    with open(f'output_s1_0{tst}.txt') as d:
        d = int(d.readline())
        if res == d:
            print(f'{tst}. Верно')
        else:
            print(f'{tst}. Неверно')
