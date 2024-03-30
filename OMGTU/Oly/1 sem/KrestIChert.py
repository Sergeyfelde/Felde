print('Введите MaxN:')
MaxN = int(input())
res = 0
for i in range(1, MaxN + 1):
    for j in range(2, 18):
        if i % (2 ** j - 1) == 0:
            res += 1
res += MaxN
print(f'Количество комбинаций: {res}')
