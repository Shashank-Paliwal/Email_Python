import smtplib

sender = "paliwalshashank648@gmail.com"
receiver = "500095932@stu.upes.ac.in"
password = "palionfire"
subject = "Python Email Test"
body = "I wrote an email XD"

#header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender, password)
print("Logged in...")
server.sendmail(sender, receiver, message)
print("Email has been sent!")