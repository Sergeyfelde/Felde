acts = {'MIX': 'MX', 'WATER': 'WT', 'DUST': 'DT', 'FIRE': 'FR'}
for tst in range(1, 11):
    with open(f'input{tst}.txt') as f:
        input = f.read().splitlines()
    spell = []
    for line in input:
        ing_sp = ''
        act = line.split()[0]
        ing = line.split()[1:]
        act_sp = acts[act]
        for el in ing:
            if el.isdigit():
                ing_sp += spell[int(el) - 1]
            else:
                ing_sp += el
        spell.append(act_sp + ing_sp + act_sp[::-1])
    spell = spell[-1]
    with open(f'output{tst}.txt') as d:
        out = d.readline()
        if spell == out:
            print(f"{tst}. Верно")
            print(spell)
        else:
            print(f"{tst}. Неверно")
            print(f"Программа: {spell}")
            print(f"Ответ: {out}")
