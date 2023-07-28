import os
import math
from pathlib import Path
from datetime import datetime


def count_files_with_scandir(path):
	total = 0
	for entry in os.scandir(path):
		if entry.is_file():
			total += 1
		else:
			total += count_files_with_scandir(entry)
	return total

def count_files_with_pathlib(path):
	total = 0
	for entry in Path(path).iterdir():
		if entry.is_file():
			total += 1
		else:
			total += count_files_with_pathlib(entry)
	return total

# print(count_files_with_scandir(
# 	'./'))


def display_entries_in_directory(path):
	with os.scandir(path) as entries:
		for entry in entries:
			if entry.is_dir():
				print(f'Directory name: {entry.name}')
			else:
				print(f'Filename: {entry.name}')

# display_entries_in_directory('./')


def format_datetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formatted_date = utc_timestamp.strftime('%d %b %Y %H:%M:%S')
    return formatted_date

def convert_size(size_bytes):
	if size_bytes == 0:
		return 'OB'
	size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return '%s %s' % (s, size_name[i])

def display_entries_in_directory(directory):
	with os.scandir(directory) as entries:
		for entry in entries:
			print('Filename:', entry.name)
			info = entry.stat()
			# print(info.st_uid)
			# print(info.st_file_attributes)
			# print(info.st_gid)
			print('Creation time:', format_datetime(info.st_ctime))
			print('Last access time:', format_datetime(info.st_atime))
			print('Size:', convert_size(info.st_size))
			print()

display_entries_in_directory('./')




