n_r = int(input("Введите количество рёбер: "))
r = []
for i in range(n_r):
    r.append((input("Введите первую вершину ребра: "), input("Введите вторую вершину ребра: "), int(input("Введите вес ребра: "))))
r2 = []
s = []
res = 0
end_of_l = False
end_of_a = False
not_s = False
for i in range(n_r):
    if i == 0:
        for k in range(n_r):
            if (r[i][0] == r[k][0]) or (r[i][0] == r[k][1]):
                s.append(r[k])
        r2 = [sorted(s, key=lambda x: x[2])[0]]
        s.remove(sorted(s, key=lambda x: x[2])[0])
    else:
        for j in range(len(r2)):
            if (r[i][0] == r2[j][0]) or (r[i][0] == r2[j][1]):
                for w in range(len(r2)):
                    if (r[i][1] == r2[w][1]) or (r[i][1] == r2[w][0]):
                        break
                    else:
                        for l in range(n_r):
                            end_of_l = False
                            for m in range(len(r2)):
                                if (r[l][0] == r2[m][0]) or (r[l][0] == r2[m][1]):
                                    for v in range(len(r2)):
                                        if (r[l][1] == r2[v][0]) or (r[l][1] == r2[v][1]):
                                            end_of_l = True
                                            break
                                    if end_of_l:
                                        break
                                    if (r[l] not in s) and (r[l] not in r2):
                                        for a in range(len(s)):
                                            if r[l][1] == s[a][0] or r[l][1] == s[a][1]:
                                                if r[l][2] >= s[a][2]:
                                                    end_of_a = True
                                                else:
                                                    s.remove(s[a])
                                                break
                                        if not end_of_a:
                                            s.append(r[l])
                                            not_s = False
                                        end_of_a = False
                                elif (r[l][1] == r2[m][0]) or (r[l][1] == r2[m][1]):
                                    for v in range(len(r2)):
                                        if (r[l][0] == r2[v][1]) or (r[l][0] == r2[v][0]):
                                            end_of_l = True
                                            break
                                    if end_of_l:
                                        break
                                    if (r[l] not in s) and (r[l] not in r2):
                                        for a in range(len(s)):
                                            if r[l][0] == s[a][0] or r[l][0] == s[a][1]:
                                                if r[l][2] >= s[a][2]:
                                                    end_of_a = True
                                                else:
                                                    s.remove(s[a])
                                                break
                                        if not end_of_a:
                                            s.append(r[l])
                                            not_s = False
                                        end_of_a = False
                        if (not not_s) and (s != []):
                            r2.append(sorted(s, key=lambda x: x[2])[0])
                            s.remove(sorted(s, key=lambda x: x[2])[0])
                            break
                        else:
                            not_s = False
            elif (r[i][1] == r2[j][1]) or (r[i][1] == r2[j][0]):
                for w in range(len(r2)):
                    if (r[i][0] == r2[w][0]) or (r[i][0] == r2[w][1]):
                        break
                    else:
                        for l in range(n_r):
                            end_of_l = False
                            for m in range(len(r2)):
                                if (r[l][0] == r2[m][0]) or (r[l][0] == r2[m][1]):
                                    for v in range(len(r2)):
                                        if (r[l][1] == r2[v][0]) or (r[l][1] == r2[v][1]):
                                            end_of_l = True
                                            break
                                    if end_of_l:
                                        break
                                    if (r[l] not in s) and (r[l] not in r2):
                                        for a in range(len(s)):
                                            if r[l][1] == s[a][0] or r[l][1] == s[a][1]:
                                                if r[l][2] >= s[a][2]:
                                                    end_of_a = True
                                                else:
                                                    s.remove(s[a])
                                                break
                                        if not end_of_a:
                                            s.append(r[l])
                                            not_s = False
                                        end_of_a = False
                                elif (r[l][1] == r2[m][0]) or (r[l][1] == r2[m][1]):
                                    for v in range(len(r2)):
                                        if (r[l][0] == r2[v][0]) or (r[l][0] == r2[v][1]):
                                            end_of_l = True
                                            break
                                    if end_of_l:
                                        break
                                    if (r[l] not in s) and (r[l] not in r2):
                                        for a in range(len(s)):
                                            if r[l][0] == s[a][0] or r[l][0] == s[a][1]:
                                                if r[l][2] >= s[a][2]:
                                                    end_of_a = True
                                                else:
                                                    s.remove(s[a])
                                                break
                                        if not end_of_a:
                                            s.append(r[l])
                                            not_s = False
                                        end_of_a = False
                        if (not not_s) and (s != []):
                            r2.append(sorted(s, key=lambda x: x[2])[0])
                            s.remove(sorted(s, key=lambda x: x[2])[0])
                            break
                        else:
                            not_s = False
for q in range(len(r2)):
    res += r2[q][2]
print("Список выбранных рёбер: ", r2)
print("Сумма: ", res)
