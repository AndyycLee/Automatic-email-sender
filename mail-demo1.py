
import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

#could not figure out a way to rename
new_file_name = "___ Resume"

#desired emails to send to
contacts = ["desired emails to send to@gmail.com"]

msg = EmailMessage()
msg['Subject'] = 'Student seeking Software Engineering Roles'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts #change to --> contacts if you want to send to contacts, or as ", ".join(contacts) or to a specific email

#desired msg to send to contacts

msg.set_content("Hi, my name is  Thank you.\n\nBest,\n ")

# the path of the resume folder so folder/resume
files = ["folder\resume.pdf"]

for file in files:

    with open(file, "rb") as f:

        resume_data = f.read()
        #resume_type = imghdr.what(f.name) # only necessary for images
        resume_name = f.name
        

    msg.add_attachment(resume_data, maintype= 'application', subtype="octet-stream", filename=resume_name )

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)



# msg.add_alternative("""\
# <!DOCTYPE html>
# <html>
#     <body>
#         <h1 style="color:SlateGray;">This is an HTML Email!</h1>
#     </body>
# </html>
# """, subtype='html')
# useful https://www.youtube.com/watch?v=JRCJ6RtE3xU video tutorial
