import smtplib


class Emailer:
    """
    Uses smtplib to send a gmail message
    """
    def __init__(self, username, password, destination):
        self.username = username
        self.password = password
        self.destination = destination

    def send_mail(self, amount):
        """
        Email sent through SMTP
        :return: True if mail is sent successfully. False otherwise.
        """
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.username, self.password)
            subject = 'Price fell down'
            body = f'Current price is lower than {amount}'
            message = f'Subject: {subject}\n\n{body}'
            server.sendmail(self.username, self.destination, message)
            server.quit()
            return True
        except smtplib.SMTPException as e:
            print(f'Something went wrong->{e}')
            return False
