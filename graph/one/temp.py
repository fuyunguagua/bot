import MySQLdb


conf = {}
conf['host'] = '172.28.5.0'
conf['user'] = 'root'
conf['passwd'] = 'abcd1234'
conf['db'] = 'botdata'

ips = []
with open('iptop1in10.csv') as f:
    for line in f:
        ip = line[0:-2]
        ips.append(ip)

db = MySQLdb.connect(host=conf['host'], user=conf['user'], passwd=conf['passwd'], db=conf['db'])
cursor = db.cursor()

with open('C:/Desktop/ares.sql') as f:
    a = f.read()
    import re
    result = re.findall('\((.*?)\)',a,re.S)
    print len(result)
    b  = filter(lambda a:len(a.split(','))==9,result)
    print len(b)
    insert = 'insert into newpacketsfilted(TIMESTAMP,LENGTH,IP_SRC,IP_DST,PORT_SRC,PORT_DST,FLAG,ISBOT) VALUES ({},{},{},{},{},{},{},{})'
    for item in b:
        ss = item.split(',')
        [id,timestamp,length,ip_src,ip_dst,port_src,port_dst,flag,isbot] = ss

        if ip_src.strip("'") not in ips and ip_dst.strip("'") not in ips:
            continue

        sql_str = insert.format(timestamp,int(length),ip_src,ip_dst,port_src,port_dst,flag,int(isbot))
        cursor.execute(sql_str)
        db.commit()