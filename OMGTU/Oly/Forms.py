for tst in range(1, 20):
    with open(f'input{tst}.txt') as f:
        N = int(f.readline())
        full = []
        half = []
        for i in range(N):
            full.append(f.readline().replace('\n', '').split(' '))
        for i in range(N*2):
            half.append(f.readline().replace('\n', '').split(' '))
    ans = []
    res2 = []
    for i in range(N):
        res0 = []
        res1 = []
        for j in range(N*2):
            if full[i][5:10] == half[j][:5] and full[i][:5] == half[j][5:10] and full[i][-5:] == half[j][-5:]:
                res0.extend((j+1, '0'))
            elif full[i][5:10] == list(reversed(half[j][-5:])) and full[i][:5] == list(reversed(half[j][5:10])) and full[i][-5:] == list(reversed(half[j][:5])):
                res0.extend((j+1, '0'))
            elif full[i][5:10] == list(reversed(half[j][:5])) and full[i][10:15] == list(reversed(half[j][5:10])) and full[i][-5:] == list(reversed(half[j][-5:])):
                res0.extend((j+1, '2'))
            elif full[i][:5] == half[j][-5:] and full[i][5:10] == half[j][5:10] and full[i][10:15] == half[j][:5]:
                res0.extend((j+1, '1'))
            elif full[i][:5] == list(reversed(half[j][:5])) and full[i][5:10] == list(reversed(half[j][5:10])) and full[i][10:15] == list(reversed(half[j][-5:])):
                res0.extend((j+1, '1'))
            elif full[i][5:10] == half[j][-5:] and full[i][10:15] == half[j][5:10] and full[i][-5:] == half[j][:5]:
                res0.extend((j+1, '2'))
            elif full[i][:5] == half[j][:5] and full[i][-5:] == half[j][5:10] and full[i][10:15] == half[j][-5:]:
                res0.extend((j+1, '3'))
            elif full[i][:5] == list(reversed(half[j][-5:])) and full[i][-5:] == list(reversed(half[j][5:10])) and full[i][10:15] == list(reversed(half[j][:5])):
                res0.extend((j+1, '3'))
        for k in range(0, len(res0), 2):
            for l in range(0, len(res0), 2):
                if k < l:
                    if (half[res0[k]-1][:5] == list(reversed(half[res0[l]-1][:5])) and half[res0[k]-1][-5:] == list(reversed(half[res0[l]-1][-5:]))) or (half[res0[k]-1][:5] == half[res0[l]-1][-5:] and half[res0[k]-1][-5:] == half[res0[l]-1][:5]):
                        if res0[k+1] == '0' and res0[l+1] == '2' or res0[k+1] == '1' and res0[l+1] == '3' or res0[k+1] == '2' and res0[l+1] == '0' or res0[k+1] == '3' and res0[l+1] == '1':
                            res1.append([res0[k], res0[l]])
        res2.append(res1)
    for i in range(len(res2)):
        if len(res2[i]) == 1:
            ans.extend(res2[i])
        else:
            ans.append([])
    for i in range(len(res2)):
        if len(res2[i]) != 1:
            for j in range(len(res2[i])):
                for k in range(0, len(res2[i][j]), 2):
                    if res2[i][j][k] in [x for a in range(len(ans)) for x in ans[a]] or res2[i][j][k+1] in [x for a in range(len(ans)) for x in ans[a]]:
                        break
                    else:
                        ans[i].extend((res2[i][j][k], res2[i][j][k+1]))
    with open(f'output{tst}.txt') as d:
        pr = 1
        for i in range(N):
            out = d.readline().replace('\n', '').split(' ')
            for j in range(2):
                if int(ans[i][j]) == int(out[j]):
                    pr *= 1
                else:
                    pr *= 0
                    print(f'ERROR {ans[i]}')
                    print(f'ERROR {out}')
        if pr == 1:
            print(f"{tst}. Верно")
        else:
            print(f"{tst}. Неверно")
