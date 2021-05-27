#!/usr/bin/env python3
""" Generate Pdf report from .txt in a directory and send the report trough email
need: sys 1(destination path for the pdf report) 
      sys 2(directory where the .txt are stored)

Email data to be add in the body : if __name__ == "__main__ (line42)"     
      """

import reports
import os
import sys
from datetime import date
import emails

# iterate trough directory .txt to generate the text to insert in the report 
def text_fun(directory):
    pdf= ""
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            with open(directory + file, "r") as f:
                lines = f.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>" 
    return(pdf)




if __name__ == "__main__":
    #Organize argument to be passed to report.py
    report_name = sys.argv[1]
    title = "Processed Update on {}".format(date.today())
    pdf_body = text_fun(sys.argv[2])
    #run report.py
    try:  
        reports.generate_report(report_name, title, pdf_body)
        print("Created {} , check if it's look as expected :)".format(report_name))
    except OSError:
        print("!!!ERROR!!! Something went wrong we cannot generate the report")    

    #email data
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  
    #send the email(emails.py)
    message = emails.generate(sender, receiver, subject, body, report_name)
    emails.send(message)
    

