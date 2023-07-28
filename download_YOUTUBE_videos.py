import time
from pytube import YouTube

def Download(link):
	youtubeObject = YouTube(link)
	# print(dir(youtubeObject.streams))
	try:
		youtubeObject_ = youtubeObject.streams.get_highest_resolution()
		print(youtubeObject_.title)
		youtubeObject_.download()
		print('First attempt: Downloading file...')
		print("Download is completed successfully")
	except Exception as e:
		print("An error has occurred")
		print(e.args)
		if e.args[0] == 'streamingData':
			# youtubeObject.streams.download()
			print('Second attempt: Downloading file...')


link = 'https://www.youtube.com/watch?v=XKuVKvSzfm0&feature=youtu.be'
URLS = [
	'https://www.youtube.com/watch?v=oXrlgOEiy6o',
	'https://www.youtube.com/watch?v=sf_ac-dYh3w',
	'https://www.youtube.com/watch?v=fnh-Ux4Jj5E',
	'https://www.youtube.com/watch?v=6JCyMPfRxoM',
	'https://www.youtube.com/watch?v=cLOT0APQzDs',
	'https://www.youtube.com/watch?v=khLaYtW5N4s',
	'https://www.youtube.com/watch?v=648mhdth6i0',
	'https://www.youtube.com/watch?v=8EtqMN7aD7A'


	# 'https://www.youtube.com/watch?v=DscBD4HK5y0',
	# 'https://www.youtube.com/watch?v=67MECnBhD_c',
	# 'https://www.youtube.com/watch?v=sOLRevIjLXY',
	# 'https://www.youtube.com/watch?v=vlYLenSMIG8',
	# 'https://www.youtube.com/watch?v=PXSWCu_3sTc',
	# 'https://www.youtube.com/watch?v=IfQtoQ2eK8w',
	# 'https://www.youtube.com/watch?v=2ZMWEGBQF14'
]
# for link in URLS:
# 	Download(link)
# 	time.sleep(1.5)

Download(link)

# link = 'https://www.youtube.com/watch?v=oXrlgOEiy6o'
# youtubeObject = YouTube(link)
# youtubeObject = youtubeObject.streams.get_highest_resolution()
# print(youtubeObject.title)
# youtubeObject.download()



