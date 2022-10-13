# coding: cp1251
import datetime
from datetime import datetime
import csv
from stringToDatetime import string_to_datetime
import locale

last_id_of_SCV_file='10800' # Указывает на конечный id записи для сравнения с первым в случае перезаписи 
locale.setlocale(locale.LC_ALL, ('ru_RU','UTF-8'))
filename = "786442_Ribbon1 Сводная.csv"

        

def body(time_start, time_stop, ap):
    start = datetime.today() #Начало работы алгоритма
    with open (filename,"r",encoding = 'cp1251') as f:
        reader = csv.DictReader(f, delimiter = ';')
        first_row = next(reader)
        previous_row = first_row.copy()
        with open ("result.csv","w",encoding = 'cp1251') as f:
            writer = csv.DictWriter(f,fieldnames=reader.fieldnames,delimiter=';')
            writer.writeheader()
            for row in reader:
                date=string_to_datetime(row["Дата и время записи"])
                if time_start<date and date<time_stop:
                    for i in row :
                        row[i]=row[i].replace(',','.')  
                        if (i!='RecordID') and (i!='Дата и время записи'):  #Пропускаем первые два столбца
                            if abs(float(row[i])-float(previous_row[i].replace(',','.')))>=ap:
                                # print('Строка с ID',row['RecordID'],'отличается')
                                # print('Параметр с отличием',i)
                                writer.writerow(row)
                                break
                    if row['RecordID']==last_id_of_SCV_file:
                        for i in row:
                            if (i!='RecordID') and (i!='Дата и время записи'):  #Пропускаем первые два столбца
                                if abs(float(row[i])-float(first_row[i].replace(',','.')))>=ap:
                                    # print('Строка с ID',row['RecordID'],'отличается')
                                    # print('Параметр с отличием',i)
                                    writer.writerow(first_row)
                                    break
                previous_row=row.copy()
    print ('Время выполнения программы:',datetime.today()-start)
    print()
