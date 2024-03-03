n_r = int(input("Введите количество рёбер: "))
r = []
v = set()
for i in range(n_r):
    v1 = input("Введите первую вершину ребра: ")
    v2 = input("Введите вторую вершину ребра: ")
    r.append((v1, v2))
    v.add(v1)
    v.add(v2)
stack_r = []
s_v = []
c_s_v = 0
while len(v) != 0:
    s_v.append({r[0][0]})
    v.remove(r[0][0])
    j = 0
    while j != len(r):
        if len(set(r[j]).intersection(set(s_v[c_s_v]))) > 0:
            stack_r.append(r[j])
            r.remove(r[j])
            j -= 1
        j += 1
    while len(stack_r) != 0:
        s_v[c_s_v].add(stack_r[-1][0])
        s_v[c_s_v].add(stack_r[-1][1])
        if stack_r[-1][0] in v:
            v.remove(stack_r[-1][0])
        if stack_r[-1][1] in v:
            v.remove(stack_r[-1][1])
        st_el = stack_r.pop()
        j = 0
        while j != len(r):
            if len(set(r[j]).intersection(set(st_el))) > 0:
                stack_r.append(r[j])
                r.remove(r[j])
                j -= 1
            j += 1
    c_s_v += 1
print("Список компонент связности: ")
for s in range(len(s_v)):
    print(s_v[s])
