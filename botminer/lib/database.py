# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import MySQLdb
import sys
from option import DB
from data import cpanel, conf
from model import Packet


def read_packets():
    """
    从数据库中读取Packets并实例化Hackers have been using the botnet to conduct a distributed denial-of-service attack on a target website, sending a large amount of spam, stealing large amounts of sensitive information within a short period of time, seizing system resources for illegal purposes and making profits, arousing the concern of domestic security companies. The academic community began to pay attention to the development of botnets in 2003. Some Honeynet teams and some members of the Honeynet Research Alliance use Honeynet Analytics to track and analyze botnet activity in depth, such as Bill McCarty at Azusa Pacific University, Richard Clarke at the French Honeynet Program, University Dave Dittrich and German honeynet project team. Some valid detection models have been proposed. For example, In [x], Guofei Gu et al. present a general detection framework that is independent of botnet C & C protocol and structure, and requires no a priori knowledge of botnets (such as captured bot binaries and hence the botnet signatures, and C & C server names / addresses).
However, as botnet protocols, structures, and attackers continue to evolve, many of the more powerful detection solutions fail to adapt to the new environment, reducing or even becoming ineffective, at a loss to highly concealed malicious behavior. For instant, Botminer can’t be able to effectively detect the 2016 IoT botnet Mirai.
In response to these circumstances, the academic community launched a new round of botnets in-depth study.
In 2010, [10] present a framework for passive tracking and identification of botnets based on analysis on three distinct but related levels(single packet analysis, network traffic analysis, TCP/IP traffic content analysis) to find more comprehensive tracking of bots.
In 2011, Wei Lu et al. address the issue that traffic content can be encrypted with the evolution of botnet and as a result leading to a fail of content based detection approaches In[X1].
In 2012, [6] propose a light-weight mechanism BotGAD to detect botnets using their fundamental characteristics, i.e., group activity.[8] propose a detection framework called BotGrab that is able to detect unknown botnets because it utilizes an unsupervised technique driven by intrinsic characteristics such as coordinated group activities（找到了内在特征）, without a priori knowledge of them.
In 2013, [9] propose event-driven log analysis software for users that lack knowledge about botnet analysis that enables detection of botnet activities and indicates whether the end-users machines have become a member of a botnet.[12][13]
In 2014, [X4] compares the output of three different botnet detection methods by executing them over a new, real, labeled and large botnet dataset which includes botnet, normal and background traffic.[11]
In 2015, anomaly score based botnet detection is proposed by [X3] to identify the botnet activities by using the similarity measurement and the periodic characteristics of botnets.
In 2016, David Zhao et al. propose a new approach in[X2] to detect botnet activity based on traffic behavior analysis by classifying network traffic behavior using machine learning. In [X5], G. Kirubavathi et al. propose a novel approach to detect botnets irrespective of their structures, based on network traffic flow behavior analysis and machine learning techniques. [7]

    """

    db = MySQLdb.connect(conf.DB.HOST, conf.DB.USER, conf.DB.PASS, conf.DB.NAME)
    cursor = db.cursor()

    sql = "select * from newpacketsfilted order by TIMESTAMP"
    raw_packets = cursor.fetchmany(cursor.execute(sql))
    print '[database] Selected Packets: {}'.format(len(raw_packets))

    cpanel.START_TIME = raw_packets[0][1]
    print '[common] START_TIME: %s' % str(cpanel.START_TIME)
    for p in raw_packets:
        cpanel.PACKETS.append(Packet(p))

    print '[common] Packets loading finished.'


