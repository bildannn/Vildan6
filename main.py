
# class DataBase:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance == super().__new__(cls)
#         return cls.__instance
#
#     def __int__(self, user, password, port):
#         self.user = user
#         self.password = password
#         self.port = port
#
#     def __del__(self):
#         print('hbgr')
#         DataBase.__instance = None
#
#     def connect(self):
#         print(f'соединение с БД: {self.user}, {self.password}, {self.port}')
#
#     def close(self):
#         print('соединение разорвано')
#
#     def read(self):
#         print('чтение данных')
#
#     def write(self):
#         print(f'Записываем данные {data}')
#
# db = DataBase('user1', 'psw1', '80000' )
# db2 = DataBase('user1', 'psw1', '80000' )
# print(db)
# print(db2)




# class Test:
#     pass
#     def __bool__(self):
#
#         return 464634354>673465
#
# t = Test()
# if t:
#     print('fjgdg')



# class Clock:
#     __DAY = 86400
#
#     def __init__(self, seconds  : int):
#         if not isinstance(seconds, int):
#             raise TypeError('Нужно вести целое чило!')
#         self.seconds = seconds % self.__DAY
#
#     def get_time(self):
#         s =  self.seconds % 60
#         m = self.seconds // 60 % 60
#         h = self.seconds // 3600 % 24
#         return f'{h} : {m} : {s}'
#
#     def __eq__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError('Нужно вести целое число')
#         # if isinstance(other, int):
#         #     other = other
#         # else:
#         #     other = other.seconds
#         p = 5**8
#         sc = other if isinstance(other, int) else other.seconds
#         return self.seconds == sc
#
#     def __lt__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError('Type Error')
#         sc = other if isinstance(other, int) else other.seconds
#         return self.seconds < sc
#
#     def __le__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError('Type Error')
#         sc = other if isinstance(other, int) else other.seconds
#         return self.seconds <= sc
#
#     def __mul__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError('Не можем сложить')
#
#         return Clock(self.seconds * other)
#
#
# cl = Clock(86401)
# cl2 = Clock(54)
# cl3 = Clock(155)
# print(cl.get_time())
# cl = cl * 3
# print(cl.get_time())



# class Passport:
#
#     def __init__(self, first_name, last_name, country, date_ot_birth, num_of_passport):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.country = country
#         self.date_ot_birth = date_ot_birth
#         self.num_of_passport = num_of_passport
#
#     def printInfo(self):
#         print(f'''
# Full name: {self.first_name} {self.last_name}
# Date of Birth: {self.date_ot_birth}
# Country: {self.country}
# Passport: {self.num_of_passport}''')
#
#     def __repr__(self):
#         return f'name {self.first_name} {self.last_name}, Passport {self.num_of_passport}'
#
#
# class ForeignPassport(Passport):
#
#     def __init__(self, first_name, last_name, country, date_ot_birth, num_of_passport, visa):
#         super().__init__(first_name, last_name, country, date_ot_birth, num_of_passport)
#         self.visa = visa
#
#     def printInfo(self):
#         super().printInfo()
#         print('Visa:', self.visa)
#
#
# MFC = []
# p = Passport('Iven', 'Ivenov', 'Russia', '14.05.2005', '8221 457896')
# MFC.append(p)
# fp = ForeignPassport('Petr','Ivenov', 'Russia', '25.03.1999', '4785 764546', 'China')
# MFC.append(fp)
# print(MFC)
# for item in MFC:
#     item.printInfo()
#
# str = 'fghfvshd'
# ls = [1, 5, 7, 2, 3, 66, 5]
# for i in str:
#     print(i)
#
# for i in ls:
#     print(i)




