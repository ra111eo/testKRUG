# coding: cp1251
from stringToDatetime import string_to_datetime
from mainLogic import body

print('\n��� ������ �� ��������� ������� � ����� �� ����� ����� ������� "exit"\n',)
while True:
    start_pointer = string_to_datetime(input('������� ������ ���������:'))
    if start_pointer != '':
        stop_pointer = string_to_datetime(input('������� ����� ���������:'))
        if stop_pointer != '':
            try: 
                aperture = float(input('������� �������� ��������:'))
                body(start_pointer,stop_pointer,aperture)
            except ValueError as ve:
                print('������ ����� ������:', ve)
                print()
        