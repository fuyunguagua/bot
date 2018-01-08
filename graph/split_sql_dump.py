# -*- coding:utf-8 -*-
from multiprocessing import Pool
import re
import csv
import datetime
import time
import os

class Log(object):
    total = 0
    @staticmethod
    def start(total):
        Log.total = total
        print '[statistics] Total files: {}'.format(total)
        print '[statistics] Program starting at ', datetime.datetime.fromtimestamp(time.time()).strftime(
            '%Y-%m-%d %H:%M:%S')
    @staticmethod
    def finished_one(index):
        print '[statistics] {}/{} finished at '.format(index, Log.total), datetime.datetime.fromtimestamp(time.time()).strftime(
            '%Y-%m-%d %H:%M:%S')

def record(ip_src, ip_dst, rdict):
    for key in rdict:
        if ip_src in key and ip_dst in key:
            rdict[key] += 1
            return
    newkey = (ip_src,ip_dst)
    rdict[newkey] = 1

def dump(rdict,ip_list,path):
    ip_map = {}
    with open(os.path.join(path, 'ip_map.csv'), 'wb') as f:
        for index,ip in enumerate(ip_list):
            ip_map[ip] = index
            writer = csv.writer(f, delimiter=' ')
            writer.writerow([index,ip])

    with open(os.path.join(path,'oddball-edges.csv'), 'wb') as f:
        writer = csv.writer(f,delimiter = ' ')
        for item in rdict:
            writer.writerow([ip_map[item[0]], ip_map[item[1]], rdict[item]])

#process results
def summarize(path):
    files = os.listdir(path)
    abs_path = os.path.abspath(path)
    if not os.path.exists(os.path.join(abs_path, 'result')):
        os.mkdir(os.path.join(abs_path, 'result'))

    ip_list = []
    rdict = {}
    sumaaa = 0
    def record_inter(ip_src,ip_dst,num):
        newkey = (ip_src, ip_dst)
        for key in rdict:
            if ip_src in key and ip_dst in key:
                rdict[key] += num
                return
        rdict[newkey] = num

    total = len(files)
    Log.start(total)
    finished = 0
    for file in files:
        finished += 1
        with open(os.path.join(path, file), 'r') as f:
            for line in f:
                row = line.split('\t')
                if row[0] not in ip_list:
                    ip_list.append(row[0])
                if row[1] not in ip_list:
                    ip_list.append(row[1])
                record_inter(row[0], row[1], int(row[2][0:-1]))
        Log.finished_one(finished)
    for value in rdict.values():
        sumaaa += value
    print sumaaa
    # dump2(rdict, os.path.join(abs_path, 'result'), 'result.csv')
    dump(rdict, ip_list, os.path.join(abs_path,'result'))

def dump2(rdict,path,file):
    with open(os.path.join(path,file), 'wb') as f:
        writer = csv.writer(f,delimiter = '\t')
        for key in rdict:
            writer.writerow([key[0], key[1], rdict[key]])

def statistic_sql_file(path):
    def process_one(file):
        ip_re = '(?:\d{1,3}\.){3}\d{1,3}'
        with open(os.path.join(path,file)) as f:
            map_dict = {}
            for line in f:
                ips = re.findall(ip_re,line)
                ip_src = ips[0]
                ip_dst = ips[1]
                record(ip_src,ip_dst,map_dict)
            dump2(map_dict,os.path.join(abs_path,'result'),file)

    files = os.listdir(path)
    abs_path = os.path.abspath(path)
    if not os.path.exists(os.path.join(abs_path, 'result')):
        os.mkdir(os.path.join(abs_path, 'result'))
    total = len(files)

    Log.start(total)
    finished = 0
    for file in files:
        if os.path.isdir(os.path.join(abs_path,file)):
            continue
        process_one(file)
        finished += 1
        Log.finished_one(finished)

#每10个文件放一个文件夹
def group(path):
    files = os.listdir(path)
    total = len(files)
    numofdir = total/10
    if total % 10 != 0:
        numofdir += 1
    dirname = ''
    for index,file in enumerate(files):
        if index % 10 == 0:
            dirname = os.path.join(path,str(index/10 + 1))
            os.system('powershell mkdir {}'.format(dirname))
        os.system('powershell mv {} {}'.format(os.path.join(path,file),dirname))

def long_time_task(dir):
    print('Run task %s (%s)...' % (dir, os.getpid()))
    start = time.time()
    summarize(dir)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (dir, (end - start)))

def run():
    path = 'C:/Desktop/acc'
    dirs =  os.listdir(path)
    print('Parent process %s.' % os.getpid())
    p = Pool(30)
    for i in range(len(dirs)):
        p.apply_async(long_time_task, args=(os.path.join(path,str(i+1)),))

    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

def check():
    files = os.listdir('/home/wangyang/data/h10/all')
    all = 0
    for file in files:
        if file.endswith('.csv'):
            sum = 0
            with open(file) as f:
                for line in f:
                    num = line[0:-1].split('\t')[-1]
                    sum += int(num)
                print f, '\t', sum
                all += sum
    print all

#怀疑字典拖慢速度，现改为元组
def summarize_list(path):
    files = os.listdir(path)
    abs_path = os.path.abspath(path)
    if not os.path.exists(os.path.join(abs_path, 'result')):
        os.mkdir(os.path.join(abs_path, 'result'))

    ip_list = []
    rlist = []# (ip1,ip2,num)
    sumaaa = 0
    def record_inter(ip_src,ip_dst,num):
        for item in rlist:
            if ip_src in item and ip_dst in item:
                item[2] += num
                return
        rlist.append([ip_src,ip_dst,num])

    total = len(files)
    Log.start(total)
    finished = 0
    for file in files:
        finished += 1
        with open(os.path.join(path, file), 'r') as f:
            for line in f:
                row = line.split('\t')
                if row[0] not in ip_list:
                    ip_list.append(row[0])
                if row[1] not in ip_list:
                    ip_list.append(row[1])
                record_inter(row[0], row[1], int(row[2][0:-1]))
        Log.finished_one(finished)
    for item in rlist:
        sumaaa += item[2]
    print sumaaa
    dump(rlist,ip_list,os.path.join(abs_path,'result'))

if __name__ == '__main__':
    # group()
    # run()
    summarize('C:/Desktop/final')
    # # statistic_sql_file(path)
    # path = 'C:/Desktop/acc'
    # 'cp 42/result/result.csv . && mv result.csv 42.csv'