# class Equipment:
#
#      def __init__(self, name , make, year):
#          self.name = name
#          self.make = make
#          self.year = year
#
#      def action(self):
#          return 'не определено'
#
#      def __str__(self):
#          return f'{self.name}, {self.make}, {self.year}. Умеет "{self.action()}"'
#
#
#      def __le__(self, other):
#          if not isinstance(other, Equipment):
#              raise TypeError
#          return self.year <= other.year
#
#
# class Printer(Equipment):
#
#     def __init__(self, series, name, make, year):
#         super().__init__(name, make, year)
#         self.series = series
#
#     def action(self):
#         return 'печатает'
#
#     def __str__(self):
#         return f'{self.series} {self.name} {self.make} {self.year}'
#
#
# class SCaner(Equipment):
#
#     def __init__(self, name, make, year):
#         super().__init__(name, make, year)
#
#     def action(self):
#         return 'сканирует в комп'
#
#
# class Xerox(Equipment):
#
#     def __init__(self, name, make, year):
#         super().__init__(name, make, year)
#
# def action(self):
#     return 'копирует и печатает на листочек'
#
# def allItems(sklad):
#     for item in sklad:
#         print(item)
#
#
# def get_items(sklad, ename):
#     for item in sklad:
#         if isinstance(item, ename):
#             print(item)
#
#
# sklad = []
# e = Equipment('Noname', 'x', 2000)
# sklad.append(e)
# s = Printer('hjfdbd', 'G', 'hjfd', 465473)
# sklad.append(s)
# x = Xerox('dhgf', 'hg4eyye', 4000)
# sklad.append(x)
# e = Equipment('Noname', 'x', 2000)
# sklad.append(e)
# s = Printer('hjfdbd', 'G', 'hjfd', 465473)
# sklad.append(s)
# x = Xerox('dhgf', 'hg4eyye', 4000)
# sklad.append(x)
# # allItems(sklad)
# get_items(sklad, Xerox)




# from random import randint
#
# class Soldier:
#     def __init__(self, name='Noname', health=100):
#         self.name = name
#         self.health = health
#
#     def set_name(self, name):
#         self.name = name
#
#     def make_kick(self, enemy):
#         enemy.health -= 20
#         if enemy.health < 0:
#             enemy.health = 0
#         self.health += 10
#         print(self.name, "бьет", enemy.name)
#         print('%s = %d' % (enemy.name, enemy.health))
#
# class Battle:
#     def __init__(self, u1, u2):
#         self.u1 = u1
#         self.u2 = u2
#         self.result = "Сражения не было"
#
#     def battle(self):
#         while self.u1.health > 0 and self.u2.health > 0:
#             n = randint(1, 2)
#             if n == 1:
#                 self.u1.make_kick(self.u2)
#             else:
#                 self.u2.make_kick(self.u1)
#         if self.u1.health > self.u2.health:
#             self.result = self.u1.name + " ПОБЕДИЛ"
#         elif self.u2.health > self.u1.health:
#             self.result = self.u2.name + " ПОБЕДИЛ"
#
#     def who_win(self):
#         print(self.result)
#
#
# first = Soldier('Mr.Kiril',140)
# second = Soldier()
# second.set_name('Mr.Vlad')
# b = Battle(first,second)
# b.battle()
# b.who_win()






# import time
# import random
# class Card():
#     NumsList = ["Джокер", '2', '3', '4', '5', '6', '7', '8', '9', '10',
#                 "Валет", "Дама", "Король", "Туз"]
#     MastList = ["пик", "крестей", "бубей", "червей"]
#
#     def __init__(self, i, j):
#         self.Mastb = self.MastList[i - 1]
#         self.Num = self.NumsList[j - 1]
#
#
# class DeckOfCards():
#     def __init__(self):
#         self.deck = [None] * 56
#         k = 0
#         for i in range(1, 4 + 1):
#             for j in range(1, 14 + 1):
#                 self.deck[k] = Card(i, j)
#                 k += 1
#
# def shuffle(self):
#     random.shuffle(self.deck)
#     def get(self, i):
#         if 0 <= i <= 55:
#             answer = self.deck[i].Num
#             answer += " "
#             answer += self.deck[i].Mastb
#         else:
#             answer = "В колоде только 56 карт"
#         return answer
#
# deck = DeckOfCards()
# deck.shuffle()
# print('Выберите карту из колоды в 56 карт:')
# n=int(input())
# if n<=56 :
#  card = deck.get(n-1)
#  print('Вы взяли карту: ', card, end='.\n')
# else :
#  print("В колоде только 56 карт")







