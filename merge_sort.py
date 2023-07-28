# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 14:34:05 2022

@author: a248433
"""

import string
import random
import pandas as pd
from faker import Faker
import mysql.connector as mysql

def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

def get_n():
    return str(random.randint(0, 9))

def generate_IC():
    nums = [get_n() for _ in range(10)]
    return '02' + ''.join(nums) + random.choice(string.ascii_uppercase)

def generate_OTP():
    letters = list(string.ascii_uppercase + string.digits)
    for _ in range(100):
        random.shuffle(letters)

    OTP = ''
    for _ in range(6):
        OTP += random.choice(letters[random.randint(0, len(letters)-1)])
    print(OTP)

config = {
    'user': 'root',
    'passwd': 'Young1995@',
    'host': 'localhost',
    'db': 'node_practice'
}

def dictfetchall(cursor):
    cols = [col[0] for col in cursor.description]
    return [
        dict(zip(cols, row)) for row in cursor.fetchall()
    ]

# conn = mysql.connect(**config)
# cursor = conn.cursor()
# cursor.execute('SHOW TABLES')
# results = dictfetchall(cursor)
# for table in results:
#     table = table['Tables_in_node_practice']
#     if table.startswith('app_') or table.startswith('auth_'):
#         query = f'DROP TABLE IF EXISTS {table}'
#         cursor.execute(query)
#         conn.commit()
        # print(table)

# Driver program
if __name__ == '__main__':
    # generate_OTP()
    faker = Faker()
    # df = pd.DataFrame({
    #     'first_name': [faker.first_name() for _ in range(25)],
    #     'last_name': [faker.last_name() for _ in range(25)],
    #     'marks': [random.randint(5, 20) for _ in range(25)]
    # })
    # df.to_excel('student_marks.xlsx', index=False)
    # print(df)


    # print(generate_IC())
    # array = [6, 5, 12, 10, 9, 1]

    # mergeSort(array)

    # print("Sorted array is: ")
    # printList(array)