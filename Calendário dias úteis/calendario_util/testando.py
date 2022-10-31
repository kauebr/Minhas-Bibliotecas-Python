import calendario_dias_uteis as cdu
import datetime

# Vou chamar a função e informar o periodo e a
# biblioteca vai me retornar uma lista com todos
# os dias últimos dias uteis de cada mes no período
lista = cdu.ultimo_util(2000, 2002)
print(lista)