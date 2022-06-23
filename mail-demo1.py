
import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

new_file_name = "Andy's Resume"

contacts = ["judgejudybooty123@gmail.com"]

msg = EmailMessage()
msg['Subject'] = 'Student seeking Software Engineering Roles'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts #change to --> contacts if you want to send to contacts, or as ", ".join(contacts) or to a specific email

msg.set_content("Hi, my name is Andy. I'm currently a student but I'm planning on taking a gap year. I believe I'd be a perfect fit for your company as a young and passionate software engineer as an intern or \
for avaliable fulltime positions as well. Attached below is my resume, it also holds my GitHub and LinkedIn information. Thank you.\n\nBest,\nAndy")

files = ["recurse\current_resumee.pdf"]

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
