#描述
````
这是一个有关僵尸网络的流量分析项目，该方法通过对离线的流量进行聚类和图论特征的分析利用投票机制决定可疑的僵尸网络主机群。
具体论文请搜索《BotCapturer: Detecting Botnets based on Two-Layered Analysis with Graph Anomaly Detection and Network Traffic Clustering, International Journal of Performability Engineering, vol. 14, no. 5, pp. 1050-1059, May 2018. EI》
````
方法步骤
* 装载离线的流量入数据库
* 图论分析，找到异常点
* 主机间通讯模式的抽取，聚类分析
* 综合分析，输出主机群

##装载离线流量

解析pcap文件，结果存入MySQL数据库

**准备工作**

* MySQL环境 `sudo apt-get install mysql-server mysql-client`
* 启动MySQL服务 `sudo service mysql start`

**初次使用** 

* 编辑数据库配置 `vi loader/config.py`
* 建立数据表结构 `python loader/main.py --init`

**切分数据包（使用data文件夹下的示例数据，按1000个包切分）**

* `mkdir testdata`
* `editcap -c 1000 ../data/bot-brute-2.pcap ./testdata/small.pcap`

**数据入库**

* `python main.py ./data2 <TIME> <NOTE>`

```html
<TIME>     添加数据的时间，不重要。
<NOTE>     备注信息（数据内容描述、上传者等）
```

命令行输出：
```
[loader] Total pcap files: 177
[loader] 1/177 finished.
[loader] 2/177 finished.
...
[loader] 175/177 finished.
[loader] 176/177 finished.
[loader] 177/177 finished.
```


**TODO**

* 数据入库之前过滤掉部分数据包(非TCP协议/内网/不完整/白名单)

botminer
--------
以`GROUP_ID`检索，从库中提取指定的Packets，分类计算flow/cflow值，生成8/52维向量

* `cd ./botminer`

查看数据库状态  

* `python main.py --status`

```
DATABASE_STATUS

GROUP_ID | UPLOAD_TIME | UPLOAD_NAME | START_TIME | PACKETS | CALC_CFLOW
1	5.28.15.23	cdxy	    1000.0	0	-
2	5.28.15.23	cdxy	    1000.0	54	7
3	1111	    cdxy-real-1	1000.0	26542	-
5	1111	    cdxy-real-1	1000.0	105329	-
6	1111	    cdxy-real-1	1000.0	171863	82
7	111	        cdxy-real	1000.0	10207	-
8	111	        cdxy-real	1000.0	62008	-
9	111	        cdxy-real	1000.0	61997	-
10	1	        cdxy-test	1000.0	61997	2678
15	1	        cdxy-real	1000.0	5242606	32420

```
## 图的分析

异常得分的计算
这部分的代码利用的是：

输入：两两主机之间的交互频度

输出：每个主机的异常得分



## 聚类分析
计算Cflow并存入数据库  

* `python main.py 6 --save`

```
xy@kali:~/Desktop/botnet/BotMiner-x/botminer$ python main.py 6 --save
[database] Selected Packets: 171863
[common] START_TIME: 80.7388
[common] Packets loading finished.
[common] Total flows: 160796
[common] Instant flows: 983
[error] total-time=0, packet num: 3
[common] Total C_flows: 82
[common] Instant C_flows: 82
[scale-data] Scale flow.bps, total: 983
[scale-data] Scale flow.ppf, total: 983
[scale-data] Scale flow.bpp, total: 983
[calc] Data scaled success.
[database] Saving cflow vectors into database.
[!] [database] Group 6 already has 82 results, wants to overwrite? [Y/n]
[database] Done, inserted items count: 82

```
进入script文件夹下，运行fetch_cflows.py将数据库相关数据导入文件
```
python fetch_cflows.py
```
然后进入 clusteringFinal 文件夹下，运行main.py得到聚类结果
```
python main.py
```
聚类结果保存在result文件夹下

在botminer文件夹下运行main.py后跟参数 group_id 和 聚类结果csv文件，得到计算僵尸得分结果
```
python main.py group_id clusterFileName
```