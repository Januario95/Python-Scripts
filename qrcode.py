import os
import time
import segno
from segno import helpers

# wifi_settings = {    
#     'ssid': 'Dangerous WIFI',
#     'password': 'Jaci1995',
#     'security': 'WPA'
# }
# wifi = segno.helpers.make_wifi(**wifi_settings)
# wifi.save("Wifi.png", dark="yellow", light="#323524", scale=8)
# os.system('start Wifi.png')

def open_file(filename):
    time.sleep(1)
    os.system(f'start QRCodes/{filename}.png')

price_tag = segno.make('Hello World')
if not os.path.exists('QRCodes'):
    os.mkdir('QRCodes')
# price_tag.save('QRCodes/hello-world.png')

# qrcode = segno.make('Vampure Blues')
# qrcode.save('QRCodes/vampire-blues.png', border=5)

# qrcode = segno.make_qr('Welcome')
# qrcode.save('QRCodes/welcome.png', scale=10)
# open_file('welcome')

# qrcode = segno.make('Green av, Kingston')
# qrcode.save('QRCodes/address.png', dark='darkgray',
#             light='teal', scale=10)
# open_file('address')

# qrcode = segno.make('Green ave, Kingston')
# qrcode.save('QRCodes/address2.png', dark='#0000ffcc',
#             scale=10)
# qrcode.save('QRCodes/Beatles.svg')
# qrcode.save('QRCodes/Beatles.eps')
# open_file('address2')

# micro_qrcode = segno.make('Rain', error='q')
# micro_qrcode.save('QRCodes/rain.png', dark='darkblue',
#                   data_dark='steelblue', scale=5)
# open_file('rain')

# video = segno.make('https://www.youtube.com')
# video.save('QRCodes/video.png', dark='yellow',
#            light='#323524', scale=5)
# open_file('video')


# qrcode = helpers.make_wifi(ssid='myWIFI',
#                            password='Test123456789',
#                            security='WPA')
# print(qrcode.designator)
# print(dir(qrcode))
# qrcode.save('QRCodes/wifi-access.png', scale=10)
# open_file('wifi-access')

# wifi_settings = {
#     'ssid': 'WIFI',
#     'password': 'Test1234567890',
#     'security': 'WPA'
# }
# wifi = segno.helpers.make_wifi(**wifi_settings)
# wifi.save('QRCodes/wifi.png', dark='yellow',
#           light='#323524', scale=8)
# open_file('wifi')

qrcode = helpers.make_mecard(
    name='Januario Cipriano',
    email='januario.cipriano@gmail.com',
    phone='+258 86 940 2316',
    url=['https://www.januario-cipriano.com',
         'https://www.januario-cipriano.co.mz'])
print(qrcode.designator)
qrcode.save('QRCodes/mycontact.png', scale=5)
open_file('mycontact')

# print(help(segno.helpers.make_geo))
# qrcode = segno.helpers.make_geo(lat=25.9692,
#                                 lng=32.5732)
# qrcode.save('QRCodes/lat-lng.png', scale=8)
# open_file('lat-lng')

# print(help(segno.helpers.make_email))
# qrcode = segno.helpers.make_email(
#     to='januario.cipriano@gmail.com',
#     cc='januario.cipriano@gmail.com',
#     subject='Complete Coursera course',
#     body='''
# Dear Sir/Madam.
    
# This is a reminder that you should complete your course
# on Coursera.

# Yours,
# Januario Cipriano
# ''')
# qrcode.save('QRCodes/email.png', scale=8)
# open_file('email')

# print(help(segno.helpers.make_epc_qr))
# print(help(segno.helpers))