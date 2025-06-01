# Treinamento Python DIO
# Projeto Treinamento DIO - Trabalhando com objetos date, datetime e time em Python

# módulo datetime

import datetime

d = datetime.date(2023, 10, 1)
print(d)  # Saída: 2023-10-01

from datetime import date
d = date(2023, 7, 10)
print(d)  # Saída: 2023-07-10

# Objeto date

print(date.today())  # Saída: data atual

# Objeto datetime

from datetime import date, datetime, time

data_hora = datetime(2023, 7, 10)
print(data_hora)  # Saída: 2023-07-10 00:00:00
print(datetime.today())  # Saída: data e hora atual
print(datetime.now())  # Saída: data e hora atual

# Objeto time

hora = time(10, 20, 0) # 10 horas, 20 minutos e 0 segundos
print(hora)  # Saída: 10:20:00

# manipulação de data e hora

import datetime

d = datetime.datetime(2023, 7, 19, 13, 45)
print(d)  # Saída: 2023-07-19 13:45:00

d = d + datetime.timedelta(weeks=1)  # Adiciona 1 semana
print(d)  # Saída: 2023-07-26 13:45:00



from datetime import datetime, timedelta, date

tipo_carro = 'M' # P, M, G
tempo_pequeno = 30
tempo_medio =  45
tempo_grande = 60
data_atual = datetime.now()
#data_mundial = datetime.utcnow()

print('=' * 100) 


# Exemplo de uso de condicionais com tipo de carro
if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou: {data_atual} e ficará pronto em: {data_estimada}')
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou: {data_atual} e ficará pronto em: {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou: {data_atual} e ficará pronto em: {data_estimada}')

print(date.today() - timedelta(days=1))  # Saída: data de ontem
# print(time(10, 19, 20)) - timedelta(hours=1) formato não suportado

resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())  # Saída: 09:19:20

print(datetime.now().date())  # Saída: data atual
print(datetime.now().time())  # Saída: hora atual

# conversão de datas de horas usando strftime e strptime

import datetime

d = datetime.datetime.now()

print(d.strftime('%d/%m/%Y %H:%M:%S'))  # Saída: 25/07/2023 10:19:20

date_string = '20//07/2023 15:30'

d = datetime.datetime.strptime(date_string, '%d//%m/%Y %H:%M') # Converte string para datetime
print(d)  # Saída: 2023-07-20 15:30:00

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = '2023-10-20 10:20'
marcara_ptbr = '%d/%m/%Y'
mascara_en = '%Y-%m-%d %H:%M'

print(data_hora_atual.strftime(marcara_ptbr))  # data atual formatada
print(datetime.strptime(data_hora_str, mascara_en))  # Converte string para datetime com máscara em inglês

# Exemplo de uso de data e hora com timezone usando pytz

import datetime
import pytz

print('=' * 100)

d = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
print(d)  # Saída: data e hora atual com timezone de São Paulo
d_utc = datetime.datetime.now(pytz.utc)
print(d_utc)  # Saída: data e hora atual em UTC

d = datetime.datetime.now(pytz.timezone('America/Campo_Grande'))
print(d)  # Saída: data e hora atual com timezone de Campo Grande

import pytz
from datetime import datetime

data = datetime.now(pytz.timezone('Europe/Oslo'))
print(data)  # Saída: data e hora atual com timezone de Oslo

# Exemplo de uso de timezone com datetime
from datetime import datetime, timezone

d = datetime.now(timezone(timedelta(hours=2)))
print(d)  # Saída: data e hora atual com timezone de + 2 horas
d = datetime.now(timezone(timedelta(hours=-3), 'BRT'))
print(d)  # Saída: data e hora atual com timezone de -3 horas