# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 20:04:35 2021
@author: darksheep
"""
import requests
from bs4 import BeautifulSoup
import json
import re
#爬取菜鸟教程string 方法,并转化为json
#找到tbody,遍历里面的td,或者找tr的第二个td
#TODO 无序号的情况
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}
r=requests.get("https://www.runoob.com/java/java-linkedlist.html",headers=headers)
r.encoding = r.apparent_encoding#分析内容编码方式,防止出现乱码
bs=BeautifulSoup(r.text,'lxml')
#使用CSS选择器获取tr中的td,过滤表头:tr>th
td_list=bs.select("tr > td ")
#获取需要爬取的行数
td_size=len(td_list)/2
#TODO 此变量默认为0,当页面中出现多个表格,且出现的第一个表格内容不想爬取时,更新i的值
i=8
res_list=[]
while i<td_size:
    #每行的第一个td为函数名,第二个为函数功能
    name=td_list[i*2].text.strip()#strip()去除字符串两端多余的空格
    trans=td_list[i*2+1].text.strip()
    res_list.append({'name':name,'trans':[name+":"+trans]})
    i=i+1
#将列表格式化为json,ensure_ascii=False解决中文乱码,并使用
# 参数:sort_keys=True, indent=4, separators=(',', ': ')美化格式
data=json.dumps(res_list,ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
print(data)

    
    
