# Лабораторная работа по программированию №2
# 1 семестр; сентябрь 2024 года
# Анчиков Пётр ИУ7-14Б

# Программа по:
#   Программа для решения квадратного уравнения


# блок 1 - ввод исходных значений

a = float(input("Введите коэффицент a:"))

b = float(input("Введите коэффицент b:"))

c = float(input("Введите коэффицент c:"))

# Блок 2 - проверка коэффицентов, выполнение основных вычислений
# и вывод корней квадратного уравнения

if a == 0:  # проверка коэффицента a
    if b == 0:  # проверка коэффицента b
        print("x принадлежит промежутку от -∞ до +∞")  # вывод промежутка которому принадлежит x
    else:
        x = (c * (-1)) / b  # нахождение корня линейной функции
        print("Корень уравнения:", "{:g}".format(x))  # вывод корня линейной функции
else:
    D = b ** 2 - 4 * a * c  # нахождение дискриминанта
    if D < 0:  # проверка дискриминанта
        print("Уравнение не имеет решений")  # вывод что уравнение не имеет решений
    else:
        if D == 0:  # проверка количества корней
            x = (b * (-1)) / (2 * a)  # нахождение единственного корня квадратного уравнения
            print("Корень уравнения:", "{:g}".format(x))  # вывод единственного корня квадратного уравнения
        else:
            x1 = (b * (-1) + D ** 0.5) / (2 * a)  # нахождение первого корня квадратного уравнения
            x2 = (b * (-1) - D ** 0.5) / (2 * a)  # нахождение второго корня квадратного уравнения
            print("Первый корень:", "{:g}".format(x1))  # вывод первого корня квадратного уравнения
            print("Второй корень:", "{:g}".format(x2))  # вывод второго корня квадратного уравнения
