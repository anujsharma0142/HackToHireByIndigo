import smtplib
from email.mime.text import MIMEText
from app.utils.logger import logger
from config.config import get_email_config


config = get_email_config()


class MailService:
    def __init__(self):
        self.service_email = config['service_email']
        self.service_password = config['service_password']
        self.host = config['smtp_host']
        self.port = config['smtp_port']

    def send_email(self, subject: str, body: str, to_email: str):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.service_email
        msg['To'] = to_email

        try:
            server = smtplib.SMTP_SSL(self.host, self.port)
            server.login(self.service_email, self.service_password)
            server.sendmail(self.service_email, [to_email], msg.as_string())
            server.quit()
            logger.info("Email sent successfully")
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
