import MySQLdb


conf = {}
conf['host'] = '172.28.5.0'
conf['user'] = 'root'
conf['passwd'] = 'abcd1234'
conf['db'] = 'botdata'
conf['db2'] = 'botdata'


def quote(s):
    return "'%s'" % s

def run():
    db = MySQLdb.connect(host=conf['host'], user=conf['user'], passwd=conf['passwd'], db=conf['db'])
    db2 = MySQLdb.connect(host=conf['host'], user=conf['user'], passwd=conf['passwd'], db=conf['db2'])
    cursor = db.cursor()
    cursor2 = db2.cursor()
    src_sql = "select TIMESTAMP,LENGTH,IP_SRC,IP_DST,PORT_SRC,PORT_DST,FLAG,ISBOT from common'"
    insert = 'insert into packets(TIMESTAMP,LENGTH,IP_SRC,IP_DST,PORT_SRC,PORT_DST,FLAG,ISBOT) VALUES ({},{},{},{},{},{},{},{})'

    cursor.execute(src_sql)
    result = cursor.fetchall()
    for index in range(len(result)):
        row = result[index]
        insert_sql = insert.format(quote(row[0]),row[1],quote(row[2]),quote(row[3]),row[4],row[5],quote(row[6]),row[7])
        cursor2.execute(insert_sql)
    db2.commit()

def a():
    db = MySQLdb.connect(host=conf['host'], user=conf['user'], passwd=conf['passwd'], db=conf['db'])
    cursor = db.cursor()
    sql_ip = "insert into temp(id) VALUES ({})"
    with open('iptop1in10.csv') as f:
        for line in f:
            ip = line[0:-1]
            cursor.execute(sql_ip.format(quote(ip)))
    db.commit()

if __name__ == '__main__':
    a()
