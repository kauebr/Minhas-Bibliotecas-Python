def ultimo_util(ano_inicial, ano_final):
    from datetime import date
    from calendar import monthrange
    from workalendar.america import Brazil
    meses = {1:'Jan', 2:'Fev', 3:'Mar', 4:'Abr', 5:'Mai', 6: 'Jun', 7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'}
    datas = []
    primeiro_dia_mes = 1
    cal = Brazil()
    for ano in range(ano_inicial, ano_final+1):
        for mes in meses.keys():
            ultimo_dia_mes = monthrange(ano,mes)
            ultimo_dia_mes = ultimo_dia_mes[1]
            total_dias_uteis_mes = cal.get_working_days_delta(date(ano, mes, primeiro_dia_mes), date(ano, mes, ultimo_dia_mes))
            for dia in range(ultimo_dia_mes, 24, -1):
                if cal.is_working_day(date(ano, mes, dia)) == True:
                    ultimo_dia_util = dia
                    if mes == 12:
                        dez = str(cal.add_working_days(date(ano, 12, 1), 15)) # colocando 15 dias uteis apos o dia 1 se for dezembro
                        datas.append(f"{dez[5:11]}-{dez[0:4]}") # fatiando e invertendo a str para ficar no formato
                        break
                    else:
                        datas.append(f"{mes}/{dia}/{ano}")
                        # print(f'O último dia útil de {meses[mes]}/{ano} : {dia}')
                        break
    return datas


