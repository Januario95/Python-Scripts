import json
import pandas as pd

class Credit:
	def __init__(self, initial_amount, interest_rate):
		self.initial_amount = initial_amount
		self.interest_rate = interest_rate

	def calculate_final(self, start_month, end_month):
		months = end_month - start_month
		data = []
		for month in range(months):
			yield_ = self.calculate_return()[0]
			# print(f'{MONTHS[month]}: Rate={self.interest_rate}%,  amount={self.initial_amount},  yield={self.calculate_return()[1]}, final={self.calculate_return()[0]}')
			row = {
				'month': MONTHS[month],
				'amount': self.initial_amount,
				'yield': self.calculate_return()[1], 
				'final': self.calculate_return()[0]
			}
			data.append(row)
			# print(json.dumps(row, indent=4))
			self.initial_amount = yield_
		# print(json.dumps(data, indent=4))
		print(pd.DataFrame(data))

	def calculate_return(self):
		amount_per_1k = (1000 * self.interest_rate) / 100
		yield_ = (self.initial_amount / 1000) * amount_per_1k
		return round(self.initial_amount + yield_, 2), round(yield_, 2)

MONTHS = ['January', 'February', 'March', 'April', 'May',
          'June', 'July', 'August', 'September', 'October',
          'November', 'December']


initial_amount = 30000
interest_rate = 25
credit = Credit(initial_amount, interest_rate)
credit.calculate_final(0, 12)
# index = 0
# while index < 12:
# 	yield_ = credit.calculate_return()[0]
# 	print(f'{MONTHS[index]}: Rate={credit.interest_rate}%,  amount={credit.initial_amount},  yield={credit.calculate_return()[1]}, final={credit.calculate_return()[0]}')
# 	credit.initial_amount = yield_
# 	index += 1

print(credit.initial_amount)










	
