import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


lista_emails = ["", ""] # coloque os e-mails aqui

# Mensagem padrão
mensagem = """\
Assunto: Teste

Olá,

Sua mensagem aqui.

Atenciosamente,
Seu Nome
"""

# Configurações do servidor de e-mail Outlook
servidor_smtp = "smtp.office365.com" # Servidor SMTP
porta_smtp = 587
usuario = ""
senha = ""

# Conecta ao servidor
server = smtplib.SMTP(servidor_smtp, porta_smtp)
server.starttls()
server.login(usuario, senha)

# Loop para enviar e-mails
for email in lista_emails:
    # Cria a mensagem
    msg = MIMEMultipart() # Cria a mensagem
    msg.attach(MIMEText(mensagem, 'plain')) # Coloque a variável com a mensagem
    msg['From'] = usuario #Quem envia
    msg['To'] = email  #Quem recebe
    msg['Subject'] = 'Titulo do e-mail' # coloque o titulo aqui

    # Envia a mensagem
    server.sendmail(usuario, email, msg.as_string())

# Fecha a conexão
server.quit()
