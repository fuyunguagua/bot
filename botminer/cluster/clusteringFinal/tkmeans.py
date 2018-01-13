# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
import numpy as np
import csv
from sklearn import metrics

def run_kmeans(cluster_num):
    ip = open("result/ip.csv", "r")
    ip_src = ip.read().split("\n")[:-1]
    ip.close()
    X = np.loadtxt("result/tmp.csv", delimiter=",", skiprows=0, ndmin=2)

    with open('result/kmeans_result41{}.csv'.format(cluster_num), 'wb+') as csvfile:
        writer = csv.writer(csvfile)
        result=[]
        k_means = KMeans(init="k-means++",n_clusters=cluster_num,n_init=10)
        y_pred = k_means.fit_predict(X)
        # print y_pred
        kmeans = [[] for i in range(cluster_num)]
        # print len(kmeans)
        for i in xrange(len(y_pred)):
            # kmeans[y_pred[i]].append(ip_src[i])
            kmeans[y_pred[i]].append(i)
        for i in range(cluster_num):
            # print len(kmeans[i]), kmeans[i]
            result.append((kmeans[i]))
        writer.writerows(result)
#
# print 'Calinski-Harabasz Score', metrics.calinski_harabaz_score(X, y_pred)
# # Step size of the mesh. Decrease to increase the quality of the VQ.
# h = .02     # point in the mesh [x_min, x_max]x[y_min, y_max].


