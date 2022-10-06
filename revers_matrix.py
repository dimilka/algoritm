""" (1) Исходя из необходимости анализировать время выполнения программы, код будет работать с заранее верно введённой
 матрицей размерностью 3 на 3, взятой из файла Matrix(i).txt, где (i) - 1,2..."""

import timeit
import numpy


def Enter_of_matrix():
    print('Введите матрицу 3x3:')
    flag = True
    while flag:
        array = []
        for j in range(3):
            row = input().split()
            check = 0
            for k in range(len(row)):
                if row[k].isdigit() or (row[k][0] == '-' and row[k][1:].isdigit()):
                    check += 1
            if check != 3:
                print('Некорректный ввод матрицы')
                break
            else:
                row = list(map(int, row))
                array.append(row)
            if len(array) == 3:
                flag = False
    return array


def Drobi(a, b): # Функция для записи значений обратной матрицы в виде правильных дробей
    ost = a % b
    if ost == 0:
        return a // b
    else:
        if a // b == 0:
            return '[' + str(ost) + '/' + str(b) + ']'
        else:
            return str(a // b) + '[' + str(ost) + '/' + str(b) + ']'


def Correct_Trans(a, b): # Функция для транспонирования матрицы алгебраических дополнений
    trans_array = []
    for i in range(len(a[0])):
        s = []
        for j in range(len(a)):
            s.append(Drobi(a[j][i], b))
        trans_array.append(s)
    return trans_array


array = Enter_of_matrix()

start_my = timeit.default_timer() # начало отсчёта времени выполнения рукописного алгоритма
array_char = array[0][0] * array[1][1] * array[2][2] + array[1][0] *\
             array[2][1] * array[0][2] + array[0][1] * array[1][2] * array[2][0]
array_char = array_char - (array[2][0] * array[1][1] * array[0][2] +
                           array[0][1] * array[1][0] * array[2][2] + array[2][1] * array[1][2] * array[0][0])
flag = False
if array_char == 0:
    print('ERROR MATRIX')
else:
    flag = True
if flag:
    alg_dop_array = []
    s1 = [array[1][1] * array[2][2] - array[2][1] * array[1][2],
          -(array[1][0] * array[2][2] - array[2][0] * array[1][2]),
          array[1][0] * array[2][1] - array[2][0] * array[1][1]]
    s2 = [-(array[0][1] * array[2][2] - array[2][1] * array[0][2]),
          array[0][0] * array[2][2] - array[2][0] * array[0][2],
          -(array[0][0] * array[2][1] - array[2][0] * array[0][1])]
    s3 = [array[0][1] * array[1][2] - array[1][1] * array[0][2],
          -(array[0][0] * array[1][2] - array[1][0] * array[0][2]),
          array[0][0] * array[1][1] - array[1][0] * array[0][1]]
    alg_dop_array.append(s1)
    alg_dop_array.append(s2)
    alg_dop_array.append(s3)
    koeff = array_char
    second_array = Correct_Trans(array, koeff)
    print('\n'.join(str(Correct_Trans(alg_dop_array, koeff))[2:-2].split("], [")).replace("', '", ' ').replace("'", '').replace(',', ''))
""" (2) Ввиду того, что вывод полученной матрицы не относится к функциональной части алгоритма, а лишь демонстрирует
    результат работы данного алгоритма, закомментим его, как элемент, "портящий" временной показатель.
    Верность работы алгоритма легко проверить, сняв символ "#" с print."""
time_my = timeit.default_timer() - start_my  # временя выполнения рукописного алгоритма
time_my = float(str(time_my)[:-4]) * (10 ** -5)


start_numpy = timeit.default_timer() # начало отсчёта времени выполнения кода при использовании numpy
array_for_numpy = numpy.linalg.inv(array)
print(array_for_numpy)
""" Комментирование вывода аналогичное (2)"""
time_numpy = timeit.default_timer() - start_numpy # временя выполнения кода при использовании numpy

print(time_my)
print(time_numpy)
print(time_my-time_numpy)

""" P.S. при формировании правильных дробей целая часть выносится перед [], дробная - находится внутри [].
    Формирование правильных дробей не является обязательным, однако предоставляет пользователю наглядное представление
    результатов, сранимое с результатами, получаемыми в ходе ручного решения. """