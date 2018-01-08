import MySQLdb


class DB:
    HOST = 'localhost'
    USER = 'root'
    PASS = 'abcd1234'
    NAME = 'botdata'

db = MySQLdb.connect(DB.HOST, DB.USER, DB.PASS, DB.NAME)


sql1 = '''select a.ip_src,a.ip_dst,a.port_dst,a.duration,a.px,a.nsp,a.psp,a.tbt,a.apl,a.pv,a.bps,a.pps,a.tbp,b.length as fps 
	from(
		select 
			ip_src,
			ip_dst,
			port_dst,
			max(timestamp)-min(timestamp) as duration,
			count(1) as px,
			sum(case when length >=40 and length<=400 then 1 else 0 end) as nsp, 
			sum(case when length >=40 and length<=400 then 1 else 0 end)/count(1) as psp ,
			sum(length) as tbt,
			avg(length) as apl,
			stddev(length)as pv,
			sum(length)/(max(timestamp)-min(timestamp))as bps,
			count(1)/(max(timestamp)-min(timestamp))as pps,
			(max(timestamp)-min(timestamp))/count(1) as tbp,
			min(timestamp)as mints 
		from newpackets  
		group by ip_src,ip_dst,port_dst
		)a 
	left join 
		newpackets b on a.mints=b.timestamp and a.ip_src=b.ip_src and a.ip_dst=b.ip_dst and a.port_dst=b.port_dst  
	group by a.ip_src,a.ip_dst,a.port_dst'''

sql2 = '''select tb1.ip_src,tb1.ip_dst,tb1.port_dst,count(tb1.number) as dps 
from (
	select ip_src,ip_dst,port_dst,length,count(1) as number 
	from newpackets 
	group by ip_src,ip_dst,port_dst,length
	)tb1 
group by tb1.ip_src,tb1.ip_dst,tb1.port_dst'''


sql3 = '''select ip_src,count(1) as fph 
from (
	select ip_src,ip_dst,port_src,port_dst,count(1) as px 
	from newpackets 
	group by ip_src,ip_dst,port_src,port_dst
	)t1 group by ip_src; '''

cursor = db.cursor()
cursor.execute(sql1)
db.commit()

cursor.execute(sql2)
db.commit()

cursor.execute(sql3)
db.commit()
