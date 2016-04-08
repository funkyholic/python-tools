
-------------------getBaiduGeoData.py-------------------

概述:
本工具主要用以
基于中文地理位置信息
从百度Geo服务接口获取该地理位置的经纬坐标
详情: http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding


实现逻辑:
本程序使用python2
本程序调用了python csv和json库
从 addressTable.csv中读取中文地理位置信息
调用百度api获取经纬度
写入文件
