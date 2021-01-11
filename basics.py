# import this
import os

# print(os.path.dirname(os.path.abspath(__file__)))
# try:
#     passwd = input("Enter the password ")
#     if passwd == "hello":
#         print("Your password is too common")
#     else:
#         print(passwd)
# except:
#     pass


class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hi am ", self.name, "and am", self.age, "years old")

    def change_age(self, age):
        self.age = age
        print("Am now", self.age)

    def celebrate_birthday(self):
        self.age = self.age + 1
        print("I have a birthday today now now am", self.age)


class Dog(Animal):
    """docstring for Dog class."""

    def __init__(self, name, age, color, rabbies=False):
        super().__init__(name, age)
        self.color = color
        self.rabbies = rabbies

    def has_rabbies(self):
        self.rabbies = True
        return self.rabbies


class Cat(Animal):
    def __init__(self, name, age, color, weight, height):
        super().__init__(name, age)
        self.color = color
        self.weight = weight
        self.height = height

    def speak(self):
        print("A cat meaws")

# sam = Animal('Sam', 21)
# sam.speak()
# sam.change_age(22)
# sam.celebrate_birthday()
# print(sam.age)

# backy = Dog('backy', 20, 'brown')
# backy.change_age(24)
# backy.speak()
# print(backy.has_rabbies())



# catty = Cat("Catty", 34, 'white', 45, 20)
# catty.change_age(60)
# catty.speak()


class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fill_up_tank(self, gas):
        self.gas = gas

    def empty_tank(self):
        self.gas = 0

    def gas_left(self):
        return self.gas


class Car(Vehicle):
    def __init__(self, price, gas, color, speed, wheel):
        super().__init__(price, gas, color)
        self.speed = speed
        self.wheel = wheel

    def beep(self):
        print("Beeeeeep!!!")


class Truck(Vehicle):
    def __init__(self, price, gas, color, weight, luggage):
        super().__init__(price, gas, color)
        self.weight = weight
        self.luggage = luggage

    def add_weight(self, weight):
        return self.weight + weight

# gas = int(input("Enter gas quantity: "))
# v1 = Vehicle('4.6M', gas, 'black sheep')
# print(v1.price, v1.gas, v1.color)
# fill = int(input("Fill the Gas tank: "))
# v1.fill_up_tank(fill)
# print(v1.gas)
# v1.empty_tank()
# print(v1.gas)
#
# print(v1.gas_left())

# gas = int(input("Enter gas quantity: "))
# c1 = Car('3.4M', gas, "Navy blue", '56km/hr', '4 wheel drive')
# c1.empty_tank()
# print(c1.gas_left())
# print(c1.speed)
# print(c1.wheel)


# gas = int(input("Enter gas quantity: "))
# t1 = Truck("20.6M", gas, "White", 3400, "Furniture")
# weight = int(input("Enter weight to add: "))
# t1.add_weight(weight)

# self repr the instance you are taliking about
# __init__ is a constructor
# whenever we instantiate the class the parameters are passed to self


class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.cords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y
        return (self.x, self.y)

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y + p.y

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __lt__(self, p):
        return self.length() < p.length()

    def __le__(self, p):
        return self.length() <= p.length()

    def __gt__(self, p):
        return self.length() > p.length()

    def __ge__(self, p):
        return self.length() >= p.length()

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


p = Point(4,6)
p1 = Point(1,9)
p2 = Point(1,9)
p3 = Point(7,1)
p4 = p1 + p2
p5 = p2 - p3
p6 = p1 * p2
# print(p.cords)
# print(p.move(6,8))
# print(p1 + p2)
# print(p4, p5, p6)
#
# print(p.length(), p1.length())
#
# print(p < p1)
# print(p <= p1)
# print(p > p1)
# print(p >= p1)
#
# print(p1 <= p2)


