# Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу, которая выводит след заданной квадратной матрицы.
#
# Формат входных данных
# На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести одно число — след заданной матрицы.s
n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
d_sum = 0
for i in range(n):
    for j in range(n):
        if i == j:
            d_sum += matrix[i][j]
print(d_sum)