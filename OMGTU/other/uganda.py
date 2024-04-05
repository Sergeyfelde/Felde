def menu():
    print("1) Начать \n2) Условия задачи \n3) Об авторе \n4) Выход")
    m = input("Выберите действие: ")
    match m:
        case "1":
            print("Стартуем")
        case "2":
            kto = "idk"
            explanation(kto)
        case "3":
            kto = "ia"
            explanation(kto)
        case "4":
            leave = True
            return leave

def explanation(kto):
    match kto:
        case "idk":
            print("Поясняем")
        case "ia":
            print("Я")
def alg:
    with open('rgr_test.txt') as op:
        f = op.readline()
while (menu() != True):
    menu()