def save_calc_results():
    """
    将CFLOW数据录入数据库，包含4个13维向量和其他CFlow特征
    """

    def quote(s):
        return "'%s'" % s

    print "[database] Saving cflow3 vectors into database."

    db = MySQLdb.connect(DB.HOST, DB.USER, DB.PASS, conf.DB.NAME)
    cursor = db.cursor()

    # add uesr-prompt before overwrite cflow data.
    # query = 'SELECT COUNT(*) FROM Cflow WHERE GROUP_ID={}'.format(cpanel.group)
    # cursor.execute(query)
    # result = cursor.fetchone()
    # if result[0]:
    #     msg = '[!] [database] Group {} already has {} results, wants to overwrite? [Y/n]'.format(cpanel.group,
    #                                                                                              int(result[0]))
    #     if raw_input(msg) in ['n', 'N', 'No', 'no']:
    #         sys.exit('System exit.')
    #     else:
    #         db.query('DELETE FROM Cflow WHERE GROUP_ID={}'.format(cpanel.group))
    #         # db.commit()

    for cflow in cpanel.C_FLOWS:
        query = """
            INSERT INTO cflow5(
             IP_SRC,
             IP_DST,
             PORT_DST,
             FLOWS,
             FPH_13,
             PPF_13,
             BPP_13,
             BPS_13)VALUES ({},{},{},{},{},{},{},{})
            """.format(
            quote(str(cflow.ip_src)),
            quote(str(cflow.ip_dst)),
            quote(str(cflow.port_dst)),
            quote(str(cflow.flow_count)),
            quote(','.join([str(i) for i in cflow.fph])),
            quote(','.join([str(i) for i in cflow.ppf])),
            quote(','.join([str(i) for i in cflow.bpp])),
            quote(','.join([str(i) for i in cflow.bps])),
        )
        cursor.execute(query)

    db.commit()

    query = 'SELECT COUNT(*) FROM cflow5'
    cursor.execute(query)
    result = cursor.fetchone()
    print "[database] Done, inserted items count: {}".format(int(result[0]))

    db.close()


def get_calc_results():  # TODO
    db = MySQLdb.connect(DB.HOST, DB.USER, DB.PASS)
    cursor = db.cursor()
    db.select_db("BOTNET")

    query = """

    """


def show_database_status():
    """
    查看当前数据库中的数据情况。

    DATABASE_STATUS

    GROUP_ID | UPLOAD_TIME | UPLOAD_NAME | START_TIME | PACKETS | CALC_CFLOW
    1	5.28.15.23	cdxy	1000.0	0	-
    2	5.28.15.23	cdxy	1000.0	54	7
    3	1111	cdxy-real-1	1000.0	26542	-
    5	1111	cdxy-real-1	1000.0	105329	-
    6	1111	cdxy-real-1	1000.0	171863	82
    7	111	    cdxy-real	1000.0	10207	-
    8	111	    cdxy-real	1000.0	62008	-
    9	111	    cdxy-real	1000.0	61997	-
    10	1	    cdxy-test	1000.0	61997	2678
    15	1	    cdxy-real	1000.0	5242606	32420

    """
    db = MySQLdb.connect(conf.DB.HOST, conf.DB.USER, conf.DB.PASS, conf.DB.NAME)
    cursor = db.cursor()

    sql = """
        select ID,UPLOAD_TIME,UPLOAD_NAME,START_TIME,
        (select count(*) from Packets where Packets.GROUP_ID=DataGroup.ID) as packets,
        IF( EXISTS (select * from Cflow where Cflow.GROUP_ID=DataGroup.ID),
            (select COUNT(*) from Cflow where Cflow.GROUP_ID=DataGroup.ID),
            '-'
        )
        from DataGroup
    """
    groups = cursor.fetchmany(cursor.execute(sql))

    print 'DATABASE_STATUS\n\nGROUP_ID | UPLOAD_TIME | UPLOAD_NAME | START_TIME | PACKETS | CALC_CFLOW'
    for g in groups:
        print('\t'.join([str(_) for _ in g]))


def fetch_apanel_results(table_name):
    """
    从数据库中读取A-panel聚类结果
    """
    db = MySQLdb.connect(DB.HOST, DB.USER, DB.PASS, DB.NAME)
    cursor = db.cursor()

    sql = "select IP_SRC from {}".format(table_name)
    raw_packets = cursor.fetchmany(cursor.execute(sql))
    print '[database] Selected A-panel table:{} ,results:{}'.format(table_name, len(raw_packets))
    return raw_packets
