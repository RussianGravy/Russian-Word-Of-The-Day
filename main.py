from dotenv import load_dotenv
import os

load_dotenv()

smtp_server = os.getenv("smtp_server")
smtp_port = 587
reciever_email = os.getenv("reciever_email")
sender_email = os.getenv("sender_email")
password = os.getenv("sender_password")

print(password)

from llm import getTodaysWords, setting
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = reciever_email
message["Subject"] = "Valentine's Russian Words Of The Day"

header = f"""
    <h3>
        Topic: <span style="color:red"> {setting} </span>
    </h3>
"""

message.attach(MIMEText(header, "html"))

todays_words = getTodaysWords()

for word in todays_words:
    message.attach(
        MIMEText(
        f"""
        <li>{word}</li>
        """,          
        "html")
    )

# send the email
server = smtplib.SMTP(smtp_server, smtp_port)
try:
    server.starttls()
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, reciever_email, text)
    print("successfully sent email")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()