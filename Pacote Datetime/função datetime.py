import datetime

a = datetime.date(2025, 8, 21)
print(a)

a = datetime.MINYEAR
print(a)

print(datetime.MAXYEAR)
a = datetime.date.today()
print(a)

data_hora = datetime.datetime.today()
print(data_hora)

hora = datetime.time(2, 46, 00)
print(hora)

print(datetime.datetime.now())

print(datetime.datetime.now(datetime.UTC))
