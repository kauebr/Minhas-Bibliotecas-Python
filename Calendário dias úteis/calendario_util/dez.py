from datetime import date
from calendar import monthrange
from workalendar.america import Brazil
lista = []
cal = Brazil()

dez = str(cal.add_working_days(date(2012, 12, 1), 15)) # 5 working days
print(dez)
lista.append(f"{dez[5:11]}-{dez[0:4]}")

print(lista)


