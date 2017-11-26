#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Date     :  2017/11/26
# @Author   :  GCC
# @Version  :  1.5
# @describe :  文字转语音

import os
from aip import AipSpeech

# 你的 APPID AK SK 申请网址http://yuyin.baidu.com/
APP_ID = '你的APP_ID'
API_KEY = '你的API_KEY'
SECRET_KEY = '你的SECRET_KEY'
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def say(say,WAV):
    """
    文字转语音
    :param say: 文字， 这里是机器人的回答
    :return:
    """
    result = aipSpeech.synthesis(say, 'zh', 1, {'vol': 5,'per':3}) # 百度api相关方法
    # 检查本目录下是否存在test.mp3文件,如果存在则删除,方便之后创建新的mp3文件
    if os.path.exists(WAV):
        os.remove(WAV)
    # 百度api返回的结果 result 有时候是一个dict类型，写入到mp3会报错
    if not isinstance(result,dict):
        try:
            with open(WAV,'wb') as f:
                f.write(result)
        except IOError as e:
            print e
