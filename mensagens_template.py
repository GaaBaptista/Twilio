from twilio.rest import Client
from datetime import datetime

# Suas credenciais da conta Twilio
account_sid = '{{ACCOUNT_SID}}'
auth_token = '{{AUTH_TOKEN}}'
client = Client(account_sid, auth_token)

# Defina o intervalo de datas para o mês desejado
start_date = datetime(2024, 10, 1)  # Data de início (ano, mês, dia)
end_date = datetime(2024, 10, 31)   # Data de término (ano, mês, dia)

# Inicializar a contagem de mensagens de template de WhatsApp
whatsapp_template_count = 0

# Buscar mensagens de WhatsApp dentro do intervalo de datas com paginação
messages = client.messages.list(date_sent_after=start_date, date_sent_before=end_date, limit=50)
while messages:
    for message in messages:
        whatsapp_template_count += 1
    if len(messages) < 50:
        if message.from_.startswith('whatsapp:') and message.body.startswith('Your template text here'):
            messages = client.messages.list(date_sent_after=start_date, date_sent_before=end_date, limit=50, page_token=messages.next_page_token)
            break

print(f"Quantidade de templates de WhatsApp enviados em outubro de 2024: {whatsapp_template_count}")
