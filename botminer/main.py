# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import random
import sys
import os
from botminer.cluster.clusteringFinal.meanshift import run_cluster
from botminer.cluster.clusteringFinal.tkmeans import run_kmeans
from botminer.cluster.clusteringFinal.AffinityPropagation import affinityPropagation

from cluster.analys_cluster_result import analys,analys_oddball
from cluster.cross import cross_cluster
from lib.calc import scale_cflow
from lib.common import split_cflow, split_flow, save
from lib.data import cpanel
from lib.database import save_calc_results, read_packets, show_database_status
from lib.option import init_options
from script.fetch import run_fetchdata
from util.help import helpmsg
from util import view

def main():
    if '--calc' in sys.argv:
        if len(sys.argv) != 4:
            print "[*]Useage: python main.py group_id clusterFileName"
            exit()
        else:
            cross_cluster(sys.argv[1], sys.argv[2])
            exit()
    if '--status' in sys.argv:
        init_options()
        show_database_status()
        exit()

    if len(sys.argv) < 3 or '-h' in sys.argv:
        helpmsg()

    cpanel.group = sys.argv[1]

    init_options()
    read_packets(cpanel.group)
    split_flow()
    split_cflow()
    scale_cflow()

    if '--save' in sys.argv:
        save_calc_results()

    if '--outfile' in sys.argv:
        output_path = './output/results.txt'
        save(output_path)


def run():
    # init_options()
    # read_packets()
    # split_flow()
    # split_cflow()
    # scale_cflow()
    # save_calc_results()
    # run_fetchdata()
    # affinityPropagation(1,2)
    # run_kmeans(100)
    # analys(100)
    for i in range(1,11):
        print '-'*100
        print 'cluster number is: ',100+i*50
        run_kmeans(100+i*50)
        analys(100+i*50)
    # run_cluster() #聚类cflow
    # cross_cluster(cpanel.group, cluster_result_file='result/msresult.csv')
    # view.show_score()# 画图展示得分的分布
    # view.show_outline_score_scatter()


#以图的分析为主的话，那么拿到各个疑似是c&c服务器的IP，取到与之相连的各个可能是bot的IP，判断它们在聚类是否能聚到一起，如果能
#聚到一起，说明这些主机既具有相同的交互模式，而且也在同一个egonet中，因此可认为是僵尸主机，未发动恶意攻击的主机。
import os

def cross():

    class OddBall(object):
        def __init__(self, ID):
            self.attrs = {}
            self.attrs['members'] = []
            self.attrs['ID'] = ID

        def __getitem__(self, item):
            return self.attrs[item]

        def __setitem__(self, key, value):
            self.attrs[key] = value

        def __str__(self):
            return str(self.attrs['ID']) +'------'+str(self.attrs['members'])

    def statistics_single_oddball(id, oddballlist):
        oddball = OddBall(id)
        with open('C:/Desktop/bot/graph/oddball/oddball/{}.nn1'.format(id), 'r') as f:
            for line in f:
                id1, id2, weight = line.split(' ')
                if int(id1) == id:
                    oddball['members'].append(id2)
                elif int(id2) == id:
                    oddball['members'].append(id1)
                else:
                    continue
            oddballlist.append(oddball)

    def statistics_oddball(oddballlist):
        for i in range(len(os.listdir('C:/Desktop/bot/graph/oddball/oddball'))):
            statistics_single_oddball(i,oddballlist)

    def get_top1000_oddball_id(ids):
        with open('C:/Desktop/bot/graph/oddball/finalscore.csv','r') as f:
            for index,line in enumerate(f):
                if index ==  1000:
                    return
                ids.append(line.split(',')[0])

    oddballlist = []
    top1000 = []
    statistics_oddball(oddballlist)
    get_top1000_oddball_id(top1000)
    top1000_oddball = [oddballlist[int(id)] for id in top1000]
    analys_oddball(top1000_oddball,'C:/Desktop/kmeans52_600.csv')


if __name__ == '__main__':
    run()
