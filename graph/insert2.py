import MySQLdb
import os
import time
from multiprocessing import Pool

#guo lv graph de result from all packetw 


def run(file):
    conf = {}
    conf['host'] = '172.28.5.0'
    conf['user'] = 'root'
    conf['passwd'] = 'abcd1234'
    conf['db'] = 'botdata'
    ips = []
    with open('10_iptop1in10.csv') as f:
        for line in f:
            ip = line[0:-2]
            ips.append(ip)

    db = MySQLdb.connect(host=conf['host'], user=conf['user'], passwd=conf['passwd'], db=conf['db'])
    cursor = db.cursor()

    with open(file) as f:
        a = f.read()
        import re
        result = re.findall('\((.*?)\)',a,re.S)
        print len(result)
        b  = filter(lambda a:len(a.split(','))==9,result)
        print len(b)
        insert = 'insert into packetsfilted(TIMESTAMP,LENGTH,IP_SRC,IP_DST,PORT_SRC,PORT_DST,FLAG,ISBOT) VALUES ({},{},{},{},{},{},{},{})'
        for item in b:
            ss = item.split(',')
            [id,timestamp,length,ip_src,ip_dst,port_src,port_dst,flag,isbot] = ss

            if ip_src.strip("'") not in ips and ip_dst.strip("'") not in ips:
                continue

            sql_str = insert.format(timestamp,int(length),ip_src,ip_dst,port_src,port_dst,flag,int(isbot))
            cursor.execute(sql_str)
            db.commit()

def long_time_task(dir):
    print('Run task %s (%s)...' % (dir, os.getpid()))
    start = time.time()
    run(dir)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (dir, (end - start)))

if __name__ == '__main__':
    path = 'C:/Desktop/acc'
    files =  os.listdir(path)
    print('Parent process %s.' % os.getpid())
    p = Pool(30)
    for file in files:
        if file.endswith('sql'):
            p.apply_async(long_time_task, args=(os.path.join(path,file),))

    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')