# -*- coding: utf-8 -*-
import simple_draw
import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код
# point = sd.get_point(300, 300)


# def triangle(point, angle=0, length=200):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
#     v3.draw()


# def sqare(point, angle=0, length=200):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()

    # v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    # v2.draw()

    # v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    # v3.draw()

    # v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
    # v4.draw()


# def pentagon(point, angle=0, length=200):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()

    # v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    # v2.draw()

    # v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    # v3.draw()

    # v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    # v4.draw()

    # v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
    # v5.draw()


# def hexagon(point, angle=0, length=200):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()

    # v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    # v2.draw()

    # v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    # v3.draw()

    # v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    # v4.draw()

    # v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
    # v5.draw()

    # v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
    # v6.draw()


# triangle(point=point,angle=10)
# sqare(point=point)
# pentagon(point=point)
# hexagon(point=point)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)


def polygon(number_of_angles, start_point, angle, length, width):
    for i in range(1, number_of_angles+1):
        vector = simple_draw.get_vector(start_point=start_point, angle=angle + (360 / number_of_angles * i),
                                        length=length, width=width)
        vector.draw()
        start_point = vector.end_point
    return vector


def triangle(point, angle, length, width):
    polygon(3, start_point=point, angle=angle, length=length, width=width)


def sqare(point, angle, length, width):
    polygon(4, start_point=point, angle=angle, length=length, width=width)


def pentagon(point, angle, length, width):
    polygon(5, start_point=point, angle=angle, length=length, width=width)


def hexagon(point, angle, length, width):
    polygon(6, start_point=point, angle=angle, length=length, width=width)


triangle(point=simple_draw.get_point(500, 300), angle=5, length=150, width=3)
sqare(point=simple_draw.get_point(200, 300), angle=12, length=100, width=3)
pentagon(point=simple_draw.get_point(500, 50), angle=20, length=100, width=3)
hexagon(point=simple_draw.get_point(200, 50), angle=0, length=100, width=3)
# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