class Student(object):
    registered_students = [] #class viariables declared before init
    # can be called Directly on class not neccessarily an instance

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        self.registered_students.append(self)

    @classmethod #can be called on class Directly not neccessarily an instance
    def num_students(cls):
        return len(cls.registered_students)

    @staticmethod
    def award(units):
        assert isinstance(units, list)
        return len(units)

# std1 = input("1. What is your name ")
# dob1 = input("1. What is your date of birth ")
# std2 = input("2. What is your name ")
# dob2 = input("2. What is your date of birth ")
# stud1 = Student("Sam", 1998)
# print(Student.registered_students)
# stud2 = Student("Tina", 1998)
# print(stud1.registered_students)
# print(Student.num_students())
# print(Student.award([1,3,2,4,55,5,66,6]))



# INTERMEDIATE PYTHON COURSE
# map function ..... takes in two args ---> function, and list and return new list...

lis = ['a', 'b', 'c', 'd', 'e', 'f']

# 1
def func(x):
    return x*2


new_lis = []
for x in lis:
    new_lis.append(func(x))

# print(new_lis)

# 2
# print(list(map(func, lis)))


# 3 List comprehension
new_lis.append(func(x) for x in lis)
# print(new_lis)
# print([func(x) for x in lis if x == 'a' or x == 'c'])


# Filter function
def add10(x):
    return x + 10


def isEven(x):
    if x % 2 == 0:
        return x


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(filter(isEven, a))

# print(list(map(add10, b)))


# Lambda function .... anonymous functions

def func2(x):
    return x ** 2

# print(func2(56))

func3 = lambda x: x ** 2
# print(func3(10))

# print(list(map(lambda x: x **3, a)))


# Containers
from collections import Counter
from inspect import currentframe, getframeinfo

frameinfo = getframeinfo(currentframe())

def get_linenumber():
    cf = currentframe()
    return cf.f_back.f_lineno

c = Counter('hellosam')
stri = 'hellosam'
# print(list(stri))
def getstr(x):
    lis_str = []
    for i in x:
        lis_str.append(i)
    return lis_str

# print(frameinfo.filename, get_linenumber(), getstr(stri))
#
# print(frameinfo.filename, get_linenumber(), c)
# c = Counter([1, 2, 3, 4, 5])
# print(frameinfo.filename, get_linenumber(), c)
# c = Counter({'a': 1, 'b': 2, 'c': 3})
# print(frameinfo.filename, get_linenumber(), c)
# # c = Counter(cats=4, dogs=7)
# print(frameinfo.filename, get_linenumber(), c['cats'])
# print(get_linenumber(), list(c.elements()))
# print(get_linenumber(), list(c.most_common(2)))

d = Counter(a=4, b=5, c=9)
e = ['a', 'a', 'b', 'b', 'b', 'c']
f = Counter(['a', 'a', 'b', 'b', 'b', 'c'])

d.subtract(e)
d.update(e)

# print(frameinfo.filename, get_linenumber(), d)
#
# print(d + f)


# NamedTuple
from collections import namedtuple

Point = namedtuple('Point', 'x y z') #str iterable object
newp = Point(4, 5, 6)
# print(newp._asdict())
# print(newp._fields)
# newp = newp._replace(z=20)
# print(newp)

Point = namedtuple('Point', ['x', 'y', 'z']) #list iterable object
newp = Point(1, 2, 3)
# print(newp)

Point = namedtuple('Point', {'x':0, 'y':0, 'z': 0}) #dict iterable object
newp = Point(7, 8, 9)
# print(newp)

from collections import deque

d = deque("hello")
# print(d)
# d.append('5')
# d.appendleft('q')
# print(d)
# d.pop()
# print(d)
# d.popleft()
# print(d)
# d.clear()
# print(d)
# d.extend('world')
# print(d)
# d.extendleft('my')
# print(d)
# print(d.rotate(-1))

d = deque('hello', maxlen=5)
print(d)
d.append(2)
print(d)


class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        return type(class_name, bases, attrs)


class Bird(metaclass=Meta):
    x = 7
    y = 79

    def hello(self):
        print("Hello world!")
