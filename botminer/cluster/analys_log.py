#  -*- coding: utf-8 -*-
import re
import os
from botminer.util.picture import drawBar
from botminer.util.ip_statistic import ip_statistic
os.chdir('../log/')

def analys():
    files = os.listdir('../log/')
    os.chdir('../log/')
    co = re.compile('Time:.*?event.*?0\n(.*?) ->.*?Port/Proto Range',re.S)
    ips = set()
    print '[log-ip-analyze] Starting analyzing scan log'
    print '\n\n\n\n'
    for file in files:
        with open(file, 'r') as f:
            content = f.read()
            a = co.findall(content)
        ips = ips.union(set(a))
        statistics = {}
        for ip in a:
            if not statistics.has_key(ip):
                statistics[ip] = 1
            else:
                statistics[ip] += 1
        print '*'*100
        for i in statistics.items():
            print i
    ip_distribution_statistics = ip_statistic(ips, 1)
    print '-'*40+'statistics'+'-'*40
    print 'ip amount:',len(ips)
    print  '***distribution***'
    for key in ip_distribution_statistics:
        print key,'---------'+ str(ip_distribution_statistics.get(key))
    #drawBar(statistics)
    #drawPie(statistics)
    with open('../result/scan_log_analys_result','wb') as f:
        for i in ips:
            f.write(i)
            f.write(os.linesep)



