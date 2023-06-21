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
msg.add_alternative("""\
<!DOCTYPE html>
<html>
<head>
	<title>Example of h1 to h5 tags with different colors and emojis</title>
	<style>
		h1 {
			background-color: #F8D7DA;
			color: #721c24;
		}
		h2 {
			background-color: #FFE5B4;
			color: #856404;
		}
		h3 {
			background-color: #D1ECF1;
			color: #0c5460;
		}
		h4 {
			background-color: #D6E9C6;
			color: #155724;
		}
		h5 {
			background-color: #E2D5F9;
			color: #4d189d;
		}
	</style>
</head>
<body>
	<h1>This is the heading of the h1 tag 😃</h1>
	<p>Some text for the h1 tag.</p>

	<h2>This is the heading of the h2 tag 🚀</h2>
	<p>Some text for the h2 tag.</p>

	<h3>This is the heading of the h3 tag 🌻</h3>
	<p>Some text for the h3 tag.</p>

	<h4>This is the heading of the h4 tag 🐝</h4>
	<p>Some text for the h4 tag.</p>

	<h5>This is the heading of the h5 tag 🎉</h5>
	<p>Some text for the h5 tag.</p>
</body>
</html>
    
    
    
    
    
    """,subtype="html")

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