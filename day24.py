import smtplib
sender = 'srijakandimalla@gmail.com'
password = 'kkclrxnyjwivsurv'
receiver = 'Wd.rkad@gmail.com'
messege = 'Thankyou for teaching us Python,sir'
with smtplib.SMTP('smtp.gmail.com', 587) as conn: #1
    conn.starttls()
    conn.login(sender, password)
    conn.sendmail(sender, receiver, messege)
print('Message sent successfully')

import smtplib
from email.message import EmailMessage
sender = 'srijakandimalla@gmail.com'
password = 'kkclrxnyjwivsurv'
receivers = ['Wd.rkad@gmail.com', 'srijakandimalla16@gmail.com']
msgobj = EmailMessage()
msgobj['From'] = 'srijakandimalla@gmail.com' 
msgobj['To'] = ','.join(receivers)
msgobj['Subject'] = 'SMTP mail'
msgobj.set_content("Hello Sir")
filenames = ['day21.py', 'day05.py', 'ocean.jpg']
for filename in filenames:
    with open(filename,'rb') as file:
        data = file.read()
        msgobj.add_attachment(data, maintype='application', subtype='octet-stream', filename=filename)
    
with smtplib.SMTP('smtp.gmail.com',587) as conn:
    conn.starttls()
    conn.login(sender,password)
    conn.send_message(msgobj)
print('Message sent successfully')