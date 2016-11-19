import datetime
import locale

def begin_message():
	begin = "%s  meu Amor"
	hour = datetime.datetime.now().strftime('%H') 
	if hour >= 0 and hour < 12 :
		return (begin %("Bom dia"))
	elif hour > 12 and hour < 18 :
		return (begin %("Bom tarde"))
	else :
		return (begin %("Boa noite")) 


def end_message():
	return "Eu te amo meu amor"