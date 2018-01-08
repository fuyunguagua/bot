# -*- coding:utf-8 -*-
import re

#args1: ip set
#args2: statistic rank
def ip_statistic(ips, num):
    rep_dic = {1:'(\d*).\d*.\d*.\d', 2:'(\d*.\d*).\d*.\d', 3:'(\d*.\d*.\d*).\d', 4:'\d*.\d*.\d*.\d'}
    suffix_dic = {1:'.x.x.x', 2:'.x.x', 3:'.x', 4:''}
    if num > 4 or num < 1:
        raise Exception('num is not correct')
    suffix = suffix_dic[num]
    rep = rep_dic[num]
    statistics = {}
    for ip in ips:
        if isinstance(ip,str):
            prefix = re.findall(rep,ip)[0]
            ip_key = prefix + suffix
            if not statistics.has_key(ip_key):
                statistics[ip_key] = 1
            else:
                statistics[ip_key] += 1
    return statistics