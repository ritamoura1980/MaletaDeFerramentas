import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(to_email, subject, body):
    from_email = "seu.email@gmail.com"
    from_password = "sua_senha"
    
    # Configuração do servidor SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Cria a mensagem
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Conecta ao servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, from_password)
        server.send_message(msg)
        server.quit()
        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Falha ao enviar email: {e}")

def monitorar_espaco_disco(threshold=80):
    # Obtém informações sobre as partições do disco
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        percent_used = usage.percent
        
        print(f"Espaço usado em {partition.mountpoint}: {percent_used}%")
        
        if percent_used > threshold:
            subject = "Alerta: Uso do Disco Acima de 80%"
            body = f"O espaço utilizado no disco {partition.mountpoint} ultrapassou {threshold}%. Uso atual: {percent_used}%."
            enviar_email("adm@adm.com.br", subject, body)

# Chama a função para monitorar o espaço em disco
monitorar_espaco_disco()