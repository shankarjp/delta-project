#Email Client Python

def sendMail(sender_email, sender_password, reciever_email, subject, body, files):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = reciever_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    SERVER_PATH = ./
    for attach_file in files:
        attachment = open(SERVER_PATH + attach_file, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {attach_file}")
        message.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        content = message.as_string()
        smtp.send_message(content)
