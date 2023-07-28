import string
import random 


chars = string.ascii_letters + \
		string.digits + \
		"$%&@\\<=>?{|}~()*+"

letters = [char for char in chars]

def shuffle():
	global letters
	random.shuffle(letters)

def get_password(n=100, maximum=12):
	for index in range(n):
		# print(f'iteration: {index}', end=': ')
		shuffle()
		# print(''.join(letters))

	print(''.join(letters))
	min_val = random.randint(0, len(letters)-1)
	password = ''.join(letters)[min_val:min_val+maximum]
	first = password[0]
	if password[0].isdigit():
		return random.choice(string.ascii_letters) + password[1:]
	else:
		return password
	

print(get_password(maximum=12))