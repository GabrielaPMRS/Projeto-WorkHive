from email.message import EmailMessage
import smtplib
import ssl


class GmailHandler():
    email_sender = 'noreply.workhive@gmail.com'
    email_passward = 'glapmivmumcddcce'
       
    def send_email(self, email_receiver, subject, body):
        

        #criar uma instancia
        em = EmailMessage()
        em['From'] = self.email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_passward)
            smtp.sendmail(self.email_sender, email_receiver, em.as_string())