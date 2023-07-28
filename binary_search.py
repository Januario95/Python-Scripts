# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 14:31:29 2022

@author: a248433
"""

import time
from datetime import datetime
import json
import requests
from random import randint


def get_random(num=7):
    return [randint(1, 50) for _ in range(num)]

def sort_values(arr):
    for num in range(len(arr)-1, -1, -1):
        for val in range(num):
            if arr[num] > arr[val]:
                temp = arr[num]
                arr[num] = arr[val]
                arr[val] = temp
    return sorted(arr)

def binarySearch(arr, x, low, high):
    if low > high:
        return False 
    else:
        mid = int((low + high) / 2)
        if x == arr[mid]:
            return True
        elif x > arr[mid]:
            return binarySearch(arr, x, mid + 1, high)
        else:
            return binarySearch(arr, x, low, mid - 1)
        

# arr = get_random()
# print(f'arr = {arr}')
# sorted_arr = sort_values(arr)
# print(f'sorted_arr = {sorted_arr}')
# value = randint(1, 50)
# print(f'value = {value}')
# print(binarySearch(sorted_arr, value, 0, len(sorted_arr)-1))



url = 'http://localhost:8000/students/'
# res = requests.get(url)
# print(res.json())

data = {
    'name': 'Reinata Cipriano',
    'roll': 5,
    'city': 'Chiure, Cabo Delgao'
}
# res = requests.post(url, data=data)
# print(res.status_code)


def calculate(num_of_studs, cost_per_month, num_of_schools):
    return num_of_studs * cost_per_month * num_of_schools

# num_of_studs = 500
# cost_per_month = 85
# num_of_schools = 1
# print(calculate(num_of_studs, cost_per_month, num_of_schools))

# print(cost_per_month * 12)
# print(1.35 * 12)


# import string
 
# test_str = 'Cr\u00e9dito ao Consumo'
 
# test_str = test_str.translate(str.maketrans('', '', string.punctuation))
# print(test_str)




# import pathlib

# grossdir = pathlib.Path(
#     __file__).parent.resolve()
# print(grossdir)


class LimitQuery:
    def __init__(self): # , func):
        # self.func = func
        self.count = 0
        
    def __call__(self, *args, **kwargs):
        limit = args[0]
        if self.count < limit:
            # self.func()
            self.count += 1
        else:
            print('No queries left')

# l = LimitQuery()
# print(dir(l))


class LimitQuery:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        limit = args[0]
        if self.count < limit:
            self.func()
            self.count += 1
        else:
            print('No queries left')


@LimitQuery
def soma():
    return 5

# soma(3)
# soma(3)
# soma(3)
# soma(3)




class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class Student:
    STUDENTS = []
    INDEX = 0
    def __init__(self, first_name, last_name, age, course, year):
        # super().__init__(first_name, last_name, age)
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__course = course
        self.__year = year
        self.__full_name = self.__first_name + ' ' + self.__last_name
        self.__username = self.__full_name.replace(' ', '').lower()
        Student.INDEX += 1
        self.__ID = Student.INDEX
        Student.STUDENTS.append(self)

    def __check_admin(self):
        if self.__username != 'januariocipriano':
            raise TypeError('Not allowed to updated student data.')

    @property
    def first_name(self):
        return first_name

    @first_name.setter
    def first_name(self, val):
        self.__check_admin()
        self.__first_name = val

    @property
    def last_name(self):
        return last_name

    @last_name.setter
    def last_name(self, val):
        self.__check_admin()
        self.__last_name = val

    @property
    def age(self):
        return age

    @age.setter
    def age(self, val):
        self.__check_admin()
        self.__age = val

    @property
    def course(self):
        return course

    @course.setter
    def course(self, val):
        self.__check_admin()
        self.__course = val

    @property
    def year(self):
        return year

    @year.setter
    def year(self, val):
        self.__check_admin()
        self.__year = val

    def __repr__(self):
        return f'Student(id={self.__ID}, first_name={self.__first_name}, last_name={self.__last_name}, age={self.__age}, course{self.__course}, year={self.__year})'

    def __str__(self):
        return json.dumps({
            'id': self.__ID, 'full_name': self.__first_name + ' ' + self.__last_name, 'age': self.__age,
            'course': self.__course, 'year': self.__year
        }, default=str, indent=4)

# std = Student('Januario', 'Cipriano', 28, 'Computer Science', 'Fourth')
# std2 = Student('Angelina', 'Cipriano', 17, 'Finance', 'First')
# std3 = Student('Reinata', 'Cipriano', 22, 'Medical Sciences', 'Second')
# std4 = Student('Maico', 'Cipriano', 31, 'Business Administration', 'Third')

# std2.year = 18
# print(std)
# del std2
# print(Student.STUDENTS[0])
# print(globals())


class Employee(object):
    def __init__(self, data):
        super().__setattr__('data', dict())
        self.data = data
    def __getattr__(self, name):
        if name in self.data:
            return self.data[name]
        return f'Attribute {name!r} not available'

    def __setattr__(self, key, value):
        if key in self.data:
            self.data[key] = value
        else:
            super().__setattr__(key, value)

emp = Employee({
    'age': 23, 'name': 'John'
})
# print(emp.email)
# print(isinstance(emp, Employee))
# print(issubclass(Employee, object))


# now = datetime.now()
# print(now.strftime('%Y-%m-%d %H:%M:%S'))

previous_gross = 45000
increase = previous_gross * 0.066
# print(increase)
gross = previous_gross + increase
# print(gross)
net = gross - (gross * 0.15)
# print(net)
calculate = lambda val: val * 0.066
incs = 0
incs2 = 0
for _ in range(4):
    incs2 += increase
    incs += calculate(previous_gross)

final = incs + net
# print(final)

debt = dict(costa=6300+5000, ernestino=4500+5000, house=3500)
# print(sum(debt.values()))
to_pay = sum(debt.values())
# print(final - to_pay)

june = dict(cost=11000 * 0.35 + 5000, ernestino=11000 * 0.25 + 5000, house=3000)
# print(net - sum(june.values()))

june = dict(cost=6000 * 0.35 + 5000, ernestino=6000 * 0.25 + 5000, house=3000)
# print(net - sum(june.values()))

MONTHS = (
    ('January', 'January'), 
    ('February', 'February'), 
    ('March', 'March'), 
    ('April', 'April'), 
    ('May', 'May'), 
    ('June', 'June'), 
    ('July', 'July'), 
    ('August', 'August'), 
    ('September', 'September'), 
    ('October', 'October'), 
    ('November', 'November'), 
    ('December', 'December')
)

now = datetime.now()
print(MONTHS[now.month-1][0])