import os
import glob 
import smtplib
from models import * 

# For guessing MIME type
import mimetypes

# Import the email modules we'll need
import email
import email.mime.application
from email.mime.multipart import MIMEMultipart
import os

origin = '/Users/lcosta5/Downloads/'
command = 'rm %s'

def get_file_name(name):
    split_name = name.split('/')
    position = len(split_name) -1
    return split_name[position]

def remove_files(file_name):
    os.system((command % (origin + '*.mobi')))

def send_email(books, smtp_client):
    message = MIMEMultipart()
    message['Subject'] = ' '
    message['From'] = smtp_client.user
    message['To'] = smtp_client.to
    for line in books :
        file = open(line, 'rb')
        attachament = email.mime.application.MIMEApplication(file.read(),_subtype="mobi")
        file.close()
        attachament.add_header('Content-Disposition','attachament',filename=get_file_name(line))
        message.attach(attachament)
    smtp = smtplib.SMTP(smtp_client.smtp)
    smtp.starttls()
    smtp.login(smtp_client.user,smtp_client.password)
    smtp.sendmail(smtp_client.user,[smtp_client.user], message.as_string())
    smtp.quit()

def main():
    books = glob.glob(origin + '*.mobi')
    if books : 
        client = smtp_client("lcosta.sp.br@outlook.com", "juh&leh@23", "smtp-mail.outlook.com:587", "lcosta.sp.br@Kindle.com")
        send_email(books, client)
        remove_files(book_name)

if '__main__' == __name__ :
    main()