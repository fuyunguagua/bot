#  -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

def drawBar(statistics, title, xlabel, ylabel):
    xticks = statistics.keys()  # 每个柱的下标说明
    gradeGroup = statistics # 用于画图的频率数据
    # 创建柱状图
    # 第一个参数为柱的横坐标
    # 第二个参数为柱的高度
    # 参数align为柱的对齐方式， 以第一个参数为参考标准
    plt.bar(range(len(xticks)), [gradeGroup.get(xtick, 0) for xtick in xticks], align='center', yerr=0.000001)

    # 设置柱的文字说明
    # 第一个参数为文字说明的横坐标
    # 第二个参数为文字说明的内容你想怎样
    # plt.xticks(range(len(xticks)), xticks)

    # 设置横坐标的文字说明
    plt.xlabel(xlabel)
    # 设置纵坐标的文字说明
    plt.ylabel(ylabel)
    # 设置标题
    plt.title(title)
    # 绘图

    plt.show()

#绘制饼形图
def drawPie(statistics,title):
    labels = statistics.keys()
    #创建饼形图
    #第一个参数为扇形的面积
    #labels参数为扇形的说明文字
    #autopct参数为扇形占比的显示格式
    plt.pie([statistics.get(label, 0) for label in labels], labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.show()

def drawScatter(statistics):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    # 设置标题
    ax1.set_title('outline')
    # 设置X轴标签
    plt.xlabel('ID')
    # 设置Y轴标签
    plt.ylabel('SCORE')
    ids = [149936,149648,149700,149987,158900]
    cValue = ['k' if int(key) not in ids else 'r' for key in statistics.keys()]
    sValue = [ 1 if int(key) not in ids else 20 for key in statistics.keys()]
    # 画散点图
    ax1.scatter(statistics.keys(), [statistics[key] for key in statistics], c=cValue, marker='o',s=sValue)
    # 设置图标
    plt.legend('x1')
    # 显示所画的图
    plt.show()

