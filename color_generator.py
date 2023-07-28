import random

def generate_num():
	return random.randint(0, 255)

def generate_codes():
	return (
		generate_num(),
		generate_num(),
		generate_num()
	)

def check_value(val):
	if val >= 0 and val <= 255:
		return val
	raise TypeError('Color value must be between 0 and 255.')

class MyColor:
	def __init__(self):
		self.red = 50 # generate_num()
		self.green = 13 # generate_num()
		self.blue = 167 # generate_num()

	def __getattr__(self, attr):
		if attr == 'rgbcolor':
			return (self.red, self.green, self.blue)
		elif attr == 'hexcolor':
			return "#{0:02x}{1:02x}{2:02x}".format(
				self.red, self.green,
				self.blue
			)

	def __setattr__(self, attr, val):
		if attr == 'rgbcolor':
			self.red = check_value(val[0])
			self.green = check_value(val[1])
			self.blue = check_value(val[2])
		else:
			super().__setattr__(attr, val)

c1 = MyColor()
# print(c1.hexcolor)
# print(c1.rgbcolor)

c1.rgbcolor = generate_codes()
# print(c1.hexcolor)
# print(c1.rgbcolor)



EXTENSIONS = {
	'csv': lambda file: pd.read_csv(file),
	'xlsx': lambda file: pd.read_excel(file),
	''
}

















