import smtplib
from email.message import EmailMessage
import imghdr
email="ranahassan427726@gmail.com"
password="nbebxkllbgcytukt"

contactes=["Sufyanrahman48@gmail.com","rana427726@gmail.com"]
message=EmailMessage()
message["Subject"]="Lorem ipsum dolor"
message["from"]=email
message["to"]=",".join(contactes)
message.set_content("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
pictures=["earth.jpg","moon.jpg","project.jpg"]
for pic in pictures:
	with open(pic,"rb")as f:
		file_data=f.read()
		file_type=imghdr.what(f.name)
		file_name=f.name
	message.add_attachment(file_data,maintype="image",subtype=file_type,filename=file_name)
pdfs=["cv.pdf","data.pdf"]
for pds in pdfs:
	with open(pds,'rb')as k:
		file_data1=k.read()
		file_type1=imghdr.what(k.name)
	message.add_attachment(file_data1,subtype="octet-stream",maintype="application",filename=file_name)
	with smtplib.SMTP_SSL("smtp.gmail.com",465)as smtp:
		smtp.login(email,password)
		smtp.send_message(message)

