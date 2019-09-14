from email.mime.text import MIMEText
import smtplib


def email_sender(email_address, height, average_height, sample):
    sender_email = "doc.brain@tin.it"
    receiver_email = email_address
    subject = "Height data"
    message = f"<H3>Hey there!</H3><BR> Your height is <B>{height}</B>.<BR>" \
              f"The average height is <B>{average_height[0]}</B>.<BR>" \
              f"In a sample of {sample} users."
    email_msg = MIMEText(message, "html")
    email_msg["Subject"] = subject
    email_msg["To"] = receiver_email
    email_msg["From"] = sender_email
    mail_com = smtplib.SMTP("mail.tin.it", 25)
    mail_com.send_message(email_msg)
    mail_com.quit()
