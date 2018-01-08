# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import MySQLdb


class DB:
    HOST = '10.0.0.2'
    USER = 'root'
    PASS = 'abcd123466666666'
    NAME = 'BOTDATA'

db = MySQLdb.connect(DB.HOST, DB.USER, DB.PASS, DB.NAME)