# class Vector3D:
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __add__(self, other):
#         return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
#
#     def __sub__(self, other):
#         return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
#
#     def __mul__(self, other):
#         if isinstance(other, Vector3D):
#             return self.x * other.x + self.y * other.y + self.z * other.z
#         elif isinstance(other, (int, float)):
#             return Vector3D(self.x * other, self.y * other, self.z * other)
#
#     def __matmul__(self, other):
#         return Vector3D(self.y * other.z - self.z * other.y,
#                         self.z * other.x - self.x * other.z,
#                         self.x * other.y - self.y * other.x)
#
#     def display(self):
#         print(f'({self.x}, {self.y}, {self.z})')
#
#     def read(self):
#         self.x = float(input('Введите координату x: '))
#         self.y = float(input('Введите координату y: '))
#         self.z = float(input('Введите координату z: '))
#
# v1 = Vector3D(4, 1, 2)
# v1.display()
#
# v2 = Vector3D()
# v2.read()
#
# v3 = Vector3D(1, 2, 3)
#
# v4 = v1 + v2
# v4.display()
#
# a = v4 * v3
# print(a)
#
# v4 = v1 * 10
# v4.display()
#
# v4 = v1 @ v3
# v4.display()







# import math
#
#
# class Triangle:
#     def __init__(self, side1, side2):
#         self.side1 = side1
#         self.side2 = side2
#
#     def increase_side(self, percent):
#         self.side1 *= (1 + percent / 100)
#         self.side2 *= (1 + percent / 100)
#
#     def decrease_side(self, percent):
#         self.side1 *= (1 - percent / 100)
#         self.side2 *= (1 - percent / 100)
#
#     def calculate_circumcircle_radius(self):
#         hypotenuse = math.sqrt(self.side1 ** 2 + self.side2 ** 2)
#         return hypotenuse / 2
#
#     def calculate_perimeter(self):
#         hypotenuse = math.sqrt(self.side1 ** 2 + self.side2 ** 2)
#         return self.side1 + self.side2 + hypotenuse
#
#     def calculate_angles(self):
#         angle1 = math.degrees(math.atan(self.side2 / self.side1))
#         angle2 = 90 - angle1
#         return angle1, angle2, 90
#
# triangle = Triangle(3, 4)
# triangle.increase_side(10)
# print('Side 1:', triangle.side1)
# print('Side 2:', triangle.side2)
#
# circumcircle_radius = triangle.calculate_circumcircle_radius()
# print('Circumcircle radius:', circumcircle_radius)
#
# perimeter = triangle.calculate_perimeter()
# print('Perimeter:', perimeter)
#
# angles = triangle.calculate_angles()
# print('Angles:', angles)






#
# class Bus:
#     def __init__(self, capacity, max_speed):
#         self.speed = 0
#         self.capacity = capacity
#         self.max_speed = max_speed
#         self.passengers = []
#         self.seats = {}
#         self.hasEmptySeats = True
#
#     def add_passenger(self, passenger):
#         if len(self.passengers) < self.capacity:
#             self.passengers.append(passenger)
#             self.seats[passenger] = len(self.passengers)
#             print(f'{passenger} сел в автобус.')
#         else:
#             print('Нет свободных мест в автобусе.')
#
#     def remove_passenger(self, passenger):
#         if passenger in self.passengers:
#             self.passengers.remove(passenger)
#             seat_number = self.seats.pop(passenger)
#             print(f'{passenger} вышел из автобуса.')
#             for p, seat in self.seats.items():
#                 if seat > seat_number:
#                     self.seats[p] = seat - 1
#         else:
#             print(f'{passenger} не найден в автобусе.')
#
#     def increase_speed(self, value):
#         if self.speed + value <= self.max_speed:
#             self.speed += value
#             print(f'Скорость увеличена на {value} км/ч. Текущая скорость: {self.speed} км/ч.')
#         else:
#             print('Достигнута максимальная скорость.')
#
#     def decrease_speed(self, value):
#         if self.speed - value >= 0:
#             self.speed -= value
#             print(f'Скорость уменьшена на {value} км/ч. Текущая скорость: {self.speed} км/ч.')
#         else:
#             print('Скорость не может быть отрицательной.')
#
#     def __contains__(self, passenger):
#         return passenger in self.passengers
#
#     def __iadd__(self, passenger):
#         self.add_passenger(passenger)
#         return self
#
#     def __isub__(self, passenger):
#         self.remove_passenger(passenger)
#         return self
#
#
#
# bus = Bus(50, 100)
# bus.add_passenger('Maks')
# bus.add_passenger('Ravil')
# bus += 'Ric'
# bus.remove_passenger('Maks')
# bus -= 'Ravil'
# bus.increase_speed(20)
# bus.decrease_speed(10)
# if 'Ric' in bus:
#     print('Ric еще находится в автобусе.')
