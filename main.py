from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("gemini_api_key")

smtp_server = os.getenv("smtp_server")
smtp_port = 587
reciever_email = os.getenv("reciever_email")
sender_email = os.getenv("sender_email")
password = os.getenv("sender_password")

setting = "the cab of his car."

import llm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = reciever_email
message["Subject"] = "Valentine's Russian Words Of The Day"

header = f"""
    <h3
    style="background-color: red; color: white; padding: 5px;"
    >
    This week's setting: {setting}
    </h3>
"""
body = f"""
    <p>
    {llm.getTodaysWords(gemini_api_key, setting)}
    </p>
"""
message.attach(MIMEText(header, "html"))
message.attach(MIMEText(body, "html"))

#send the email
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
    server.quit();