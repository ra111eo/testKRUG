# coding: cp1251
from stringToDatetime import string_to_datetime
from mainLogic import body

start_point = string_to_datetime('18 августа 2022 7:58:26.0')
stop_point =  string_to_datetime('18 августа 2022 7:58:30.0')
aperture = 1
body(start_point,stop_point,aperture)