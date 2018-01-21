# !/usr/bin/env python
#  -*- coding: utf-8 -*-

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
    'figure.figsize': '6, 10'  # set figure size
}
pylab.rcParams.update(params)

print('生成一个空的有向图')
G=nx.DiGraph()
print('为这个网络添加节点...')
for i in range(200):
    G.add_node(i)
print('在网络中添加带权重的边...')
for i in range(len(row)):
    # G.add_weighted_edges_from([(row[i],col[i],value[i])])
    G.add_edges_from([(row[i],col[i])])
# print('输出网络中的节点...')
# print(G.nodes())
# print('输出网络中的边...')
# print(G.edges())
print('输出网络中边的数目...')
print(G.number_of_edges())
print('输出网络中节点的数目...')
print(G.number_of_nodes())
print('给网路设置布局...')
# pos=nx.shell_layout(G)
pos=nx.random_layout(G)
# pos = nx.circular_layout(G)
# pos = nx.fruchterman_reingold_layout(G)
# pos = nx.kamada_kawai_layout(G)
# pos = nx.spring_layout(G)

print('画出网络图像：')
nx.draw(G,pos,with_labels=False, width=0.1,node_color='blue', edge_color='blue', node_size=5, alpha=1 )
pylab.title('Self_Define Net',fontsize=15)
pylab.show()
