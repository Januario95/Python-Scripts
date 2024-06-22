# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:39:57 2022

@author: Januario Cipriano
"""

import json
import string
import random

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def extract_vals(vals, methods, is_in=True):
    if is_in:
        return [val for val in vals if val in methods]
    return [val for val in vals if val not in methods]

class ManualCalculator:
    def __init__(self):
        self.methods = {
            '+': add, # lambda x, y: x + y,
            '-': subtract # lambda x, y: x - y
        }
        
    def calculate(self, expression):
        if len(expression.split(' ')) > 3:
            expression = expression.split(' ')
            vals = extract_vals(expression, self.methods, False) # [val for val in expression if val not in self.methods]
            symbols = extract_vals(expression, self.methods) # [val for val in expression if val in self.methods]
            first = float(vals[0])
            index = 0
            if '*' in symbols or '/' in symbols:
                print('Complicated calculations not allowed! \n"*" or "/" cannot be included in complicated calculations')
            else:
                for val in vals[1:]:
                    func = self.methods[symbols[index]]
                    result = func(first, float(val))
                    first = result
                    index += 1
                return first
        else:
            x, op, y = expression.split(' ')
            try:
                func = self.methods[op]
                result = func(float(x), float(y))
                return (f'{x} {op} {y} = {result}')
            except KeyError as e:
                print(e)
            
    def add_method(self, symbol, func):
        self.methods[symbol] = func
            
        


man = ManualCalculator()
man.add_method('*', multiply) # lambda x, y: x * y)
man.add_method('/', divide) #  lambda x, y: x / y)
# print(man.calculate('-3 - 5 + 8 + 4 - 56 + 23 - 5'))
# print(man.calculate('-8 - 15 + 4 - 2 - 16 + 3 - 25'))
#man.calculate('-3 * 5')
# print(man.calculate('-15 * 4'))



def all_digits(num):
    for x in num:
        try:
            x = int(x)
        except:
            return False
    return True


# print(all_digits('248433'))



def generate_digits():
    letter = random.choice(list('abc'))
    digits = ''.join([str(random.randint(1, 9)) for _ in range(6)])
    return letter + digits
    

# print(generate_digits())

class GenerateVoterID:
    VOTER_IDS = []
    VOTER_COUNTER = 1
    def __init__(self, voter_id='VOTER'):
        self.voter_id = str(voter_id) +\
         f'{GenerateVoterID.VOTER_COUNTER}'
        GenerateVoterID.VOTER_IDS.append(self.voter_id)
        GenerateVoterID.VOTER_COUNTER += 1

    def __str__(self):
        return json.dumps({
            'voter_id': self.voter_id
        })

voter1 = GenerateVoterID()
print(voter1)
voter1 = GenerateVoterID()
# print(voter1)

# for _ in range(100):
#     voter = GenerateVoterID()
#     print(voter)

print(GenerateVoterID.VOTER_IDS)




















