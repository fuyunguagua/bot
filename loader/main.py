# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import sys
from common import init_database, insert_packets
from help import helpmsg


def main():

    if '--init' in sys.argv:
        init_database()
        exit('Database initialized success.')

    if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv) < 5:
        helpmsg()

    delete = False
    if '--delete' in sys.argv:  # delete local pcap file after loaded.
        print "[system] File delete enabled."
        delete = True

    #insert_packets(delete)

#python main.py path tablename --delete
import os,sys

def split_files(path):
    abs_path = os.path.abspath(path)
    if not os.path.exists(os.path.join(abs_path, 'result')):
        os.mkdir(os.path.join(abs_path, 'result'))
    for index, file in enumerate(os.listdir(path)):
        if os.path.isfile(os.path.join(abs_path, file)):
            name = file.split('.')[0]
            command = 'editcap.exe -F libpcap -c 100000 ' + os.path.join(abs_path, file) + ' ' + os.path.abspath(
                path) + '\\result\\' + name + '.pcap'
            os.system(command)

def rename_outfile(path):
    abs_path = os.path.abspath(path)
    for file in os.listdir(os.path.join(abs_path,'result')):
        split_result = file.split('_')
        new_name = '_'.join([split_result[0],split_result[1]])+'.pcap'
        os.rename(os.path.join(abs_path,'result',file),os.path.join(abs_path,'result',new_name))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit('please input args')
    file_or_directory = sys.argv[1]
    table_name = sys.argv[2]
    delete = False
    if '--delete' in sys.argv:  # delete local pcap file after loaded.
        print "[system] File delete enabled."
        delete = True
    print('[Initial] Spliting pcap file')
    split_files(file_or_directory)
    rename_outfile(file_or_directory)
    print('[Begining] Starting read files')
    insert_packets(file_or_directory=file_or_directory,
                   table_name=table_name,
                   delete=True)