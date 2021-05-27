#!/usr/bin/env python3
"""Report an error if CPU usage is over 80%
Report an error if available disk space is lower than 20%
Report an error if available memory is less than 500MB
Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1
Email data to be insert"""

import psutil
import socket
import emails
import os

# Checking system
cpu_percent = psutil.cpu_percent()
disk_used = dict(psutil.disk_usage('/')._asdict())['percent']
ram_free = dict(psutil.virtual_memory()._asdict())["available"]/ 1024 ** 2 #convert to MB
localhost = socket.gethostbyname('localhost')

#preparing the email
def alarm(error):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = error
    body = "Please check your system and resolve the issue as soon as possible."
  
    message = emails.generate(sender, receiver, subject, body)
    emails.send(message)

def system_check():
    if cpu_percent > 80:
        sub = "Error - CPU usage is over 80%"
        alarm(sub)
    if disk_used > 80:
        sub = "Error - Available disk space is less than 20%"
        alarm(sub)
    if ram_free < 500:
        sub = "Error - Available memory is less than 500MB"
        alarm(sub)
    if localhost != "127.0.0.1":    
        sub = "Error - localhost cannot be resolved to 127.0.0.1"
        alarm(sub)

if __name__ == "__main__": 
    system_check() 
    #print(cpu_percent,disk_used,ram_free,localhost)




