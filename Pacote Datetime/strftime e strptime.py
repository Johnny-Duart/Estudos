import datetime

import pytz

data_atual = datetime.datetime.now()
data_str = "2025-08-26 20:18"
mascara_ptbr = "%d/%m/%Y %H:%M %a"
mascara_en = "%Y-%m-%d %H:%M"
fusohorario_brasil = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data_atual.strftime(mascara_ptbr))
data_convertida = datetime.datetime.strptime(data_str, mascara_en)
print(data_convertida)
print(fusohorario_brasil)

data = datetime.datetime.now(
    datetime.timezone(datetime.timedelta(hours=12), "Inexistente")
)
print(data)
print(data.tzname())
