from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    # print(data_atual.day)
    print(data_atual.weekday())
    # print(data_atual.month)
    # print(data_atual.year)
    # print(data_atual.minute)
    tupla = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2022, 3, 26, 16, 10)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2022 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    print(type(data_convertida))

    nova_data = data_convertida - timedelta(days=365, hours= 2, minutes=15)
    print(nova_data)

def trabalhando_com_date():
    data_atual = date.today()
    print('Data atual: {}'.format(data_atual))
    print('Data atual: {}'.format(data_atual.strftime('%d/%m/%Y')))
    print(type('Tipo: {}'.format(data_atual)))
    data_atual_str = data_atual.strftime(' %A %B %Y') # dentro dos parametros posso está olhando a documentação e alterando conforme eu desejar
    print(data_atual_str)
    print('Tipo: {}'.format(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = print(horario.strftime('%H:%M:%S'))
    # print(type(horario))
    print(horario_str)
    print(type(horario_str))

if __name__ == '__main__':
    #trabalhando_com_date()
    # trabalhando_com_time()
    trabalhando_com_datetime()