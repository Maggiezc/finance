import datetime
import re
import time
from datetime import date
from datetime import datetime
from datetime import timedelta

import pandas as pd
import requests
import os
import pdb
import  matplotlib.pyplot as plt

# 跌幅分布统计(随时间段,横坐标是斜率和长度,分不同的股票)跌幅越大,概率越小,所以总的跌幅是有一定规律的,按照这个来写权重就行!
# 截尾正态分布
# 最终期望是多少
# 同样上涨概率分布统计(随时间段)
# 如果金额小了离散下不就行了吗,离散状态下的公式
# 跌幅回调曲线统计(随时间段, 发生跌幅时v字形的概率,即涨幅和跌幅之间的关联分布)
# 当整体趋势是涨的时候分布会发生怎样的变化
# debug:当直线下落时怎样分布股票权重(1%,2%,4%…..)
# 需要50%长期,50%短期吗
# 考虑末尾变化范围是一个小正态分布的话,考虑交易失败的话怎么进行下一个交易(FIFO队列里元素limit的值怎么变化)
# 暂时只考虑当天而不是跨天的
# 平滑滤波,高斯滤波
# pattern转换,当看到单边跌时候从震荡判定切换到单边跌模式

#中值滤波滤出噪声的平均幅度
#总资产,股价,振幅三者之间关系的可视化
#crawl跌幅榜, 自动在跌幅榜中找出最低点附近的股票, EST11点左右, 列举, 分列图, 如何判断震荡
#点击跳转页面
#从博弈角度看,短期相关的是必输的,所以relatively小震荡都可以忽略,尤其在100+股以上情况下,至少半小时才能变成时间无关
#以lendingclub为例看震荡,
#瀑布式两者走势比较,叠加动态图, 随时间走动的gif图像, 同步放大缩小选项, 倒数工具,叠加
#考虑robinhood的交易滞后和不能立刻交易
#波动率, 曲线波动率计算
#添加播放器playlist(参考hulu)
#imdb的volume
#动量效应, 动量投资策略, 反转效应, 股票定价理论, 吸附效应动态定价
#monitor和login system
#点击跳转
Date = "2016-05-10"
item = 'DATA'

filename = "data/"+item+".pkl"
data0 = pd.read_pickle(filename)

def amplitudeDistribution:
	

def main():


if __name__ == "__main__":
    main()