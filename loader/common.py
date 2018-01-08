# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import time
import os, sys
import datetime
from scapy.all import *
from config import db,IP_SET


class Log():
    filter_packets_num = 0


cursor = db.cursor()
def print_list(l):
    for index, i in enumerate(l):
        print index,i
def init_database():
    cursor = db.cursor()
    #cursor.execute("create database if not exists BOT;")
    db.select_db("BOT")
    sql = """CREATE TABLE DataGroup(
             ID INT NOT NULL AUTO_INCREMENT,
             UPLOAD_TIME CHAR(10),
             UPLOAD_NAME CHAR(20),
             START_TIME  FLOAT,
             PRIMARY KEY (ID))
             """

    cursor.execute(sql)
    sql = """CREATE TABLE  Packets(
             ID INT NOT NULL AUTO_INCREMENT,
             GROUP_ID INT NOT NULL,
             TIMESTAMP  VARCHAR(15) NOT NULL,
             LENGTH INT NOT NULL,
             IP_SRC CHAR(15) NOT NULL,
             IP_DST CHAR(15) NOT NULL,
             PORT_SRC INT NOT NULL,
             PORT_DST INT NOT NULL,
             FLAG CHAR(5),
             PRIMARY KEY (ID),
             foreign key(GROUP_ID) references DataGroup(ID)
             )"""
    cursor.execute(sql)
    sql = """CREATE TABLE  Cflow(
             ID INT NOT NULL AUTO_INCREMENT,
             GROUP_ID INT NOT NULL,
             IP_SRC VARCHAR(20),
             IP_DST VARCHAR(20),
             PORT_SRC INT,
             PORT_DST INT,
             FLOWS INT NOT NULL,
             FPH_13 VARCHAR (100) NOT NULL,
             PPF_13 VARCHAR (100) NOT NULL,
             BPP_13 VARCHAR (100) NOT NULL,
             BPS_13 VARCHAR (100) NOT NULL,
             NOTE CHAR (100),
             PRIMARY KEY (ID),
             foreign key(GROUP_ID) references DataGroup(ID)
             )"""
    cursor.execute(sql)

    # sql = """CREATE TABLE  Mirai(
    #          ID INT NOT NULL AUTO_INCREMENT,
    #          GROUP_ID INT NOT NULL,
    #          IP_SRC VARCHAR(20),
    #          IP_DST VARCHAR(20),
    #          PORT_SRC INT,
    #          PORT_DST INT,
    #          PRIMARY KEY (ID)
    #          )"""
    # cursor.execute(sql)
    # sql = "ALTER TABLE Mirai ADD UNIQUE ( IP_SRC )"
    # cursor.execute(sql)
    # sql = """CREATE TABLE  Ares(
    #          ID INT NOT NULL AUTO_INCREMENT,
    #          GROUP_ID INT NOT NULL,
    #          IP_SRC VARCHAR(20),
    #          IP_DST VARCHAR(20),
    #          PORT_SRC INT,
    #          PORT_DST INT,
    #          PRIMARY KEY (ID)
    #          )"""
    # cursor.execute(sql)
    # sql = "ALTER TABLE Ares ADD UNIQUE ( IP_SRC )"
    # cursor.execute(sql)
    db.commit()

def statistics_file(path):
    name_set = []
    for file in os.listdir(path):
        name_suffix = file.split('_')[0]
        name_set.append(int(name_suffix))
        name_set = sorted(name_set,reverse=False)
    return name_set
def insert_packets(file_or_directory = '.', table_name = '',delete=False):

    def insert_single_file(filename,Log):
        pcap = rdpcap(filename)[TCP]
        for i in xrange(len(pcap)):
            length = len(pcap[i])
            #过滤白名单
            try:
                timestamp = "%.6f" % pcap[i].time
                ip_src = str(pcap[i]['IP'].src)
                ip_dst = str(pcap[i]['IP'].dst)
                port_src = int(pcap[i]['IP'].sport)
                port_dst = int(pcap[i]['IP'].dport)
                if ip_dst in IP_SET or ip_src in IP_SET:
                    Log.filter_packets_num += 1
                    continue
            except:
                continue
            """
            <Ether  dst=00:23:89:3a:8b:08 src=00:0e:c6:c2:5f:d8 type=0x800 |<IP  version=4L ihl=5L tos=0x0 len=40 id=34019 flags=DF frag=0L ttl=64 proto=tcp chksum=0x9920 src=172.29.90.176 dst=42.156.235.98 options=[] |<TCP  sport=47571 dport=https seq=3681001345 ack=1822908669 dataofs=5L reserved=0L flags=A window=65280 chksum=0x1ce7 urgptr=0 |>>>
            """
            if bin(pcap[i][TCP].flags)[-1] == '1':
                flag = 'Fin'
            elif bin(pcap[i][TCP].flags)[-2] == '1':

                flag = 'Syn'
            else:
                flag = ''

            sql = "INSERT INTO {}(`TIMESTAMP`,`LENGTH`,`IP_SRC`,`IP_DST`,`PORT_SRC`,`PORT_DST`,`FLAG`)" \
                  "VALUES({},{},{},{},{},{},{})".\
                format(table_name,'"'+str(timestamp)+'"',length,'"'+ip_src+'"','"'+ip_dst+'"',port_src,port_dst,'"'+flag+'"')
            cursor.execute(sql)
            db.commit()

        if delete:
            os.remove(filename)

    if os.path.isfile(file_or_directory):
        print('[loader] Inserting......'+ file_or_directory)
        insert_single_file(filename = file_or_directory)
    elif os.path.isdir(file_or_directory):
        files = os.listdir(os.path.join(file_or_directory,'result'))
        total = len(files)
        print '[loader] Total pcap files: {}'.format(total)
        print '[loader] Inserting at ', datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        finished = 0
        for i in sorted(set(statistics_file(os.path.join(file_or_directory,'result')))):
            for j in range(10):
                each = '0'*(5-len(str(i)))+str(i) + '_'+'0'*(5-len(str(j))) + str(j) + '.pcap'
                finished += 1
                print('[loader] Inserting......' + each + ' in table '+ table_name)
                file_path = os.path.abspath(os.path.join(file_or_directory,'result',each))
                # print file_path
                insert_single_file(file_path,Log)
                print '[loader] {}/{} finished at '.format(finished, total), datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        print '[Filter] Filtered '+str(Log.filter_packets_num)+' packets'
    else:
        print 'File or directory is not correct!!!'

