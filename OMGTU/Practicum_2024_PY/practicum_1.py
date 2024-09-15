import numpy as n


# (п.1)
my_array = n.arange(10, 70, 2)
print("П.1")
print(*my_array)
# (п.2)
new_arr_2 = my_array.reshape(6, 5).T
print("\nП.2")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in new_arr_2]))

# (п.3)
A = new_arr_2.dot(2.5)
A[0] = A[0]-5
A = n.round(A.astype(int))
print("\nП.3")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in A]))

# (п.4)
B = n.random.randint(0, 11, (6, 3))
print("\nП.4")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in B]))

# (п.5)
a = n.sum(A, axis=1)
print("\nП.5")
print(f"Размер вектора a: {n.size(a, axis = 0)}")
b = n.sum(B, axis=0)
print(f"Размер вектора b: {n.size(b, axis = 0)}")

# (п.6)
C = A.dot(B)
print("\nП.6")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in C]))

# (п.7)
A = n.delete(A, 2, axis=1)
B = n.append(B, n.random.randint(10, 21, (6, 3)), axis=1)
print("\nП.7")
print("Матрица A:")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in A]))
print("\nМатрица B:")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in B]))

# (п.8)
det_A = n.linalg.det(A)
det_B = n.linalg.det(B)
print("\nП.8")
print("Определитель A: ", det_A)
print("Определитель B: ", det_B, '\n')

if det_A != 0:
    print("Обратная матрица к A:")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in n.linalg.inv(A)]))
else:
    print("Определитель A равен нулю, нет обратной матрицы\n")

if det_B != 0:
    print("Обратная матрица к B:")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in n.linalg.inv(B).round(3)]))
else:
    print("Определитель B равен нулю, нет обратной матрицы")
n.set_printoptions(precision=3, formatter={'float_kind': '{:0.3f}'.format})
# (п.9)
A = n.linalg.matrix_power(A, 6)
B = n.linalg.matrix_power(B, 14)
print("\nП.9")
print("A в 6 степени: ")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in A]))
print("B в 14 степени: ")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in B]))

# (п.10)
SLU_A = n.array([3, -1.2, -8, 8, 21, -19, 0.5, 0, 7, 0, -4.9, -2, 1, -2, 13, 9]).reshape(4,4)
SLU_b = n.array([20, -8, 11, 3])
SLU_x = n.linalg.solve(SLU_A, SLU_b)
print("\nП.10 Вариант 3")
print(*SLU_x.round(3))

