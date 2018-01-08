# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import MySQLdb


class DB:
    HOST = '10.0.0.2'
    USER = 'root'
    PASS = 'abcd1234'
    NAME = 'BOTDATA'

db = MySQLdb.connect(DB.HOST, DB.USER, DB.PASS, DB.NAME)

