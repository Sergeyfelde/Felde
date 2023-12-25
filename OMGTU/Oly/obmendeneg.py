for tst in range(1, 15):
    with open(f'input{tst}.txt') as f:
        NI, KI, NK, KK, E = [list(map(int, f.readline().split())) for i in range(5)]
        KI = [KI[0]] + sorted(KI[1:], reverse=True)
        KK = [KK[0]] + sorted(KK[1:])
        ml = 0
        res = [0] * NK[0]
    for i in range(NI[0]):          #перевод к сумме с несчастливыми цифрами
        for j in range(KI[0]):
            if E[i] >= KI[j+1]:
                E[i] -= 1
    NI.append(1)
    NI.append(1)
    for i in range(NI[0]-1, -1, -1): #перевод к младшим единицам
        NI[i+1] *= NI[i+2]
        ml += NI[i+1] * E[i]
    NK.insert(1, 1000000)
    for i in range(NK[0]-1, -1, -1): #перевод к старшим единицам
        res[i] = ml % NK[i+1]
        ml //= NK[i+1]
    for i in range(NK[0]):           #перевод к сумме без несчастливых цифр
        for j in range(KK[0]):
            if res[i] >= KK[j+1]:
                res[i] += 1
    res = ' '.join(map(str, res))
    with open(f'output{tst}.txt') as d:
        d = d.readline()
        if res == d:
            print(f'{tst}. Верно')
        else:
            print(f'{tst}. Неверно')
            print('res', res)
            print('d  ', d)
