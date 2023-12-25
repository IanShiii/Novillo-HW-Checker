from email.mime.text import MIMEText 
from email.mime.image import MIMEImage 
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart 
import smtplib 
import os 
import json

def email(text): 

    with open("..\config\config.json") as config:
        config = json.load(config)

    smtp = smtplib.SMTP(host='smtp.gmail.com', port=587) 
    smtp.ehlo() 
    smtp.starttls() 
    smtp.login(user=config['loginUser'], password=config['loginPass']) 

    msg = MIMEMultipart() 
    msg['Subject'] = "Novillo APCSA HW"
    to = config['recipients']
    msg.attach(MIMEText(text))   
    
    smtp.sendmail(from_addr=config['loginUser'], to_addrs=to, msg=msg.as_string())

    smtp.quit()