# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import Birch
import sys
sys.path.append("..")
from lib.option import DB




def run_fetchdata():
    print '[fetch c_flow] starting dump cflow to file'
    cflows = get_cflow_data()
    ip_src = []
    f = open("result/tmp.csv","w+")
    ip = open("result/ip.csv","w+")
    for i in xrange(len(cflows)):
        f.write(cflows[i][6] + ',' + cflows[i][7] + ',' + cflows[i][8] + ',' + cflows[i][9] + "\n")#每个ip的39维数据
        ip.write(cflows[i][1]+','+cflows[i][2]+"\n")#记录ip
    f.close()
    ip.close()
    # ip = open("result/ip.csv" ,"r")
    # ip_src = ip.read().split("\n")[:-1]
    # ip.close()

def get_cflow_data():
    """
    Fetch all cflow data from database
    """
    import MySQLdb
    db = MySQLdb.connect(DB.HOST, DB.USER, DB.PASS, DB.NAME)
    cursor = db.cursor()
    sql = "select * from Cflow5 order by id"
    cflows = cursor.fetchmany(cursor.execute(sql))
    print "[database] cflows: {}".format(len(cflows))
    return cflows