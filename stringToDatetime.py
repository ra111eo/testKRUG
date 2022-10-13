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
    try:    #18 августа 2022 г. 7:58:29.002 мсек
        return datetime.strptime(s,'%d %B %Y г. %H:%M:%S.%f мсек')
    except:
        try: # 18.08.22 7:58:29.002
            return datetime.strptime(s,'%d.%m.%y %H:%M:%S.%f')
        except:
            try: #18 августа 2022 7:58:29.002 
                return datetime.strptime(s,'%d %B %Y %H:%M:%S.%f')
            except ValueError as ve:
                print('Ошибка ввода данных:', ve)
                print('Попробуйте один из этих форматов:')
                print('"ДД месяц ГГГГ г. ЧЧ:ММ:СС.МСЕК мсек" например "18 августа 2022 г. 7:58:29.002 мсек"')
                print('"ДД.ММ.ГГ ЧЧ:ММ:СС.МКСЕК" например "18.08.22 7:58:29.002"')
                print('"ДД месяц ГГГГ ЧЧ:ММ:СС.МСЕК" например "18 августа 2022 7:58:29.002"')
                print()
                return ''