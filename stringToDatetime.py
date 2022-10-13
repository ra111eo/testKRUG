# coding: cp1251
import sys
import datetime
from datetime import datetime
from logging import error
import locale

locale.setlocale(locale.LC_ALL, ('ru_RU','UTF-8'))

def string_to_datetime(s):
    if s=='exit':
        return sys.exit()
    try:    #18 ������� 2022 �. 7:58:29.002 ����
        return datetime.strptime(s,'%d %B %Y �. %H:%M:%S.%f ����')
    except:
        try: # 18.08.22 7:58:29.002
            return datetime.strptime(s,'%d.%m.%y %H:%M:%S.%f')
        except:
            try: #18 ������� 2022 7:58:29.002 
                return datetime.strptime(s,'%d %B %Y %H:%M:%S.%f')
            except ValueError as ve:
                print('������ ����� ������:', ve)
                print('���������� ���� �� ���� ��������:')
                print('"�� ����� ���� �. ��:��:��.���� ����" �������� "18 ������� 2022 �. 7:58:29.002 ����"')
                print('"��.��.�� ��:��:��.�����" �������� "18.08.22 7:58:29.002"')
                print('"�� ����� ���� ��:��:��.����" �������� "18 ������� 2022 7:58:29.002"')
                print()
                return ''