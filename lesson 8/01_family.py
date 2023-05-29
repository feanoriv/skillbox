# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money_in_the_nightstand = 100
        self.food_in_the_fridge = 50
        self.cat_food = 30
        self.dirt = 0

    def __str__(self):
        return f'денег в тумбочке {self.money_in_the_nightstand}, еды в холодильнике {self.food_in_the_fridge}, грязь {self.dirt}'


class Husband:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.happiness = 100
        self.house = home

    def __str__(self):
        return f'{self.name} Сытость {self.fullness}, счастье {self.happiness}'

        # return super().__str__()

    def act(self):
        if self.fullness <= 0:
            cprint(f'💀{self.name} умер от голода💀', color='red')
            return
        elif self.happiness < 10:
            cprint(f'💀{self.name} умер от депрессии💀', color='red')
            return
        if self.house.dirt > 90:
            self.happiness -= 10
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.happiness < 30:
            self.gaming()
        elif dice == 1:
            self.pet_the_cat()
        else:
            self.work()


    def eat(self):
        self.fullness += 30
        self.house.food_in_the_fridge -= 30
        cprint(f'{self.name} покушал. Сытость {self.fullness}, еда в холодильнике {self.house.food_in_the_fridge}',
               color='light_cyan')

    def work(self):
        self.fullness -= 10
        self.house.money_in_the_nightstand += 150
        cprint(f'{self.name} поработал. Деньги {self.house.money_in_the_nightstand}, сытость {self.fullness}',
               color='light_cyan')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        cprint(f'{self.name} поиграл в танки. Счастье {self.happiness}, сытость {self.fullness}', color='light_cyan')

    def pet_the_cat(self):
        self.happiness += 5
        self.fullness -= 10
        cprint(f'{self.name} погладила кота. Счастье {self.house.dirt}', color='light_magenta')


class Wife:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.happiness = 100
        self.house = home


    def __str__(self):
        return f'{self.name} Сытость {self.fullness}, счастье {self.happiness}'

        # return super().__str__()

    def act(self):
        if self.fullness <= 0:
            cprint(f'💀{self.name} умерла от голода💀', color='red')
            return
        elif self.happiness < 10:
            cprint(f'💀{self.name} умерла от депрессии💀', color='red')
            return
        if self.house.dirt > 90:
            self.happiness -= 10
        dice = randint(1, 6)
        if self.house.food_in_the_fridge < 60:
            self.shopping()
        elif self.happiness < 30:
            self.buy_fur_coat()
        elif self.house.cat_food < 20:
            self.buy_cat_food()
        elif self.house.dirt > 110:
            self.clean_house()
        elif dice == 1:
            self.pet_the_cat()
        else:
            self.eat()



    def eat(self):
        self.fullness += 30
        self.house.food_in_the_fridge -= 30
        cprint(f'{self.name} покушалa. Сытость {self.fullness}, еда в холодильнике {self.house.food_in_the_fridge}',
               color='light_magenta')

    def shopping(self):
        self.house.food_in_the_fridge += 150
        self.house.money_in_the_nightstand -= 150
        self.fullness -= 10
        cprint(f'{self.name} купила еды. Сытость {self.fullness}, еда в холодильнике {self.house.food_in_the_fridge}',
               color='light_magenta')

    def buy_fur_coat(self):
        self.happiness += 60
        self.house.money_in_the_nightstand -= 350
        self.fullness -= 10
        cprint(f'{self.name} купила шубу. Счастье {self.happiness}, сытость {self.fullness}', color='light_magenta')

    def clean_house(self):
        self.house.dirt -= 100
        self.fullness -= 10
        cprint(f'{self.name} убрала дом. Грязь {self.house.dirt}, сытость {self.fullness}', color='light_magenta')
    def pet_the_cat(self):
        self.happiness += 5
        self.fullness -= 10
        cprint(f'{self.name} погладила кота. Счастье {self.house.dirt}', color='light_magenta')

    def buy_cat_food(self):
        self.house.money_in_the_nightstand -= 50
        self.house.cat_food += 50

class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = home

    def __str__(self):
        return f'{self.name} Сытость {self.fullness}'


    def act(self):
        if self.fullness <= 0:
            cprint(f'💀{self.name} умер от голода💀', color='red')
        if self.fullness < 20:
            self.eat()
            return
        dice = randint(1, 6)
        if dice == 1:
            self.soil()
        else:
            self.sleep()


    def eat(self):
        self.fullness += 40
        self.house.cat_food -= 20
        print(f'{self.name} покушал. Сытость {self.fullness}')
    def sleep(self):
        self.fullness -= 10
        print(f'{self.name} спал целый день. Сытость {self.fullness}')

    def soil(self):
        self.fullness -= 10
        self.house.dirt += 10
        print(f'{self.name} подрал обои. Грязь {self.house.dirt}')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
hulk = Cat(name='Халк')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    hulk.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')
    cprint(hulk, color='cyan')
    home.dirt += 5
print()

# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов
#
#
# class Cat:
#
#     def __init__(self, name):
#         self.name = name
#         self.fullness = 30
#
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

