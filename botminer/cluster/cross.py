# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from botminer.lib.database import fetch_apanel_results
import sys
import os
import csv
class C:
    def __init__(self, id):
        self.id = int(id)
        self.host = set()

    def add_host(self, host):
        if host not in self.host:
            self.host.add(host)

    def __len__(self):
        return len(self.host)


class A:
    def __init__(self, id, weight, type):  # 4 types available, weight >= 1
        self.id = int(id)
        self.weight = float(weight)
        self.host = set()
        self.type = type

    def add_host(self, host):
        if host not in self.host:
            self.host.add(host)

    def __len__(self):
        return len(self.host)


def cal_botscore(ip, As, Cs):
    """
    计算某个IP的僵尸得分

    ip 指定目标IP
    As 全部A-panel聚类结果
    Cs 全部C-panel聚类结果
    """

    def calc1(Ai, Aj):
        return Ai.weight * Aj.weight * (float(len(Ai.host.intersection(Aj.host))) / len(Ai.host.union(Aj.host)))

    def calc2(Ai, Ck):
    	#print len(Ai.host.intersection(Ck.host)),' ',len(Ai.host.union(Ck.host))
        return Ai.weight * (float(len(Ai.host.intersection(Ck.host))) / len(Ai.host.union(Ck.host)))

    A_list = get_list_by_host(ip, As)
    C_list = get_list_by_host(ip, Cs)


    score = 0
    for i in range(len(A_list)):
        for j in range(len(A_list)):
            if j > i and A_list[i].type != A_list[j].type:
                score += calc1(A_list[i], A_list[j])
    for A in A_list:
        for C in C_list:
            score += calc2(A, C)

    return score


def get_list_by_host(host_id, As):
    """
    A(h) = {Ai}i=1...m

    the set of A-clusters that contain h,
    """
    res = []
    for A in As:
        if host_id in A.host:
            res.append(A)
    return res


# 混合计算的主入口
def cross_cluster(group_id, cluster_result_file):
    print '[cross_cluster] starting calc bot score'
    all_bot_ips = set()
    As = []  # 全部A的聚类结果


    As.append(A(id=1, weight=1.0, type='scan'))
    #此文件包含所有具有扫描行为的主机ip
    with open('result/scan_log_analys_result','rb') as f:
        for ip in f:    # 第一类
            ip = ip.strip('\r\n')
            As[0].add_host(ip)
            all_bot_ips.add(ip)


    #此文件包含所有二进制下载的主机ip
    As.append(A(id=1, weight=1.0, type='other'))
    with open('result/download_log_analys_result','rb') as f:
        for ip in f:    # 第一类
            ip = ip.strip('\r\n')
            As[1].add_host(ip)
            all_bot_ips.add(ip)



    # TODO 将聚类后的结果导入Cs
    # TODO 修改后将本函数加入到程序的主流程之中
    Cs = []
    csfile = open(cluster_result_file, "r")
    cs = csfile.read().split("\n")
    count = 0
    for c in cs:
        c = c.split(",")
        tmpc = C(count)
        for i in c:
            tmpc.add_host(i)
        Cs.append(tmpc)
        count += 1
    # 对所有被A-panel收录的IP计算僵尸得分
    scores = []
    print '#'*100
    for ip in all_bot_ips:
        score = cal_botscore(ip, As, Cs)
        rows = str(ip) + '------------' + str(score)
        print rows
        scorekv = []
        scorekv.append(ip)
        scorekv.append(score)
        scores.append(scorekv)
    with open('result/score.csv', 'wb') as f:      # 采用b的方式处理可以省去很多问题
        writer = csv.writer(f)
        writer.writerows(scores)
