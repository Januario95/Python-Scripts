import os
import requests

# url = 'https://pdfgoes.com/download/4266980-Hbr%20Guide%20To%20Finance%20Basics%20For%20Managers%20Hbr%20Guide%20Series.pdf'

# response = requests.get(url)

# with open('HBR-Guide-To-Finance-Basics.pdf', 'wb') as f:
#     f.write(response.content)

url = 'http://www.untag-smd.ac.id/files/Perpustakaan_Digital_1/BUSINESS%20Creating%20value%20successful%20business%20strategies..pdf'
response = requests.get(url)

with open('BUSINESS Creating Value Successful Business Strategies.pdf', 'wb') as f:
    f.write(response.content)

# path = 'C:/Software/wkhtmltox.exe'
# print(os.path.exists(path))













































