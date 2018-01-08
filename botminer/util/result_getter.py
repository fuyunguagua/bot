import MySQLdb
from botminer.util.ip_statistic import ip_statistic
from botminer.lib.option import DB
import csv
import  os

def get_outline_scores():
    with open('result/finalscore.csv','rb') as f:
        reader = csv.reader(f)
        result = {item[0]:float(item[1]) for item in reader}
        result = filter(lambda item:item[1] < 100,result.items())
        return dict(result)

def get_bot_scores():
    with open('result/score.csv','rb') as f:
        reader = csv.reader(f)
        result = {item[0]:float(item[1]) for item in reader}
        return result

def get_scan_log_ip_statistic(rank):
    with open('result/scan_log_analys_result','rb') as f:
        ips = set()
        for ip in f:
            ip = ip.strip('\r\n')
            ips.add(ip)
        result = ip_statistic(ips,rank)
        return result

def get_packet_ip_statistic(rank):
    db = MySQLdb.connect(DB.HOST, DB.USER, DB.PASS, DB.NAME)
    cursor = db.cursor()
    sql = "select IP_SRC from packets where GROUP_ID={}".format(1)
    raw_packets = cursor.fetchmany(cursor.execute(sql))
    print '[database] Selected Packets: {}'.format(len(raw_packets))
    h = [i[0] for i in raw_packets]
    ip_set = set(h)
    result = ip_statistic(h, rank)
    return result
