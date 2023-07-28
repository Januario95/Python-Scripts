

import requests, zipfile, io

url = 'https://ocw.mit.edu/courses/15-835-entrepreneurial-marketing-spring-2002/a629d6561e3a8e28fde0dd89ce007172_prg.zip'
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall("entrepreneurial-marketing")

# print(help(zipfile.ZipFile))


# import wget
# wget.download(url)



