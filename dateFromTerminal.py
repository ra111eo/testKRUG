# coding: cp1251
import sys
import argparse
from stringToDatetime import string_to_datetime
from mainLogic import body

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-d', '--dateStart', default='18.08.22')
    parser.add_argument ('-t', '--timeStart', default='00:00:00.0')
    parser.add_argument ('-D', '--DateStop', default='18.08.22')
    parser.add_argument ('-T', '--TimeStop', default='00:00:00.0')
    parser.add_argument ('-a','--aperture', default='0')
    return parser


parser = createParser()
params= parser.parse_args(sys.argv[1:])
start_pointer=string_to_datetime(params.dateStart + ' ' + params.timeStart)
stop_pointer=string_to_datetime(params.DateStop + ' ' + params.TimeStop)
body(start_pointer,stop_pointer,float(params.aperture))

