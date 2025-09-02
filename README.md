# Python-Email-Sender
A script for sending automated emails using Python's standard library.
# Python Email Sender

This repository contains a simple Python script for sending emails using the built-in **`smtplib`** library. It's a fundamental skill for any developer looking to automate notifications, reports, or alerts.

## Features
- Sends plain-text emails.
- Uses standard library modules, no external dependencies required.

## Requirements
- An email account with "less secure app access" enabled or a generated "app password."

## Configuration
1. Open `send_email.py`.
2. Replace `sender_email`, `password`, and `recipient_email` with your credentials and the recipient's email address.
   - For Gmail, you need to create an App Password.
3. Run the script from your terminal:
   ```
   python send_email.py
   ```
