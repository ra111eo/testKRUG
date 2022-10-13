# coding: cp1251
from stringToDatetime import string_to_datetime
from mainLogic import body

print('\nДля выхода из программы введите в любое из полей ввода команду "exit"\n',)
while True:
    start_pointer = string_to_datetime(input('Введите начало диапазона:'))
    if start_pointer != '':
        stop_pointer = string_to_datetime(input('Введите конец диапазона:'))
        if stop_pointer != '':
            try: 
                aperture = float(input('Введите значение апертуры:'))
                body(start_pointer,stop_pointer,aperture)
            except ValueError as ve:
                print('Ошибка ввода данных:', ve)
                print()
        