# Лабораторная работа по программированию №3
# 1 семестр; сентябрь 2024 года
# Анчиков Пётр ИУ7-14Б

# Программа:
#   Программа, определяющая стороны треугольника и высоту из меньшего угла по координатам точек


# блок 1 - импортирование библиотеки

from sys import float_info as fi

# блок 2 - ввод исходных значений и проверка точек

x1 = int(input("Введите координату X для первой вершины"))  # ввод координаты X для первой вершины треугольника
y1 = int(input("Введите координату Y для первой вершины"))  # ввод координаты Y для первой вершины треугольника
x2 = int(input("Введите координату X для второй вершины"))  # ввод координаты X для второй вершины треугольника
y2 = int(input("Введите координату Y для второй вершины"))  # ввод координаты Y для второй вершины треугольника
x3 = int(input("Введите координату X для третьей вершины"))  # ввод координаты X для третьей вершины треугольника
y3 = int(input("Введите координату Y для третьей вершины"))  # ввод координаты Y для третьей вершины треугольника

# блок 3 - проверка точек на нахождение на одной прямой

if ((x2 - x1) * (y3 - y2) - (x3 - x2) * (
        y2 - y1)) == 0:  # найдем векторное произведение и определим паралельность A и B
    print("Точки не могут образовать треугольник, так как две прямые лежат на одной прямой")
else:

    # блок 4 - вычисление сторон треугольника по координатам

    ax = abs(x1 - x2)  # разность координат X для первой стороны, которая образует катет c гипотенузой A
    ay = abs(y1 - y2)  # разность координат Y для первой стороны, которая образует катет c гипотенузой A
    a = (ax ** 2 + ay ** 2) ** 0.5  # нахождение первой стороны по теореме Пифагора
    bx = abs(x2 - x3)  # разность координат X для второй стороны, которая образует катет c гипотенузой B
    by = abs(y2 - y3)  # разность координат Y для второй стороны, которая образует катет c гипотенузой B
    b = (bx ** 2 + by ** 2) ** 0.5  # нахождение второй стороны по теореме Пифагора
    cx = abs(x1 - x3)  # разность координат X для третьей стороны, которая образует катет c гипотенузой C
    cy = abs(y1 - y3)  # разность координат Y для третьей стороны, которая образует катет c гипотенузой C
    c = (cx ** 2 + cy ** 2) ** 0.5  # нахождение третьей стороны по теореме Пифагора

    # блок 5 - вычисление косинусов углов треугольника

    corn_a = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)  # косинус угла между сторонами b и c
    corn_b = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)  # косинус угла между сторонами a и c
    corn_c = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)  # косинус угла между сторонами a и b

    # блок 6 - определение наименьшего угла

    if corn_a - corn_b > fi.epsilon:  # определение большего угла из углов a и b
        if corn_a - corn_c > fi.epsilon:  # определение большего угла из углов a и c
            min_corn = corn_a  # сохранение значения косинуса наименьшего угла
            side_3 = a  # сохранение стороны противолежащей наименьшему углу
        else:
            min_corn = corn_c  # сохранение значения косинуса наименьшего угла
            side_3 = c  # сохранение стороны противолежащей наименьшему углу
    else:
        if corn_b - corn_c > fi.epsilon:  # определение большего угла из углов b и c
            min_corn = corn_b  # сохранение значения косинуса наименьшего угла
            side_3 = b  # сохранение стороны противолежащей наименьшему углу
        else:
            min_corn = corn_c  # сохранение значения косинуса наименьшего угла
            side_3 = c  # сохранение стороны противолежащей наименьшему углу

    # блок 7 - вычисление высоты, опущенной из наименьшего угла

    p = (a + b + c) / 2  # нахождение полупериметра треугольника
    h = (2 * (p * (p - a) * (p - b) * (p - c)) ** 0.5) / side_3  # нахождение высоты, опущенной из наименьшего угла

    # блок 8 - вывод величин сторон треугольника и высоты, опущенной из наименьшего угла

    print("Величина стороны a:", "{:g}".format(a))  # вывод величины первой стороны
    print("Величина стороны b:", "{:g}".format(b))  # вывод величины второй стороны
    print("Величина стороны c:", "{:g}".format(c))  # вывод величины третьей стороны
    print("Величина высоты, проведенной из наименьшего угла:", "{:g}".format(h))  # вывод величины высоты

    # блок 9 - определение равнобедренности треугольника

    if (a - b == fi.epsilon) or (b - c == fi.epsilon) or (
            a - c == fi.epsilon):  # проверка треугольника на равнобедренность
        print("Треугольник равнобедренный")
    else:
        print("Треугольник не равнобедренный")

    # блок 10 - ввод координат точки M

    xM = int(input("Введите координату X"))  # ввод координаты X точки M
    yM = int(input("Введите координату Y"))  # ввод координаты Y точки M

    # блок 11 - определение принадлежности точки к оласти треугольника и последующее нахождение расстояния до ближайшей стороны

    if (xM >= x1 or xM >= x2 or xM >= x3) and (xM <= x1 or xM <= x2 or xM <= x3) \
            and (yM >= y1 or yM >= y2 or yM >= y3) and ( \
                    yM <= y1 or yM <= y2 or yM <= y3):  # проверка принадлежности точки к области треугольника
        print("Точка принадлежит области треугольника")
        x1M = abs(x1 - xM)  # катет откладываемый от точки M до точки x1 по координате x
        y1M = abs(y1 - yM)  # катет откладываемый от точки M до точки y1 по координате y
        AM = (x1M ** 2 + y1M ** 2) ** 0.5  # расстояние от точки (x1,y1) до M
        x2M = abs(x2 - xM)  # катет откладываемый от точки M до точки x2 по координате x
        y2M = abs(y2 - yM)  # катет откладываемый от точки M до точки y2 по координате y
        BM = (x2M ** 2 + y2M ** 2) ** 0.5  # расстояние от точки (x2,y2) до M
        x3M = abs(x3 - xM)  # катет откладываемый от точки M до точки x3 по координате x
        y3M = abs(y3 - yM)  # катет откладываемый от точки M до точки y3 по координате y
        CM = (x3M ** 2 + y3M ** 2) ** 0.5  # расстояние от точки (x3,y3) до M
        pAB = (AM + BM + a) / 2  # полупериметр треугольника AMB
        pBC = (BM + CM + b) / 2  # полупериметр треугольника BMC
        pAC = (AM + CM + c) / 2  # полупериметр треугольника AMC
        hAB = (2 * (pAB * (pAB - a) * (p - BM) * (p - AM)) ** 0.5) / a  # высота из точки M до стороны AB
        hBC = (2 * (pBC * (pBC - BM) * (pBC - b) * (pBC - CM)) ** 0.5) / b  # высота из точки M до стороны BС
        hAC = (2 * (pAC * (pAC - AM) * (pAC - CM) * (pAC - c)) ** 0.5) / c  # высота из точки M до стороны AC
        if hAB - hBC > fi.epsilon:  # нахождение минимального расстояния от точки до стороны по трем расстояниям
            if hAC - hBC > fi.epsilon:  # нахождение минимального расстояния от точки до стороны
                h_min = hBC
            else:
                h_min = hAC
        else:
            if hAB - hAC > fi.epsilon:
                h_min = hAC
            else:
                h_min = hAB
        # блок 12 - вывод расстояния от точки до ближайшей стороны
        print("Расстояние от точки до ближайшей стороны:", "{:g}".format(h_min))
    else:
        print("Точка не принадлежит области треугольника")
