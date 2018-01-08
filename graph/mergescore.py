# -*- coding:utf-8 -*-
from botnet import BotNet
import numpy as np
import os
import csv
p = {}
l = {}
s = {}
Mirai = BotNet(NAME='Mirai', CNC='120.76.125.235')
Ares = BotNet(NAME='Ares', CNC='162.219.125.220')
BlackEnergy = BotNet(NAME='BlackEnergy', CNC='104.224.140.235')
Zeus = BotNet(NAME='Zeus', CNC='23.83.234.122')
Athena = BotNet(NAME='Athena', CNC='45.62.122.120')
botnet_list = [Mirai, Ares, BlackEnergy, Zeus, Athena]

def init():

    with open('ip_map.csv') as f:
        for line in f:
            id =line[0:-1].split(',')[0]
            ip = line[0:-1].split(',')[1]
            for botnet in botnet_list:
                if botnet['CNC'] == ip:
                    botnet['ID'] = int(id)

    with open('oddball_16_9_scores_p') as f:
        for line in f:
            id = line.split(' ')[0]
            score = float(line.split(' ')[1][0:-1])
            p[id] = score

    with open('oddball_16_9_scores_l') as f:
        for line in f:
            id = line.split(' ')[0]
            score = float(line.split(' ')[1][0:-1])
            l[id] = score

    for key in p:
        s[key] = p[key] + l[key]

    #calculate botnet cv index
    for botnet in botnet_list:
        botnet['CV'] = cal_var_means(botnet['ID'])

def get_final_rank():
    rankp = []
    rankl = []
    newrank = []

    for item in sorted(p.iteritems(), key=lambda a: a[1], reverse=True):
        rankp.append(item[0])
    for item in sorted(l.iteritems(), key=lambda a: a[1], reverse=True):
        rankl.append(item[0])

    for i in range(len(rankp)):
        if rankp[i] not in newrank:
            newrank.append(rankp[i])
        if rankl[i] not in newrank:
            newrank.append(rankl[i])
    return newrank

def dump_sorted_result(l,filename):
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        for key in l:
            writer.writerow([key[0], key[1]])

def printdict(d):
    for index,key in enumerate(d):
        for item in botnet_list:
            if int(key[0]) == item['ID']:
                item['CV_RANK'] = index + 1
        if index > 10000:
            break
        print index+1,'\t',key[0],'\t',key[1]

# printdict(sorted(p.iteritems(),key = lambda a:a[1]))
def cal_var_means(id):
    with open('oddball/{}.nn1'.format(id),'r') as f:
        weights = []
        for line in f:
            id1,id2,weight = line.split(' ')
            if int(id1) == id or int(id2) == id:
                weights.append(float(weight))
        if len(weights) == 1:
            return 100
        var = np.var(weights)
        mean = np.mean(weights)
        return np.sqrt(var) / mean

#计算变异系数
def cal_cv():
    cvs = {}
    for i in range(len(os.listdir('oddball'))):
        cvs[i] = cal_var_means(i)
    return cvs


if __name__ == '__main__':
    init()

    cv_result = sorted(cal_cv().iteritems(),key = lambda a:a[1])
    dump_sorted_result(cv_result,'cv.csv')

    sum_result = sorted(s.iteritems(),key = lambda a:a[1])
    dump_sorted_result(sum_result,'sum.csv')