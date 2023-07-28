#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Created on Wed May 10, 2023 08:09:23

@author: a248433
"""

import os
import nltk
import PyPDF2
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')

def get_filename(name, ext):
	return f'{name}.{ext}'

file = open(
	get_filename('JOINT_CSA_HUNTING_RU_INTEL_SNAKE_MALWARE_20230509', 'pdf'), "rb")
reader = PyPDF2.PdfFileReader(file)
num_pages = reader.numPages
page = reader.getPage(0)
text = page.extractText()
# print(text)

# print(num_pages)
words = {}
all_words = ''
for page_num in range(num_pages-1):
	page = reader.getPage(page_num)
	text = page.extractText()
	for line in text.split(' '):
		if len(line) > 1:
			line = line.replace('\n', '')
			all_words += (' ' + line)



text_tokens = word_tokenize(all_words)
tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
# print(tokens_without_sw)

for word in tokens_without_sw:
	if word in words:
		words[word] += 1
	else:
		words[word] = 1

words_ = []
counts = []
for word, count in words.items():
	words_.append(word)
	counts.append(count)


df = pd.DataFrame({
	'Word': words_,
	'Count': counts
})
df.sort_values(by=['Count'], ascending=False, inplace=True)
# df = pd.read_excel(filename)
# df['Count'] = df['Count'].astype()
df = df[df['Count'] > 4]
df = df[df['Word'].str.len() > 1]
print(df)
filename = get_filename('JOINT_CSA_HUNTING_RU_INTEL_SNAKE_MALWARE_20230509', 'xlsx')
df.to_excel(filename, index=False)
os.system('start JOINT_CSA_HUNTING_RU_INTEL_SNAKE_MALWARE_20230509.xlsx')

