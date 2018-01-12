import os
import csv
from graph.botnet import botnet_list

def analys(num):
    os.chdir(os.path.abspath('.'))
    for botnet in botnet_list:
        botnet['bots_id'] = []
        with open("C:/Desktop/ip.csv") as f:

            reader = csv.reader(f)
            for row_index,row in enumerate(reader):
                if row[0] in botnet['bots'] and row[1] == botnet['CNC']:
                    botnet['bots_id'].append(row_index)
        print len(botnet['bots_id'])
        botnet['row_record'] = {}

    ipnum = []

    # with open('C:/Desktop/bot/botminer/result/kmeans_result41{}.csv'.format(num)) as f:
    with open('C:/Desktop/kmeans52_{}.csv'.format(num)) as f:
        reader = csv.reader(f)
        for row_index,row in enumerate(reader):
            ipnum.append(len(row))
            for bot_index, botnet in enumerate(botnet_list):
                botnet['row_record'][row_index] = set()
                for id in row:
                    if int(id) in botnet['bots_id']:
                        botnet['row_record'][row_index].add(id)

    print '\t'.join(['Name','row_index','count'])
    print
    for botnet in botnet_list:
        max = 0
        pointer = 0
        for key in botnet['row_record']:
            if len(botnet['row_record'][key]) > max:
                max = len(botnet['row_record'][key])
                pointer = key
        print botnet['NAME'],'\t', pointer+1, '\t', max,'/',ipnum[pointer],'/',len(botnet['bots'])
        # print botnet['cnc_row_record'],'\t',sum(botnet['cnc_row_record'])

def analys_oddball(top1000_oddball,clusterfile):
    ip_map = {}
    with open('C:/Desktop/bot/graph/oddball/ip_map.csv') as f:
        for line in f:
            id = int(line[0:-1].split(' ')[0])
            ip = line[0:-1].split(' ')[1]
            ip_map[id] = ip

    for oddball in top1000_oddball:
        oddball['row_record'] = {}
        oddball['membersip'] = [ip_map[int(id)] for id in oddball['members']]

    ipnum = []
    with open(clusterfile) as f:
        reader = csv.reader(f)
        for row_index,row in enumerate(reader):
            ipnum.append(len(row))
            for oddball_index, oddball in enumerate(top1000_oddball):
                oddball['row_record'][row_index] = set()
                for ip in row:
                    if ip in oddball['membersip']:
                        oddball['row_record'][row_index].add(ip)

    for oddball_index,oddball in enumerate(top1000_oddball):
        max = 0
        pointer = 0
        for key in oddball['row_record']:
            if len(set(oddball['row_record'][key])) > max:
                max = len(set(oddball['row_record'][key]))
                pointer = key
        # with open('aa.txt','a') as f:
        #     f.write(str(oddball['ID'])+'\t'+str(pointer+1)+'\t'+str(max)+'/'+str(ipnum[pointer])+'/'+str(len(oddball['members']))+'\n')
        if float(max) / len(oddball['members']) == 1.0 and float(max) / ipnum[pointer] >= 0.5:
            print oddball['ID'], '\t',pointer+1, '\t', max,'/',ipnum[pointer],'/',len(oddball['members'])

if __name__ == '__main__':

    analys(600)
