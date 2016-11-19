import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from pymongo import MongoClient
from types_message import begin_message	

def builder_data(to, from_mail ,subject, body, sm):
	header = "To:%s\nFrom:%s\nSubject:%s\n%s"
	response =  (header % (to, from_mail ,subject, body))
	sm.sendmail(from_mail, to, header)


def get_phrase():
	today = datetime.datetime.now().strftime("%d/%m/%Y")
	client = MongoClient('localhost', 27017)
	result = client['send_message']['frases'].find_one({"date" : today })
	# client['sendmailnd_message']['frases'].remove({"date" : today }
	return result["frase"]


def send_email():
	# message['To']="lcosta.sp.br@gmail.com" #"juliana.araujo.ramalho@gmail.com"
	smtp = smtplib.SMTP("smtp-mail.outlook.com:587")
	smtp.starttls()
	smtp.login("lcosta.sp.br@outlook.com","juh&leh@23")
	builder_data("lcosta.sp.br@gmail.com",
		"lcosta.sp.br@outlook.com",
		"Projeto 365 dias de mensagem",
		get_phrase(),
		smtp)
	smtp.quit()

def main():
	send_email()

if __name__ == "__main__":
	main()
