for tst in range(1, 21):
    if tst < 10:
        tst = '0' + str(tst)
    with open(f'input_s1_{tst}.txt') as f:
        V = [int(i) for i in f.readline().split()]
        P = [int(i) for i in f.readline().split()]
        M = [int(i) for i in f.readline().split()]
    def F(v, p, m):
        Xv = v[0]
        Yv = v[1]
        Zv = v[2]
        Xp = p[0]
        Yp = p[1]
        Zp = p[2]
        Xm = m[0]
        Ym = m[1]
        Zm = m[2]
        if Xp == Xm == Xv or Xp == Xm == 0:
            return ((Yp - Ym) ** 2 + (Zp - Zm) ** 2) ** 0.5
        elif Yp == Ym == Yv or Yp == Ym == 0:
            return ((Xp - Xm) ** 2 + (Zp - Zm) ** 2) ** 0.5
        elif Zp == Zm == Zv or Zp == Zm == 0:
            return ((Yp - Ym) ** 2 + (Xp - Xm) ** 2) ** 0.5
        elif (Xp == Xv or Xp == 0) and Xm != Xp and (Ym == Yv or Ym == 0) and Yp != Ym:
            d = (abs(Xp - Xm) + abs(Yp - Ym))
            return (d ** 2 + (Zp - Zm) ** 2) ** 0.5
        elif (Zp == Zv or Zp == 0) and Zm != Zp and (Ym == Yv or Ym == 0) and Yp != Ym:
            d = (abs(Zp - Zm) + abs(Yp - Ym))
            return (d ** 2 + (Xp - Xm) ** 2) ** 0.5
        elif (Yp == Yv or Yp == 0) and Ym != Yp and (Zm == Zv or Zm == 0) and Zp != Zm:
            d = (abs(Yp - Ym) + abs(Zp - Zm))
            return (d ** 2 + (Xp - Xm) ** 2) ** 0.5
        elif (Xp == Xv or Xp == 0) and Xm != Xp and (Zm == Zv or Zm == 0) and Zp != Zm:
            d = (abs(Xp - Xm) + abs(Zp - Zm))
            return (d ** 2 + (Yp - Ym) ** 2) ** 0.5
        elif (Yp == Yv or Yp == 0) and Ym != Yp and (Xm == Xv or Xm == 0) and Xp != Xm:
            d = (abs(Yp - Ym) + abs(Xp - Xm))
            return (d ** 2 + (Zp - Zm) ** 2) ** 0.5
        elif (Zp == Zv or Zp == 0) and Zm != Zp and (Xm == Xv or Xm == 0) and Xp != Xm:
            d = (abs(Zp - Zm) + abs(Xp - Xm))
            return (d ** 2 + (Yp - Ym) ** 2) ** 0.5
        elif (Xp == Xv and Xm == 0) or (Xp == 0 and Xm == Xv):
            if Zv - Zp + Zv - Zm < Zp + Zm:
                d = (Zv - Zp + Zv - Zm + Xv)
            else:
                d = (Zp + Zm + Xv)
            if Yv - Yp + Yv - Ym < Yp + Ym:
                e = (Yv - Yp + Yv - Ym + Xv)
            else:
                e = (Yp + Yv + Xv)
            if d <= e:
                return (d ** 2 + (Yp - Ym) ** 2) ** 0.5
            else:
                return (e ** 2 + (Zp - Zm) ** 2) ** 0.5
        elif (Yp == Yv and Ym == 0) or (Yp == 0 and Ym == Yv):
            if Zv - Zp + Zv - Zm < Zp + Zm:
                d = (Zv - Zp + Zv - Zm + Yv)
            else:
                d = (Zp + Zm + Yv)
            if Xv - Xp + Xv - Xm < Xp + Xm:
                e = (Xv - Xp + Xv - Xm + Yv)
            else:
                e = (Xp + Xv + Yv)
            if d <= e:
                return (d ** 2 + (Xp - Xm) ** 2) ** 0.5
            else:
                return (e ** 2 + (Zp - Zm) ** 2) ** 0.5
        elif (Zp == Zv and Zm == 0) or (Zp == 0 and Zm == Zv):
            if Yv - Yp + Yv - Ym < Yp + Ym:
                d = (Yv - Yp + Yv - Ym + Zv)
            else:
                d = (Yp + Yv + Zv)
            if Xv - Xp + Xv - Xm < Xp + Xm:
                e = (Xv - Xp + Xv - Xm + Zv)
            else:
                e = (Xp + Xm + Zv)
            if d <= e:
                return (d ** 2 + (Xp - Xm) ** 2) ** 0.5
            else:
                return (e ** 2 + (Yp - Ym) ** 2) ** 0.5
    res = round(F(V, P, M), 3)
    with open(f'output_s1_{tst}.txt') as out:
        out = float(out.readline())
        if res == out:
            print(f'{tst}. Верно')
        else:
            print(f'{tst}. Неверно')
            print(f'{res}')
            print(f'{out}')
