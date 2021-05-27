This is a collection of script generate and used to complete the following task on th Google Automation with Python

Problem statement as follow:

You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. 
The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). 
The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. 
The contents of the HTML file need to be uploaded to a web service that is already running using Django. 
You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.
You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.
Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. 
The email should have a PDF attached with the name of the fruit and its total weight (in lbs). 
Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong. 

Script are exteung the following functions separately:
- change_image.py : Modify the image to upload
- upload.py : Upload the image
- upload_text.py : generate .jason file, associate the image, and upload description
- emails.py : module to send email
- reports.py : module to generate the report
- send_email_and_report.py : Call the email and reports module to generate the report and send the email
- health_check.py : monitor the system