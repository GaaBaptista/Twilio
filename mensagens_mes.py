from twilio.rest import Client
from datetime import datetime

# Suas credenciais da conta Twilio
account_sid = '{{ACCOUNT_SID}}'
auth_token = '{{AUTH_TOKEN}}'
client = Client(account_sid, auth_token)

# Defina o intervalo de datas para o mês desejado
start_date = datetime(2024, 10, 1)  # Data de início (ano, mês, dia)
end_date = datetime(2024, 10, 31)   # Data de término (ano, mês, dia)

# Buscar mensagens dentro do intervalo de datas
messages = client.messages.list(date_sent_after=start_date, date_sent_before=end_date)


# Contar o número de mensagens
message_count = len(messages)

print(f"Quantidade de mensagens trocadas em outubro de 2024: {message_count}")
