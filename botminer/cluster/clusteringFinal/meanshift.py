import numpy as np
import csv
from sklearn.cluster import MeanShift, estimate_bandwidth

def run_cluster():
    print('[cluster] starting clustering')
    np.set_printoptions(threshold='nan')
    ip_src = []
    ip = open("result/ip.csv", "r")
    ip_src = ip.read().split("\n")[:-1]
    ip.close()
    csvfile = file('result/msresult.csv', 'wb')
    writer = csv.writer(csvfile)
    result=[]
    X = np.loadtxt("result/tmp.csv", delimiter=",", skiprows=0, ndmin=2)
    # estimate_bandwidth(X)
    bandwidth = 0.875
    ms = MeanShift(bin_seeding=True,cluster_all=True).fit(X)
    # y_pred=ms.fit_predict(X)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_
    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)
    meanshift = [[] for c in range(n_clusters_)]
    print("number of estimated clusters : %d" % n_clusters_)

    for k in range(len(labels)):
        meanshift[labels[k]].append(ip_src[k])
    for k in range(n_clusters_):
        #print len(meanshift[k]), meanshift[k]
        result.append((meanshift[k]))
    writer.writerows(result)
    csvfile.close()
