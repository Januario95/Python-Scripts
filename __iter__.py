import random
from urllib.error import (
	HTTPError, URLError
)
from urllib.request import (
	urlopen, Request
)
import os
import json
import string
import requests

class Enumerator:
	def __init__(self):
		self.values = []

	def append(self, val):
		if not isinstance(val, (int, float)):
			raise TypeError('can only add int or float')
		self.values.append(val)

	def __iter__(self):
		for val in self.values:
			yield val

# enum = Enumerator()
# enum.append(4)
# enum.append(3)
# enum.append(8)
# for val in enum:
# 	print(val)

# request = Request(url,
# 	headers=headers or {})
# try:
# 	with urlopen(request, timeout=10) as response:
# 		print(response.status)
# 		return response.read(), response
# except HTTPError as error:
# 	print(error.status, error.reason)
# except URLError as error:
# 	print(error.reason)
# except TimeoutError:
# 	print('Request timed out')


class URLFetcher:
	def __init__(self, url):
		# try:
		# 	request = Request(url)
		# 	with urlopen(request, timeout=10) as response:
		# 		print(response.status)
		# 		return response.read(), response
		# except (HTTPError, URLError) as error:
		# 	raise (error.status, error.reason)

		self.response = requests.get(url)

	@property
	def headers(self):
		return self.response.headers

	@property
	def status_code(self):
		return self.response.status_code

	def json(self, indent=False):
		data = self.response.json()
		if indent:
			return json.dumps(data, indent=4)
		return data

	def __iter__(self):
		for val in self.json():
			yield val


url = 'http://localhost:8000/api/products'
# fetcher = URLFetcher(url)
# print(fetcher.headers)
# print(fetcher.status_code)
# print(fetcher.json(indent=True))
# for val in fetcher:
# 	print(val)

# print(dir(fetcher))
# print(fetcher.__sizeof__())
# print(fetcher.__reduce__())



# def bottom_up_walk(path):
#     for dirpath, dirnames, files in os.walk(path, topdown=False):
#         print("Diretory:", dirpath)
#         # print("Includes these directories:")
#         # for dirname in dirnames:
#         #     print(dirname)
#         print("Includes these files:")
#         for filename in files:
#             if 'Poter' in filename:
#             	print(filename)
#             	break
	    

# def top_down_walk(path):
#     for dirpath, dirnames, files in os.walk(path):
#         print("Diretory:", dirpath)
#         print("Includes these directories:")
#         for dirname in dirnames:
#             print(dirname)
#         print("Includes these files:")
#         for filename in files:
#             if 'Five Forces' in filename:
#             	print(filename)
#             	break
#         print()
        


# if __name__=='__main__':
#     # top_down_walk()
#     top_down_walk('C:/Users/a248433/Documents/Learning')


class UniqueWord:
	def __init__(self, text):
		self.text = text
		self.num_of_characters = self.character_count()
		self.words_count = self.word_count()

	def word_count(self):
		words = dict()
		for word in self.text.split(' '):
			if word in words:
				words[word] += 1
			else:
				words[word] = 1
		return words

	def unique_characters(self):
		words = []
		text = self.text.lower().replace(' ', '')
		for char in text:
			if char not in words:
				words.append(char)
		return sorted(words)
	
	def character_count(self):
		words = dict()
		for char in self.text:
			if char in words:
				words[char] += 1
			else:
				words[char] = 1
		return words
	
	def used_charaters(self):
		words = self.unique_characters()
		letters = string.ascii_lowercase
		words_ = []
		used_character = 0
		for letter in letters:
			if letter not in words:
				words_.append('[x]')
			else:
				words_.append(letter)
				used_character += 1

		return '-'.join(words_) + f'.  Charaters used: {used_character}'
	
# text = 'Customer retention rate is the rate at which a business keeps its customers within a given period of time. Calculating retention rate helps companies understand the relationship between what they do (like their marketing strategies and other internal business processes) and the outcomes they achieve (how much money they’re making).'
# unique = UniqueWord(text)
# print(unique.used_charaters())
# # print(unique.num_of_characters)
# words_count = unique.words_count
# # print(type(words_count))
# for key, value in words_count.items():
# 	print('\t', key, ':', value)


digits = string.digits
preffix = ['86', '87', '84', '85', '82']

def get_suffix():
	return ''.join([random.choice(digits) for _ in range(7)])

def generate_phone_number():
	return '+258' + random.choice(preffix) + get_suffix()

def check_phone_nr_validity(phone_number):
	# for phone_code in [f'8{x}' for x in [2, 3, 4, 5, 6, 7]]:
	# for phone_code in ['82', '83', '84', '85', '86', '87']:
	for phone_code in range(82, 88):
		if phone_number.startswith(f'{phone_code}') and len(phone_number) == 9:
			return 'Valid'
	return 'Invalid'

phone_numbers = [generate_phone_number() for _ in range(10)]
for phone_number in phone_numbers:
	phone_number = phone_number[-9:]
	print(f'{phone_number} is {check_phone_nr_validity(phone_number)}')