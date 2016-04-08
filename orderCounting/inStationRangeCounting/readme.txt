
-------------------inStationRangeCounting.py-------------------

概述:
本工具主要用以
基于大量订单坐标信息，以及地铁站点坐标信息
计算地铁站点一定半径范围内的订单数量


实现逻辑:
本程序使用python2
本程序调用了python csv和json库
从 station.csv文件中 读取站点的经纬度等信息 
从 data.json文件中 读取订单经纬度等信息
计算站点坐标与订单坐标之间距离，绝对值小与阈值即标记count++
输出站点周围订单数量——保存成output.json
console输出 站点名:计数 信息

