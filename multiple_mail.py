import smtplib
from email.message import EmailMessage
from PIL import Image
import imghdr
email="chwaleednasir5@gmail.com"
password="aigedagmgmgmpptk"


contactes=["itzmudassir07@gmail.com","ranahassan427726@gmail.com","attiqrana18@gmail.com"]

msg=EmailMessage()
msg["Subject"]="Lorem ipsum dolor"
msg["From"]=email
msg["To"]=",".join(contactes)
msg.set_content("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
pictures=["app.jpg","Test-picture.png"]
for picture in pictures:
    with open(picture,"rb") as f:
        file_data=f.read()
        file_type=imghdr.what(f.name)
        file_name=f.name
    msg.add_attachment(file_data,maintype="image",subtype=file_type,filename=file_name)
project_requriments=["project_requriment.pdf","invoice 24nov.pdf"]
for project_requriment in project_requriments:
    with open(project_requriment,"rb") as a:
        file_data1=a.read()
        file_name1=a.name
    msg.add_attachment(file_data1,maintype="application",subtype="octet-stream",filename=file_name1)
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(email,password)
        smtp.send_message(msg)