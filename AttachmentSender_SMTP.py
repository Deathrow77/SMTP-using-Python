import smtplib
import base64
// use of SMTP to send attachments
sender = 'abc@gmail.com'
receiver = 'pqr@gmail.com'
file = open("C:\Users\Deathrow_77\Desktop\abc.txt", 'rb')
file1 = file.read()
rfile = base64.b64encode(file1)
part1 = """
To : To Person <parul654@gmail.com>
Subject : Using SMTP to send Attachments to other users
Content-Type : multipart/mixed;
"""
part2 = """
Content-Type: 'text/plain'
Please Find the attachment enclosed with  this mail...."""
part3 = """
Content-Type:multipart/mixed;
name = /"%s/"
Content-Transfer-Encoding: base64;
Content-Disposition : attachment ; filename = %s
%s
"""%(filename, filename, rfile)
Message = part1 + part2 + part3
try:
    smtplib.SMTP('localhost')
    smtplib.sendmail(sender, receiver, Message)
except smtplib.SMTPException as msg:
    print("Error : " + str(msg))