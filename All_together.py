from time import sleep
import numpy


def Enter_of_matrix(kind_of_matrix):
    rows = int(input('Введите размерность матррицы (rows x columns): rows _'))
    cols = int(input('                                            columns _'))
    if kind_of_matrix == 2:
        if colsA != rows:
            return "xxx"
    s = '  '
    p = '  '
    for i in range(cols):
        s += str(i + 1) + ' '
        p += '--'
    flag = True
    while flag:
        array = []
        print(s)
        print(p)
        for j in range(rows):
            row = input(str(j + 1) + '|').split()
            check = 0
            for k in range(len(row)):
                if row[k].isdigit() or (row[k][0] == '-' and row[k][1:].isdigit()):
                    check += 1
            if check != cols:
                print('Некорректный ввод матрицы')
                break
            else:
                row = list(map(int, row))
                array.append(row)
            if len(array) == rows:
                flag = False
    if kind_of_matrix == 1:
        return array, rows, cols
    else:
        return array


def Correct_Trans(array):
    trans_array = []
    for i in range(len(array[0])):
        s = []
        for j in range(len(array)):
            s.append(array[j][i])
        trans_array.append(s)
    return trans_array

def Multi(array1, array2):
    multi_array = []
    correct_ar2 = Correct_Trans(array2)
    for i in range(len(array1)):
        remember_array = []
        for j in range(len(correct_ar2)):
            value = 0
            for k in range(len(array1[i])):
                value += array1[i][k] * correct_ar2[j][k]
            remember_array.append(value)
        multi_array.append(remember_array)
    return multi_array




def SwapRows(A, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]


def DivideRow(A, row, divider):
    if divider == 0:
        pass
    else:
        A[row] = [a / divider for a in A[row]]



def CombineRows(A, row, source_row, weight):
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]


def Gauss(A):
    column = 0
    while (column < len(A)): # поиск максимального по модулю значения в (column + 1)-ом столбце
        current_row = None
        for r in range(column, len(A)):
            if current_row is None or abs(A[r][column]) > abs(A[current_row][column]):
                 current_row = r
        if current_row is None:
            print("решений нет")
            return None
        if current_row != column: # переставляем строчку с найденным элементом повыше
            SwapRows(A, current_row, column)
        DivideRow(A, column, A[column][column]) # упрощаем нашу строку
        for r in range(column + 1, len(A)):
            CombineRows(A, r, column, -A[r][column]) # обрабатываем строки лежащие ниже
        column += 1
    return A # возвращаем новый массив


s = 'Здравствуйте, сегодня мы с Вами поработаем с матрицами.'
sleep(0.5)
print(s)
sleep(0.5)
for i in range(3):
    sleep(0.5)
    print('. ', end='')
sleep(0.5)
print('', end='\n')
print('Давайте начнём с ввода матрицы!')
sleep(0.5)

array, rowsA, colsA = Enter_of_matrix(1)

sleep(0.5)
print('И так, Вы ввели следующую матрицу:')
print()
for i in range(len(array)):
    print(*array[i])
print()

print('Что Вы хотите сделать с матрицей?')
insert = int(input('1 - Транспонировать. 2 - Найти произведение. 3 - Определить ранг. 4 - Закончить. Ваш ответ _'))
while insert != 4:
    if insert == 1:
        print('Вот итог нашего с Вами транспонирования:')
        print()
        print('\n'.join(str(Correct_Trans(array))[2:-2].split("], [")).replace(',', ''))
        print()
    elif insert == 2:
        print('')

        print('Давайте введём матрицу-множитель!')
        sleep(0.5)
        second_array = Enter_of_matrix(2)
        sleep(0.5)
        if second_array == "xxx":
            print("Неверная размерность матрицы-множителя")
        else:
            print('И так, Вы ввели следующую матрицу-множитель:')
            print()
            for i in range(len(second_array)):
                print(*second_array[i])
            print()
            print("Вот результат нашего умножения:")
            print()
            print('\n'.join(str(Multi(array, second_array))[2:-2].split("], [")).replace(',', ''))
            print()
    elif insert == 3:
        myA = list(array)
        numpy_array = numpy.matrix(myA)
        if myA == [([0] * len(myA[0]))] * len(myA):
            print(0)
        else:
            if len(myA) > len(myA[0]):
                myA = Correct_Trans(myA)
            myA = Gauss(myA)
            help_array = []
            for i in range(len(myA)):
                if myA[i] != [0] * len(myA[0]):  # проверяем на нулевую строку
                    help_array.append(myA[i])
            myA = list(help_array)
            y_y = min(len(myA), len(myA[0]))
            print('Определённый нами ранг:')
            print(y_y)
            print('Ранг определённый numpy:')
            print(numpy.linalg.matrix_rank(numpy_array))


    print('Что Вы хотите сделать с матрицей?')
    insert = int(input('1 - Транспонировать. 2 - Найти произведение. 3 - Определить ранг. 4 - Закончить. Ваш ответ _'))

sleep(0.5)
print('Было приятно с Вами поработать!')
sleep(1)