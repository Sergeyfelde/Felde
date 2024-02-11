n_v = int(input("Введите количество вершин: "))
n_r = int(input("Введите количество рёбер: "))
r = []
for i in range(n_r):
    r.append((int(input("Введите первую вершину ребра: ")), int(input("Введите вторую вершину ребра: ")), int(input("Введите вес ребра: "))))
    print("Список в цикле: ", r)
r.sort(key=lambda x: x[2])
print("Сортированный список: ", r)
r2 = []
res = 0
ok = True
b = False
end_of_i = False

for i in range(n_r):
    end_of_i = False
    if i == 0:
        r2.append([r[i]])
    else:
        for j in range(len(r2)):
            a = False
            for k in range(len(r2[j])):
                if (r[i][0] == r2[j][k][0]) or (r[i][0] == r2[j][k][1]):
                    for l in range(len(r2[j])):
                        if (r[i][1] == r2[j][l][0]) or (r[i][1] == r2[j][l][1]):
                            a = True
                            b = False
                            break
                    if not a:
                        for m in range(len(r2)):
                            if not b:
                                for x in range(len(r2[m])):
                                    if (r[i][1] == r2[m][x][0]) or (r[i][1] == r2[m][x][0]):
                                        r2 = [list(set(r2[m] + r2[j]))]
                                        b = True
                                        end_of_i = True
                                        break
                        if not b:
                            r2[j].append(r[i])
                            ok = True
                            end_of_i = True
                            break
                    else:
                        ok = True
                        end_of_i = True
                        break
                elif (r[i][1] == r2[j][k][0]) or (r[i][1] == r2[j][k][1]):
                    for n in range(len(r2[j])):
                        if (r[i][0] == r2[j][n][0]) or (r[i][0] == r2[j][n][1]):
                            a = True
                            b = False
                            break
                    if not a:
                        for p in range(len(r2)):
                            if not b:
                                for y in range(len(r2[p])):
                                    if (r[i][0] == r2[p][y][0]) or (r[i][0] == r2[p][y][0]):
                                        r2 = [list(set(r2[p] + r2[j]))]
                                        b = True
                                        end_of_i = True
                                        break
                                if end_of_i:
                                    break
                        if not b:
                            r2[j].append(r[i])
                            ok = True
                            end_of_i = True
                            break
                    else:
                        ok = True
                        end_of_i = True
                        break
                    if end_of_i:
                        break
    if not ok:
        r2.append([r[i]])
    ok = False
for q in range(len(r2[0])):
    res += r2[0][q][2]
print("Список r2: ", r2)
print("Сумма: ", res)