import time
from datetime import datetime
import pickle

store = {}

# dictionary format: data=[{fid: val1}, {fid: val2}, {msg: val3}]
def addToDB(ch, **kwargs):
	date = getDate()

	if 'msg' in kwargs:
		input_type = 'msg'
		d = kwargs['msg']
	if 'fid' in kwargs:
		input_type = 'fid'
		d = kwargs['fid']

	entry = {input_type: d, "channel": ch}

	if date in store:
		store[date].append(entry)
	else:
		store[date] = [entry]
	return entry

# get either entries with specified date or date and other flags 
def get(ch, date):
	result = []
	if date in store:
		data = store[date]
		for item in data:
			if item["channel"]==ch:
				result.append(item)
	return result		

def getDate():
	now = datetime.now()
	date = str(now.month) +"/"+ str(now.day) + "/" + str(now.year)
	return date

def remove(date):
	if date in store:
		del store[date]

def save(filename):
	with open(filename, 'wb') as storage:
		pickle.dump(store, storage)

def load(filename):
	with open(filename, 'rb') as storage:
		return pickle.load(storage)