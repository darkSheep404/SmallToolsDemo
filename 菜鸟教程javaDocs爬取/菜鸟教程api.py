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
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}
r=requests.get("https://www.runoob.com/java/java-arraylist.html",headers=headers)
r.encoding = r.apparent_encoding#分析内容编码方式,防止出现乱码
#初始化美丽汤库
bs=BeautifulSoup(r.text,'lxml')
td_list=bs.select("tr > td ")#使用css选择器,选择tr中的td,以免读取到th表头
td_size=len(td_list)/2#获取行数,读取第二个单元格,第一个是序号,使用下标计算访问
#TODO 此变量默认为0,当页面中出现多个表格,且出现的第一个表格内容不想爬取时,更新i的值
i=9
res_list=[]
while i<=td_size:
    #每行的第二个单元格即为函数名与解释
    temp=td_list[i*2-1].text.strip()
    m=temp.split("\n")#用\n分割符,分开函数名和解释
    #()左边的就是函数名,所需要求函数名右边为(),不需要入参
    temp_name_list=m[0].strip().split("(")[0].split(" ")
    temp_name_len=len(temp_name_list)
    temp_name=temp_name_list[temp_name_len-1]#左边如果被空格分割开,则最后一个就是函数名
   
    temp_name=temp_name+"()"
    res_list.append({'name':temp_name,'trans':[m[0].strip()+":"+m[1].strip()]})
    i=i+1
    
#将列表格式化为json,ensure_ascii=False解决中文乱码,并使用
# 参数:sort_keys=True, indent=4, separators=(',', ': ')美化格式
data=json.dumps(res_list,ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
print(data)
#废弃的不太聪明的获得函数名的方法:根据空格分割后的几组元素位置确定函数名位置,容易定位失败
#改为'('左边即为函数名
 #一个:isEmpty()
    #2个:String trim()
    #3个:"contains(CharSequence chars),如果是数组,则是[]4个
    ##
   # if temp_name_len==1:
       # temp_name=temp_name_list[0]
   # elif temp_name_list[0] == "static":
    #    temp_name=temp_name_list[2]
    #else:
     #   temp_name=temp_name_list[1]
        #/
        
    
