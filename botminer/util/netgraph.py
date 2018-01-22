# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from operator import itemgetter
import csv
import networkx as nx
import pylab
import math
import numpy as np
#自定义网络
row=[int(math.floor(i*200)) for i in list(np.random.random_sample(500))]
col=[int(math.floor(i*200)) for i in list(np.random.random_sample(500))]
value=[int(math.floor(i*1000)) for i in list(np.random.random_sample(10000))]
# 绘图参数全家桶
params = {
    'axes.labelsize': '16',
    'xtick.labelsize': '16',
    'ytick.labelsize': '13',
    'lines.linewidth': '2',
    'legend.fontsize': '20',
    'figure.figsize': '5, 5'  # set figure size
}

pylab.rcParams.update(params)

# print('生成一个空的有向图')
# # G=nx.DiGraph()
# G=nx.Graph()
# print('为这个网络添加节点...')
# # for i in range(200):
# #     G.add_node(i)
# print('在网络中添加带权重的边...')
# node = set()
# with open('C:/Desktop/bot/graph/oddball/oddball/65.nn1') as file:
#     import csv
#     reader = csv.reader(file,delimiter=' ')
#     for row in reader:
#         G.add_edges_from([(row[0], row[1])])
#         node.add(row[0])
#         node.add(row[1])
#     for i in node:
#         G.add_node(i,color='blue',size = 10)
# # for i in range(len(row)):
# #     # G.add_weighted_edges_from([(row[i],col[i],value[i])])
# #     G.add_edges_from([(row[i],col[i])])
# # print('输出网络中的节点...')
# # print(G.nodes())
# # print('输出网络中的边...')
# # print(G.edges())
# print('输出网络中边的数目...')
# print(G.number_of_edges())
# print('输出网络中节点的数目...')
# print(G.number_of_nodes())
# print('给网路设置布局...')
# # pos=nx.shell_layout(G)
# # pos=nx.random_layout(G)
# # pos = nx.circular_layout(G)
# # pos = nx.fruchterman_reingold_layout(G)
# # pos = nx.kamada_kawai_layout(G)
# # pos = nx.spring_layout(G)
#
# # print('画出网络图像：')
# # nx.draw(G,with_labels=False, width=1, edge_color='black',  alpha=1 )
# # pylab.title('Self_Define Net',fontsize=15)
# # pylab.show()
#
# # find node with largest degree
# node_and_degree = G.degree()
# (largest_hub, degree) = sorted(node_and_degree, key=itemgetter(1))[-1]
# # Create ego graph of main hub
# hub_ego = nx.ego_graph(G, largest_hub)
# # Draw graph
# pos = nx.spring_layout(hub_ego)
# nx.draw(hub_ego, pos, node_color='b', node_size=10, with_labels=False)
# # Draw ego as large and red
# nx.draw_networkx_nodes(hub_ego, pos, nodelist=[largest_hub], node_size=2, node_color='r')
# pylab.show()

n = 1000
m = 10
G = nx.generators.barabasi_albert_graph(n, m)
# find node with largest degree
node_and_degree = G.degree()
(largest_hub, degree) = sorted(node_and_degree, key=itemgetter(1))[-1]
# Create ego graph of main hub
hub_ego = nx.ego_graph(G, largest_hub)
# Draw graph
pos = nx.spring_layout(hub_ego)
nx.draw(hub_ego, pos, node_color='b', node_size=50, with_labels=False)
# Draw ego as large and red
nx.draw_networkx_nodes(hub_ego, pos, nodelist=[largest_hub], node_size=300, node_color='r')
pylab.show()