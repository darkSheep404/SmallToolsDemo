# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:58:22 2021
@author: darksheep
"""
# 导入模块
from wxpy import *
from IPython import embed
import time
import random
# 初始化机器人，扫码登陆
bot = Bot()
my_friend = bot.friends().search('2号')[0]
my_friend.send('Hello WeChat!')
list_replyed=[]
@bot.register()
def print_messages(msg):
    #群聊
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    #回复祝福
    if("年" in msg.text):
         #如果该好友已经回复过,退出函数   
        if msg.sender in list_replyed:
            print("--->已经回复过的好友",end='')
            print(msg)
            return
        #将已回复过祝福的好友加入列表
        list_replyed.append(msg.sender)
        print("进入年判定")
        #从祝福列表和同文件夹下图片中随机选取图片+祝福回复
        bless=["祝你岁岁常欢愉，年年皆胜意，多喜乐，长安宁","祝你好心情正常营业，烦心事永远打烊","祝你2021年,三餐四季,温暖有趣","愿新的一年开心与好运与你撞个满怀"]
        ran=random.randint(1,5)
        ran2=random.randint(0,3)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        print(ran)
        #img="00"+ran+".jpg":错误的拼接方式
        img='00{}.jpg'.format(ran)
        #print(img)
        print(msg)
        print(bless[ran2],end="--->")
        print(img)
        msg.reply_image(img)
        msg.reply_msg("新年快乐鸭(*^▽^*)\n ")
        msg.reply_msg(bless[ran2])
        return
    #回复
    print (time.strftime("%H:%M:%S", time.localtime()))
    print(msg)
    #return '冬眠中,已收到: {} ({})'.format(msg.text, msg.type)
    return        
embed()#阻塞函数并进入命令行
