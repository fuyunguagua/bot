import  MySQLdb
import csv
import gc
class DB:
    HOST = '172.28.5.0'
    USER = 'root'
    PASS = 'abcd1234'
    NAME = 'botdata'

db = MySQLdb.connect(DB.HOST, DB.USER, DB.PASS, DB.NAME)
def record(ip_src,ip_dst,rdict):
    '''
    rdist      (a,b)---num
    :param ip_src:
    :param ip_dst:
    :param rdist:
    :return:
    '''
    newkey = (ip_src,ip_dst)
    for key in rdict:
        if ip_src in key and ip_dst in key:
            rdict[key] += 1
            return
    rdict[newkey] = 1

def dump(rdict,ip_list):
    ip_map = {}
    for index,ip in enumerate(ip_list):
        ip_map[ip] = index

    with open('ip_map.csv', 'wb') as f:
        writer = csv.writer(f)
        for key in ip_map:
            writer.writerow([key,ip_map[key]])

    with open('oddball-edges.csv', 'wb') as f:
        writer = csv.writer(f)
        for key in rdict:
            writer.writerow([ip_map[key[0]], ip_map[key[1]], rdict[key]])

def run():
    sqls = []
    sql1 = "select IP_SRC,IP_DST from athena limit 100000000"
    sql2 = "select IP_SRC,IP_DST from athena limit 100000000,200000000"
    sql3 = "select IP_SRC,IP_DST from athena limit 200000000,300000000"
    sql4 = "select IP_SRC,IP_DST from athena limit 300000000,400000000"
    sql5 = "select IP_SRC,IP_DST from athena limit 400000000,-1"
    sqls.append(sql1)
    sqls.append(sql2)
    sqls.append(sql3)
    sqls.append(sql4)
    sqls.append(sql5)
    ip_list = []
    rdict = {}
    cursor = db.cursor()
    for sql in sqls:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            if row[0] not in ip_list:
                ip_list.append(row[0])
            if row[1] not in ip_list:
                ip_list.append(row[1])
            record(row[0],row[1],rdict)
        del result
        gc.collect()
    sum = 0
    for va in rdict.values():
        sum += va
    print sum
    dump(rdict,ip_list)
def f():
    ip_list = []
    rdict = {}
    def record(ip_src,ip_dst,num):
        newkey = (ip_src, ip_dst)
        rdict[newkey] = num
    with open('result.txt','r') as f:
        for line in f:
            row = line.split('\t')
            if row[0] not in ip_list:
                ip_list.append(row[0])
            if row[1] not in ip_list:
                ip_list.append(row[1])
            record(row[0], row[1], row[2])
    dump(rdict,ip_list)
if __name__ == '__main__':
    f()