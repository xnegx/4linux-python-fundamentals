#!usr/bin/python 
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 20:03:59 2017
@author: Everton
"""

from datetime import datetime,timedelta

print datetime.now()
print datetime.now().strftime ('%H - %I - %s')
print datetime(1990,8,1,0,0,0)
print datetime(1990,8,1,0,0,0).strftime('%d/%b/%Y')

print datetime.now() + timedelta(
        days=4,
        seconds=123,
        milliseconds=123,
        minutes=21,
        hours=4,
        weeks=1         
)
