import logging
from datetime import date

log_data_name = str(date.today()).split('-') 

'''
logging.basicConfig(
	filename='media/logs/'+log_data_name[0]+'/'+log_data_name[1],
	filemode='a',
	encoding='utf-8', 
	level=logging.DEBUG,
	format='%(asctime)s %(message)s',
	datefmt='%m/%d/%Y %I:%M:%S %p',
	)

'''