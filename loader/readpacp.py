# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import time
import os, sys
import datetime
import MySQLdb
from scapy.all import *

path = ''
table = ''
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

class Log():
    filter_packets_num = 0


cursor = db.cursor()
def print_list(l):
    for index, i in enumerate(l):
        print index,i

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
        for i in range(744):
            if i == 563:
                continue
            each = '0'*(5-len(str(i)))+str(i) + '.pcap'
            finished += 1
            print('[loader] Inserting......' + each + ' in table '+ table_name)
            file_path = os.path.abspath(os.path.join(file_or_directory,'result',each))
            insert_single_file(file_path,Log)
            print '[loader] {}/{} finished at '.format(finished, total), datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        print '[Filter] Filtered '+str(Log.filter_packets_num)+' packets'
    else:
        print 'File or directory is not correct!!!'

if __name__ == '__main__':
    print('[Begining] Starting read files')
    insert_packets(file_or_directory=path,
                   table_name=table,
                   delete=True)