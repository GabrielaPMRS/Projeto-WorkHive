from email.message import EmailMessage
import smtplib
import ssl


# Os emails de comunicação sairão sempre do gmail da empresa e ele não admite respostas.
# Todos os emails devem conter o email pessoal do empregados caso ele deseje continuar a conversa.
def send_email():
    email_sender = 'noreply.workhive@gmail.com'
    email_passward = 'glapmivmumcddcce'

    email_receiver = input('Email do destinatario: ')

    subject = input('Qual o assunto do seu email? ')
    print('\nLembre de informar uma forma de contato pessoal para futuro contato com o prestador de serviço.\n')
    body = input('Digite sua mensagem: ')

    #criar uma instancia
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_passward)
        smtp.sendmail(email_sender, email_receiver, em.as_string())