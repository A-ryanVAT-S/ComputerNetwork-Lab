import smtplib
from email.mime.text import MIMEText

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "aryanvatsa2018@gmail.com"
password = "kuoifqwzhtyapwnq"
receiver_email = "aryanvats0909@gmail.com"

message = MIMEText("This is a test email sent from a Python script.")
message["Subject"] = "SMTP Test"
message["From"] = sender_email
message["To"] = receiver_email

try:
    server = smtplib.SMTP(smtp_server, port)
    server.set_debuglevel(1)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("\nEmail sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    if 'server' in locals():
        server.quit()
