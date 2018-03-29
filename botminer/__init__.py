# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import numpy as np
import os
from matplotlib import pyplot as plt

def regular_occupy(result):
    for egonet_id in result:
        if 0 in result[egonet_id]:
            index = result[egonet_id].index(0)
            if index == 0:
                result[egonet_id]= [0 for i in range(len(result[egonet_id]))]
                continue

            if max(result[egonet_id][:index]) > 0.8:
                for i, item in enumerate(result[egonet_id]):
                    if i >= index:
                        result[egonet_id][i] = 2
            else:
                for i, item in enumerate(result[egonet_id]):
                    if i >= index:
                        result[egonet_id][i] = 0

def show(k,result):
    plt.xlabel('K')
    plt.ylabel('Occupancy')
    for egonet_id in result:
        if int(egonet_id) == 158900:
            plt.plot(k, result[egonet_id],'g-.')
        elif int(egonet_id) == 149648:
            plt.plot(k, result[egonet_id], 'r--')
        elif int(egonet_id) == 149936:
            plt.plot(k, result[egonet_id], 'o')
        elif int(egonet_id) == 149700:
            plt.plot(k, result[egonet_id], 'b-')
        else:
            plt.plot(k, result[egonet_id])
        plt.hold(True)
    # plt.legend()
    # red dashes, blue squares and green triangles
    # plt.plot(t, t, 'r--', t, t ** 2, 'bs',
    #          t, t ** 3, 'g^')
    plt.show()

def run():
    path = '/Users/wy/temp'
    result = {}
    k = [] #all k
    for file in os.listdir(path):
        k.append(int(file[4:file.find('.')]))
    k = sorted(k)
    for i in k:
        with open('/Users/wy/temp/lala{}.txt'.format(i), 'r') as f:
            for line in f:
                id = line.split(' ')[0]
                occupy = float(line.split(' ')[1])
                try:
                    result[id].append(occupy)
                except Exception:
                    result[id]=[]
                    result[id].append(occupy)

    regular_occupy(result)
    show(k,result)

def print_dict(d):
    ids = [158900,149648,149936,149700]
    for key in d:
        if int(key) in ids:
            for i in range(30,41):
                if d[key][i] < 0.8:
                    print key
                    break

if __name__ == '__main__':
    run()