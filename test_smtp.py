import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl

smtp_server = 'smtp-mail.outlook.com'
port = 587
sender_email = 'dwightkschruteaitaskman@outlook.com'
password = 'Thisisformyai'
receiver_email = 'dwightkschruteaitaskman@outlook.com'

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'A Joke from Pam'

joke = '''Why did the AI break up with the database?

Because there was no spark in their relationship.

(Ba dum tss!)

Honestly though, I find this funny because I spend so much time thinking about databases and connections. And let's be real - sometimes the spark just isn't there.

- Pam'''

message.attach(MIMEText(joke, 'plain'))

try:
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print('SUCCESS: Email sent!')
except Exception as e:
    print(f'ERROR: {e}')
