"""
Email Automation Tool
=====================

A Python script to automate sending emails with attachments using smtplib.

Key Features
------------

* Bulk email sending
* Dynamic content generation
* Custom templates

Usage
-----

1. Install the required packages by running `pip install -r requirements.txt`
2. Configure the email settings in `settings.py`
3. Run the script using `python main.py`

"""

import smtplib
import os
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
from settings import EMAIL_SETTINGS

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def send_email_with_attachment(subject, message, from_addr, to_addr, attachment=None):
    """Send an email with an optional attachment"""
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    if attachment:
        with open(attachment, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                'attachment; filename="%s"' % os.path.basename(attachment)
            )
            msg.attach(part)

    with smtplib.SMTP(EMAIL_SETTINGS['SMTP_SERVER'], EMAIL_SETTINGS['SMTP_PORT']) as server:
        server.starttls()
        server.login(EMAIL_SETTINGS['FROM_EMAIL'], EMAIL_SETTINGS['FROM_PASSWORD'])
        server.send_message(msg)


if __name__ == '__main__':
    # Replace with your own email list
    emails = ['email1@example.com', 'email2@example.com']

    # Replace with your own template
    with open('template.html', 'r') as f:
        template = f.read()

    for email in emails:
        # Replace with your own dynamic content
        name = email.split('@')[0]
        subject = 'Hello {}!'.format(name)
        message = template.format(name=name)

        # Replace with your own attachment
        attachment = 'attachment.txt'

        send_email_with_attachment(
            subject, message, EMAIL_SETTINGS['FROM_EMAIL'], email, attachment
        )