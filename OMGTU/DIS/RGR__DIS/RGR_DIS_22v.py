def Menu():
    print("1) Начать \n2) Условия задачи \n3) Об авторе \n4) Выход")
    m = input("Выберите действие: ")
    match m:
        case "1":
            print(Alg())
            Create()
        case "2":
            print("В стране Угандии построили аттракцион 'Лабиринт знаний'.\nЛабиринт представляет собой N комнат, пронумерованных от\n1 до N, между некоторыми из которых есть двери.\nКогда человек проходит через дверь, показатель его знаний\nизменяется на определенную величину, фиксированную для данной двери.\nВход в лабиринт находится в комнате 1, выход - в комнате N.\nКаждый человек проходит лабиринт ровно один раз.\nОпределить наилучший результат, который можно набрать при прохождение лабиринта.")
        case "3":
            print("Фельде Сергей Дмитриевич\nСтудент группы ФИТ-231\nОМГТУ 2024")
        case "4":
            exit()
def Alg():
    def get_connects(vershina):
        lst = []
        for elem in data:
            if elem[0][1] == vershina:
                lst.append(elem)
        return lst
    with open('rgr_test.txt') as f:
        try:
            N_M = [int(x) for x in f.readline().split()]
            N = N_M[0]
            M = N_M[1]
        except ValueError:
            output = 'Неправильный ввод'
            return output
        if N > 2000 or M > 10000 or N < 1 or M < 0:
            output = 'Неправильный ввод'
            return output
        data = []
        cur_v = set()
        for i in range(M):
            try:
                nums = [int(x) for x in f.readline().split()]
            except ValueError:
                output = 'Неправильный ввод'
                return output
            cur_v.add(nums[0])
            cur_v.add(nums[1])
            w = -int(nums[2])
            if abs(w) > 10000:
                output = 'Неправильный ввод'
                return output
            data.append((nums, w))
        if f.readline() != '':
            output = 'Неправильный ввод'
            return output
        if M == 0:
            output = 'Лабиринт нельзя пройти'
            return output
        prev_list, cur_list = [], []
        for i in range(N):
            prev_list.append('inf')
            cur_list.append('inf')
        cur_v = sorted(list(cur_v))
        o = min(cur_v)
        start_v = 1
        cur_list[start_v - o] = 0
        dests = {}
        for v in cur_v:
            dests[v] = 'inf'
            if v == start_v:
                dests[v] = 0
        iteration = 0
        no_otriz = True
        while True:
            has_changed = False
            for ver in cur_v:
                if ver == start_v:
                    continue
                v_list = get_connects(ver)
                if v_list:
                    for elem in v_list:
                        if dests[elem[0][0]] != 'inf':
                            if cur_list[ver - o] == 'inf':
                                way_len = elem[1] + dests[elem[0][0]]
                                cur_list[ver - o] = way_len, elem[0][0]
                                dests[ver] = way_len
                            else:
                                way_len = elem[1] + dests[elem[0][0]]
                                if way_len < cur_list[ver - o][0]:
                                    cur_list[ver - o] = way_len, elem[0][0]
                                    dests[ver - 0] = way_len
            if prev_list != cur_list:
                has_changed = True
            if has_changed and iteration == N:
                output = 'Бесконечное количество набранных знаний'
                no_otriz = False
                break
            if not has_changed:
                break
            iteration += 1
            prev_list = cur_list[:]
        if no_otriz:
            if N in dests:
                output = f'Максимальное количество набранных знаний - {-dests[N]}'
            else:
                output = 'Лабиринт нельзя пройти'
        return output
def Create():
    rgr_output = open("rgr_output.txt", "w+")
    rgr_output.write(Alg())
    rgr_output.close()
while True:
    Menu()