import os
import datetime as dt
import pandas as pd
from datetime import datetime, timedelta

class Salary:
    def __init__(self, base_salary):
        self.base_salary = base_salary + 14_000 + 5_328.76

    def increment(self, percentage):
        incre = self.base_salary * (percentage / 100)
        self.base_salary += incre

sal = Salary(93_703.00)
sal.increment(6.66)
# print(sal.base_salary)

text = f"""NIVEL-16 270,609.81 284,140.30 298,347.32 313,264.68 328,927.92
NIVEL-15 212,029.88 222,631.38 233,762.95 245,451.10 257,723.65
NIVEL-14 166,130.96 174,437.51 183,159.39 192,317.36 201,933.24
NIVEL-13 136,676.36 143,510.18 150,685.69 158,219.97 -
NIVEL-12 112,443.97 118,066.17 123,969.48 130,167.95 -
NIVEL-11 89,240.93 93,703.00 98,388.15 103,307.55 -
NIVEL-10 74,367.45 78,085.81 81,990.10 - -
NIVEL-09 61,972.86 65,071.53 68,325.10 - -
NIVEL-08 51,644.05 54,226.25 56,937.57 - -
NIVEL-07 43,036.72 45,188.54 47,447.98 - -
NIVEL-06 35,863.94 37,657.12 - - -
NIVEL-05 29,886.62 31,380.93 - - -
NIVEL-04 24,905.52 26,150.79 - - -
NIVEL-03 20,754.59 21,792.32 - - -
NIVEL-02 17,295.48 18,160.26 - - -
NIVEL-01 14,412.90 15,133.54 - - -"""
data = []
for line in text.split('\n'):
    row = line.split(' ')
    data.append(row)

df = pd.DataFrame(data,
	columns=['Nivel', 'Base', 'ESCALAO-A',
			 'ESCALAO-B', 'ESCALAO-C',
			 'ESCALAO-D'])
df['Nivel'] = df['Nivel'].apply(
	lambda x: x.split('-')[-1])

def format_salary(val):
	try:
		return float(str(val).replace(',', ''))
	except Exception as e:
		return 0.0
df['Base'] = df['Base'].apply(format_salary)
df['Grading'] = 'All'
for col in ['A', 'B', 'C', 'D']:
	df[f'ESCALAO-{col}'] = df[f'ESCALAO-{col}'].apply(format_salary)

def set_grading(nivels, text):
	for nivel in nivels:
		df.loc[nivel, 'Grading'] = text

df.set_index('Nivel', inplace=True)

set_grading(['16', '15', '14'], 'Director Formalmente nomeado / Gestor Sénior')
set_grading(['12', '13'], 'Chefe de Departamento formalmente nomeado / Gestor Intermédio')
set_grading(['10', '11'], 'Chefe de Secção formalmente nomeado / Gestor Júnior')
set_grading(['08', '09'], 'Técnico Superior')
set_grading(['04', '05', '06', '07'], 'Técnico')
set_grading(['01', '02', '03'], 'Auxiliar Administrativo')

df.reset_index(inplace=True)
#print(df.dtypes)
# print(df[[f'ESCALAO-{char}' for char in list('ABCD')]].pct_change(axis=1))
# print(df)
df.to_excel('Table-Salarial.xlsx', index=False)
# os.system('start Table-Salarial.xlsx')

# print(dir(df.groupby('Grading')))
df.set_index('Grading', inplace=True)
# print(df)
df.to_excel('Table-Salarial.xlsx', index=True)
# os.system('start Table-Salarial.xlsx')

# print(270_609.81 - 284_140.30)

# 270_609.81 ------ 100
# 284_140.30 ------  x
# x = (284_140.30 * 100) / 270_609.81 
# print(x)
# sals = [
# 	270_609.81, 284_140.30,
# 	298_347.32, 313_264.68,
# 	328_927.92
# ]
# first = sals.pop(0)
# for sal in sals:
# 	x = (sal * 100) / first 
# 	print(x - 100)
# 	first = sal

def starting_time(time_span=8, n_times=6):
	time = datetime(year=2023, month=5, day=16,
				hour=13, minute=9, second=30)
	for _ in range(n_times):
		print(f'{time_span} hours = {time}')
		time_span_ = timedelta(hours=time_span)
		time += time_span_
	print('')

# starting_time()
# starting_time(time_span=12)


for i in range(0, 15000):
	# print(f'\t{i}: ', chr(i))
	print(chr(i), end=', ')


# print(type(dt.date(2023, 4, 19)))
# print(30 * 10)

# amount = 18000
# interest_rate = 0.25
# n_times = 9
# future_value = amount * (
# 	((1 + interest_rate) ** n_times) - 1
# ) / interest_rate
# print(future_value)

# print(2250 + 6250 + 4500 * 5 +
# 	18000
# )
# print(6300 * 8)
# print(38400 - 31775)

# 845054617 - Amituna Litos Carlos

val = 18000
print(val * 0.35 - val * 0.30)