# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from data import cpanel, conf
from model import Cflow, Flow, Packet


def split_flow():
    flows = {}
    for p in cpanel.PACKETS:
        vector = ':'.join([p.ip_src, p.ip_dst, p.port_src, p.port_dst])
        if vector in flows:
            flows[vector].append(p)
        else:
            flows[vector] = [p]
    print '[common] Total flows: {}'.format(len(flows))

    count = 1
    filtered_flows = []
    for _vector, _packets in flows.iteritems():
        if len(_packets) < 3:  # 删除只有一个包的flow，根据测试效果决定是否选用
            pass
        else:
            filtered_flows.append(Flow(count, _vector, _packets))
            count += 1
    #处理mirai僵尸网络，将连续的两个数据包作为一个flow
    new_filtered_flows = []
    for flow in filtered_flows:
        if flow.ip_dst == '120.76.125.235':
            print 'Detect a telnet flow,the packets is :',len(flow.packets)
            num = 0
            _vector = ':'.join([flow.ip_src, flow.ip_dst, flow.port_src, flow.port_dst])
            try:
                for i in range(len(flow.packets)):
                    if flow.packets[i].byte == 70:
                        p = [flow.packets[i],flow.packets[i+1]]
                        new_filtered_flows.append(Flow(count, _vector, p))
                        num += 1
                        count += 1
            except IndexError:
                continue
            print 'Aggregation new flow number is:',num
        else:
            new_filtered_flows.append(flow)
    cpanel.FLOWS = new_filtered_flows
    print '[common] Instant flows: {}'.format(len(cpanel.FLOWS))

    # 计算三个关键值
    for f in cpanel.FLOWS:
        f.calc()


def split_cflow():
    cflow = {}
    for f in cpanel.FLOWS:
        vector = ':'.join([f.ip_src, f.ip_dst, f.port_dst])
        if vector in cflow:
            cflow[vector].append(f)
        else:
            cflow[vector] = [f]
    print '[common] Total C_flows: {}'.format(len(cflow))

    count = 1
    filtered_cflows = []
    for _vector, _flows in cflow.iteritems():
        # TODO add filter here
        filtered_cflows.append(Cflow(count, 0, 24, _vector, _flows))  # TODO epoch调整为全局变量？动态获取？
        count += 1
    for cf in filtered_cflows:
        if cf.ip_dst == '120.76.125.235':
            print 'C-flow flows nums:',cf.flow_count
    cpanel.C_FLOWS = filtered_cflows
    print '[common] Instant C_flows: {}'.format(len(cpanel.C_FLOWS))

def filter_cflow():
    # TODO fix here when done
    #处理那些是bot但是flow大于1的C_flow,将其flow变为1（选出packet最多的flow）
    for cflow in cpanel.C_FLOWS:
        if not cmp(cflow.ip_dst,'120.76.125.235') and not cmp(cflow.port_dst,'23') and cflow.flow_count > 1:
            max_index = 0
            max_packet_num = 0
            for index, flow in enumerate(cflow.flows):
                if flow.packet_num > max_packet_num:
                    max_index = index
                    max_packet_num = flow.packet_num
            new_flows = []
            new_flows.append(cflow.flows[max_index])
            cflow.flows = new_flows
            cflow.flow_count = 1

def save(output_path):
    with open(output_path, 'w') as f:  # TODO more checks here
        for cf in cpanel.C_FLOWS:
            line = ','.join([
                str(cf.id), str(cf.fph), str(cf.bps), str(cf.bpp),
                str(cf.ppf), str(cf.ip_src), str(cf.ip_dst), str(cf.port_dst)]
            ).replace('[', '').replace(']', '').replace(' ', '')

            f.write(line + '\n')
