import MySQLdb

ip_dict = {}
def printdict(d):
    for key in d:
        print key,'-----',d[key]

def init_ip_dict(botnet_ip_path,first_ip):
    ip_base = first_ip.split('.')[-1]
    ip_model = first_ip.replace(ip_base,'{}')
    ip_dict = {}
    with open(botnet_ip_path,'r') as f :
        for index,line in enumerate(f):
            ip = line[0:-1]
            ip_dict[ip_model.format(index+ip_base)] = ip
        return ip_dict

def quote(s):
    return "'%s'" % s

def execute_replace(table,ip_dict):

    db = MySQLdb.connect(host='', user='', passwd='', db='')
    cursor = db.cursor()

    replace_src_sql = "update {} set IP_SRC ={} where ISBOT = 1 AND IP_SRC = {}"
    replace_dst_sql = "update {} set IP_DST ={} where ISBOT = 1 AND IP_DST = {}"
    for ip in ip_dict:
        sql = replace_src_sql.format(table,quote(ip_dict[ip]),quote(ip))
        cursor.execute(sql)
    for ip in ip_dict:
        sql = replace_dst_sql.format(table,quote(ip_dict[ip]),quote(ip))
        cursor.execute(sql)
