import smtplib
from email.mime.text import MIMEText
import os

sender_email = "your_email@gmail.com"
password = "your_app_password"
recipient_email = "recipient_email@example.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587

def send_email(sender, recipient, subject, body):
    """
    Sends a plain-text email.
    """
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    subject = "Python Automated Email"
    body = "This is a test email sent from a Python script."
    send_email(sender_email, recipient_email, subject, body)
