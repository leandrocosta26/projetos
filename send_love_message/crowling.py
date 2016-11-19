# -*- encoding=Utf-8 -*-

from requests import get
import re
from pymongo import MongoClient
import datetime

if __name__ == "__main__" :
	
	client = MongoClient('localhost', 27017)
	today = datetime.datetime.now()
	next_date = None
	day_add = 1;

	
	url = "https://pensador.uol.com.br/frases_de_amor/"
	for index in range(1, 20) :
		if index > 1 :
			url = ("%s%s%s" % (url, index,"/"))  
		
		result = get(url) 
		frases = re.findall(r'class="frase fr" id="\w*"\>(...*)\<\/p\>', result.text)
		for frase in frases:
			next_date = (today + datetime.timedelta(days=day_add))
			json = {"frase" : frase, "date" : next_date.strftime("%d/%m/%Y")}
			client['send_message']['frases'].insert_one(json)
			day_add = day_add + 1