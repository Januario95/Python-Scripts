# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 14:13:16 2022

@author: Januario Cipriano
"""

import json
import random
import string


def all_digits(num):
    for x in num:
        try:
            x = int(x)
        except:
            return False
    return True
        

def format_username(username):
    letters = string.ascii_letters
    if (len(username) == 7 and username[0] in list('abc') and 
        all_digits(username[1:])):
        return username
    raise TypeError('Username must start with a letter and remaining characters must be digits')


def generate_digits():
    letter = random.choice(list('abc'))
    digits = ''.join([str(random.randint(1, 9)) for _ in range(6)])
    return letter + digits



# usernames = [generate_digits() for _ in range(1000000)]
# for user in sorted(usernames, key=lambda val: val[1:]):
#     if user == 'a248433':
#         print(user)


class CustomError(Exception):
    def __init__(self, message):
        raise Exception(message)


class Debt:
    def __init__(self):
        self.__debt = {}

    def add(self, owner, value):
        self.__debt[owner] = value

    def pay(self, owner):
        password = input('Enter password to accept payment:  ')
        if password != 'Jaci1995':
            raise CustomError('Unauthorized access')
        if owner in self.__debt:
            del self.__debt[owner]
        print(f'Debt for {owner} was successfully paid!')

    def get_total(self):
        return sum(self.__debt.values())

    def get_owners(self):
        return list(self.__debt.keys())

    def __str__(self):
        return 'Debt class'

    def get_debt(self, password=None):
        new_dict = {}
        for key, value in self.__debt.items():
            if password == 'Jaci1995':
                new_dict[key] = value
            else:
                new_dict[key] = '*' * random.randint(3, 6)
        return f'{new_dict}'

debt = Debt()
debt.add('cumbana', 2600)
debt.add('costa', 4500)
debt.add('general', 780)
debt.add('rossana', 1130)
debt.add('victor', 5600)
debt.add('ernestino', 1800)
debt.add('house', 3000)
# print(debt.get_debt('Jaci1995'))
# debt.pay('costa')
# print(debt.get_debt())
# print(debt)
sal = 38400
print(sal - debt.get_total())
# print(debt.get_owners())














