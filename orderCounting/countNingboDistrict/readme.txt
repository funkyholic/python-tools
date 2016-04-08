

-------------------countNingboDistrict.py-------------------

概述:
本工具主要用以
基于python正则匹配
基于大量宁波中文订单地址信息
计算宁波城市各区各有多少订单


实现逻辑:
本程序使用python2
本程序调用了python csv和json库 以及re库
从 inNingboData.csv中获取所有中文订单地址信息
正则匹配关键字
console输出字典 {区名:计数} 

