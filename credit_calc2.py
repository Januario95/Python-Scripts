import os
import json
import string
import random
import pandas as pd
from datetime import datetime

MONTHS = ['January', 'February', 'March', 'April', 'May',
          'June', 'July', 'August', 'September', 'October',
          'November', 'December']

class Credit:
	def __init__(self, initial_amount, interest_rate):
		self.initial_amount = initial_amount
		self.interest_rate = interest_rate
		self.amount_injected = 10000

	def calculate_final(self, start_month, end_month, year): # , amount_injected=1000):
		months = end_month - start_month
		data = []
		for month in range(start_month, end_month):
			yield_ = self.calculate_return()[0]
			row = {
				'Month': f'{MONTHS[month]} {year}',
				'Amount': self.initial_amount,
				'Final': self.calculate_return()[0],
				'Yield': self.calculate_return()[1], 
				'Amount Injected': self.amount_injected
			}
			data.append(row)
			self.initial_amount = yield_ + self.amount_injected
			# self.amount_injected += 10000
		# print(json.dumps(data, indent=4))
		# print(pd.DataFrame(data))
		return data

	def calculate_return(self):
		amount_per_1k = (1000 * self.interest_rate) / 100
		yield_ = (self.initial_amount / 1000) * amount_per_1k
		return round(self.initial_amount + yield_, 2), round(yield_, 2)


initial_amount = 30000
interest_rate = 35
credit = Credit(initial_amount, interest_rate)
data1 = credit.calculate_final(9, 12, 2023)
data2 = credit.calculate_final(0, 12, 2024)
# # data3 = credit.calculate_final(0, 12, 2025)
data = data1 + data2 # + data3
df = pd.DataFrame(data)
# print(df)
df.to_excel('Credit.xlsx', index=False)
os.system(f'start Credit.xlsx')

# initial_amount = 30000
# interest_rate = 35
# credit = Credit(initial_amount, interest_rate)
# print(credit.calculate_return())

# first = 13 * 250
# second = 5 * 600
# print(first + second)

# print(((f'{x}ª. classe', f'{x}ª. Classe') for x in range(8, 13)))
# print([(f'{x}ª. classe', f'{x}ª. Classe') for x in range(8, 13)])


digits = string.digits
preffix = ['86', '87', '84', '85', '82']

def get_suffix():
	return ''.join([random.choice(digits) for _ in range(7)])

def generate_phone_number():
	# return '+258' + random.choice(preffix) + get_suffix()
	return '86' + get_suffix()

# numbers = [get_suffix() for _ in range(9500000)]
# print('9402316' in numbers)



	
class Student:
	def __init__(self, first_name, last_name, date_of_birth):
		self.first_name = first_name
		self.last_name = last_name
		self.date_of_birth = date_of_birth

	@property
	def age(self):
		today = datetime.today()
		age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
		return age

	def __repr__(self):
		return f'Student(first_name={self.first_name}, last_name={self.last_name}, date_of_birth={self.date_of_birth})'

s = Student('Januario', 'Cipriano', datetime(1995, 3, 14))
# print(repr(s))
# print(s.age)









