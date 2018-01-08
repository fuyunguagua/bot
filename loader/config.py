# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import MySQLdb
import re

class DB:
    HOST = 'localhost'
    USER = 'root'
    PASS = 'abcd1234'
    NAME = 'botdata'

f = open('all_ip.txt','r')
exp = '((?:\d{1,3}\.){3}\d{1,3})'
result = re.findall(exp,f.read())
IP_SET = result
f.close()

db = MySQLdb.connect(DB.HOST, DB.USER, DB.PASS, DB.NAME)

# class SETTING:
#     PCAP_SIZE = 10  # cut into small files (10M)
