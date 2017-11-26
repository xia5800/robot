#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Date     :  2017/11/26
# @Author   :  GCC
# @Version  :  1.5
# @describe :  语音转文字

from aip import AipSpeech
import json

# 你的 APPID AK SK 申请网址http://yuyin.baidu.com/
APP_ID = '你的APP_ID'
API_KEY = '你的API_KEY'
SECRET_KEY = '你的SECRET_KEY'
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
def get_say():
    content = aipSpeech.asr(get_file_content('demo.wav'), 'wav', 16000, {
        'lan': 'zh',
    })
    data = json.dumps(content)
    say = json.loads(data)['result'][0]     # 得到语音识别成的文字
    return say