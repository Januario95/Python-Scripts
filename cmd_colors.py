# import os
# import time
from colorama import Fore, Back, Style

# def change_color(code):
#     print('Priting random text here in cmd...')
#     os.system(f'color {code}')
#     time.sleep(3)

# color_codes = list(range(0, 10))

# for color in color_codes:
#     change_color(color)

print(Fore.RED, 'RED TEXT')
print(Back.GREEN, ' Green background')
print(Style.DIM, 'dim text')
print(Style.RESET_ALL)
print('back to normal')