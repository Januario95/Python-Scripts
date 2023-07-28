import os
import pandas as pd

sal = 40200

def calculate(initial, percentage):
	index = 1
	to_pays = []
	# print('Month \tInitial \tInterest \tTo Pay \t\tSalary-Balance')
	while initial > 0:
		interest = initial * percentage / 100
		to_pay = interest + 5000
		# print(f'\t{index} \t{initial} \t\t{interest} \t\t{to_pay} \t\t{sal - to_pay}')
		initial = initial - 5000
		initial - initial * (1 - percentage / 100)
		index += 1
		to_pays.append(to_pay)
	return to_pays

initial = 18000
percentage = 35
to_pays_1 = calculate(initial, percentage)
to_pays_2 = calculate(initial, 24)
index = 1
rent = 3000
pay_debt = 0
balance = 0
line_width = 57
values = []
with open('debt-restructuting.txt', mode='w') as f:
	# f.write(f"{'-' * line_width} \n")
	# f.write('Month |\t Debt     |  Rent  | Salary-Balance |  Balance  |\n')
	# f.write(f"{'-' * line_width} \n")
	for val1, val2 in zip(to_pays_1, to_pays_2):
		to_pay = val1 + val2
		pay_debt += to_pay
		bal = sal - (to_pay + rent)
		balance += bal
		f.write(f"  {index}   |  {to_pay}  |  {rent}  |    {bal}     |  {balance}  |\n")
		# print('-' * 48)
		index += 1
		row = {
			'month': index,
			'debt': to_pay,
			'salary_balance': bal,
			'balance': balance
		}
		values.append(row)
	# f.write(f"{'-' * line_width} \n")

df = pd.DataFrame(values)
df.to_excel('debt-restructuting.xlsx', index=False)
avg = df.sum(axis=0)
# avg[0] = 'sum'
# print(avg)
# print(df.append(avg, ignore_index=True))
os.system('start debt-restructuting.xlsx')

# print(pay_debt)
# print(balance)

# to_pay_monthly=5000
# debt = dict(costa=6300+to_pay_monthly, ernestino=4500+to_pay_monthly, house=3000)
# for index in range(1, 5):
# 	to_pay = sum(debt.values())
# 	print(sal - to_pay)
# 	debt['costa'] = 18000 - (to_pay_monthly * index)
# 	debt['ernestino'] = 1800