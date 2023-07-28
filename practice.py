import os
import sys
import time
import random
import PyPDF2
import argparse
import pandas as pd

class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print(f'Opening the file {self.filename!r}')
        self.__file = open(self.filename, self.mode)
        return self.__file
    
    def __exit__(self, exc_tye, exc_value, exc_traceback):
        print(f'Closing the file {self.filename!r}')
        if not self.__file.closed:
            self.__file.close()
        return False 
    
# with File('data.txt', 'r') as f:
#     print(next(f))

class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop = time.perf_counter()
        self.elapsed = self.stop - self.start
        return False
    
def fibonacci(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a + b
    return a

# with Timer() as timer:
#     for x in range(1, 10000):
#         fibonacci(x)
        
# print(timer.elapsed)

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
    raise TypeError('Color value must be between 0 and 255')

def dispaly_text_std(text, delay=0.01):
    sys.stdout.write('\t')
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print('')
    time.sleep(0.5)

class MyColor:
    def __init__(self):
        self.red = 50
        self.green = 13
        self.blue = 167

    def __getattr__(self, attr):
        if attr == 'rgbcolor':
            return (self.red, self.green, self.blue)
        elif attr == 'hexcolor':
            return '#{0:02x}{1:02x}{2:02x}'.format(
                self.red, self.green, self.blue
            )
        
    def __setattr__(self, attr, val):
        if attr == 'rgbcolor':
            self.red = check_value(val[0])
            self.green = check_value(val[1])
            self.ble = check_value(val[2])
        else:
            super().__setattr__(attr, val)

c1 = MyColor()
# print(c1.hexcolor)
# print(c1.rgbcolor)
print('')
colors = []
for _ in range(50000):
    c1.rgbcolor = generate_codes()
    color = (c1.hexcolor, c1.rgbcolor)
    if color not in colors:
        colors.append(color)

    # text = f'hex: {c1.hexcolor}. \trgb: {c1.rgbcolor}'
    # dispaly_text_std(text, delay=0.09)

df = pd.DataFrame(colors)
print(df.head())
df.to_excel('colors.xlsx', index=False)
os.system('start colors.xlsx')

# filename = 'A Manager Guide to Finance & Accounting.pdf'
# print(os.path.exists(filename))
# file = open(filename, 'rb')
# reader = PyPDF2.PdfFileReader(file)
# num_pages = reader.numPages
# page = reader.getPage(1)
# text = page.extractText()
# for line in text.split('\n'):
#     dispaly_text_std(line)

