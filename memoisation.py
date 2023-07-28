# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 14:34:39 2022

@author: a248433
"""

import os
import math
from datetime import datetime

def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


def memoize2(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
fib = memoize(fib)
# print(fib(40))


def memoize3(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
@memoize3
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
# print(fib(40))


class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]
@Memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
# print(fib(40))


def factors_set():
        for i in [-1, 0, 1]:
            for j in [-1,0,1]:
                for k in [-1,0,1]:
                    for l in [-1,0,1]:
                        yield (i, j, k, l)  
def memoize(f):
    results = {}
    def helper(n):
        if n not in results:
            results[n] = f(n)
        return results[n]
    return helper
@memoize
def linear_combination(n):
    """ returns the tuple (i,j,k,l) satisfying
        n = i*1 + j*3 + k*9 + l*27      """
    weighs = (1,3,9,27)
    for factors in factors_set():
       sum = 0
       for i in range(len(factors)):
          sum += factors[i] * weighs[i]
       if sum == n:
          return factors 
      
        
def weigh(pounds):
        weights = (1, 3, 9, 27)
        scalars = linear_combination(pounds)
        left = ""
        right = ""
        for i in range(len(scalars)):
            if scalars[i] == -1:
                left += str(weights[i]) + " "
            elif scalars[i] == 1:
                right += str(weights[i]) + " "
        return (left,right)
# for i in [2, 3, 4, 7, 8, 9, 20, 40]:
#             pans = weigh(i)
#             print("Left  pan: " + str(i) + " plus " + pans[0])
#             print("Right pan: " + pans[1] + "\n")   
            
            






def format_datetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formatted_date = utc_timestamp.strftime('%d %b %Y %H:%M:%S')
    return formatted_date


def convert_size(size_bytes):
    if size_bytes == 0:
        return 'OB'
    size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return '%s %s' % (s, size_name[i])


def display_entries_in_directory(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                print('File Name: ', entry.name)
                info = entry.stat()
                # print(info.st_uid)
                # print(info.st_file_attributes)
                # print(info.st_gid)
                print("Creation Time: ", format_datetime(info.st_ctime))
                print("Last Access Time:", format_datetime(info.st_atime))
                print('Size:', convert_size(info.st_size))
                print()

file = 'New rotation 20220914.xlsx'
display_entries_in_directory("./")




























