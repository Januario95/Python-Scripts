# from cryptography.fernet import Fernet

# key = Fernet.generate_key()

# f = Fernet(key)

# token = f.encrypt(b'example 123')
# print(token)

import string
import random

digits = string.digits
preffix = ['86', '87', '84', '85', '82']

def get_suffix():
	return ''.join([random.choice(digits) for _ in range(7)])

def generate_phone_number():
	return random.choice(preffix) + get_suffix()

print(generate_phone_number())
















































