#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Date     : 2017/11/20
# @Author   : GCC
# @Version  : 1.5
# @describe : 智能问答机器人
"""
# 版本    创建时间     作者        功能描述
# 1.0     2017/11/15  GCC         实现基本功能
# 1.5     2017/11/20  GCC         增加代码注释
"""

import requests
import json
from tools import literals_TO_voice
import mp3play
import time
import sys
reload(sys)                             # 解决ascii问题
sys.setdefaultencoding('utf8')          # 解决ascii问题

class robotes:
    def run(self,say):
        """
        机器人运行
        :param say: 你的问题
        :return: robotsay 机器人的回答
        """
        # 构造请求url
        url = "http://api.jisuapi.com/iqa/query"
        question = {
            "appkey":"你的appkey",           # <--------------  在此填入你申请到的appkey 网址https://www.jisuapi.com/api/iqa/
            "question":say
        }
        # 请求机器人api，得到返回数据
        answer = requests.get(url,params=question).content
        # 机器人api返回的json
        data = json.loads(answer)
        # print data
        # 如果status的值为0，说明机器人成功回答了你的问题。否则打印错误信息
        if data['status'] == "0":
            # 控制台打印机器人回答的话。
            robotsay = data['result']['content']
            # 实现了语音之后，这行代码就没卵用了
            print "机器人的回答：%s" %(robotsay)
            literals_TO_voice.say(robotsay)
            # 返回机器人回答的话
        else:
            # 错误信息
            robotsay = data['msg']
            print robotsay     # 打印错误信息
            literals_TO_voice.say(robotsay)
