#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Date     : 2017/11/20
# @Author   : GCC
# @Version  : 1.0
# @describe : 启动程序
from rbot import robotes
from tools import literals_TO_voice # 文字转声音
from tools import sound_recording   # 录音
from tools import voice_TO_literals # 声音转文字
import mp3play
import time

def playMusic():
    # 播放mp3
    play_mp3 = mp3play.load(r'.\file\test.mp3')  # 加载mp3文件
    play_mp3.play()  # 开始播放mp3
    time.sleep(play_mp3.seconds() + 1)  # 播放"mp3的长度+1"秒
    play_mp3.stop()  # 播放完毕

if __name__ == "__main__":
    rbot = robotes()
    flag = True
    while flag:
        # 1.录音
        print "请说话："
        sound_recording.record_to_file(r'..\file\demo.wav')
        print "录音结束,说'退出'结束程序"
        # 2.声音转文字 保存到say变量里去
        say = voice_TO_literals.get_say()
        # print say
        # 3.机器人回答
        if '退出' not in say:
            # 把机器人回答转成语音
            rbot.run(say,r'.\file\test.mp3')
            # 播放语音
            playMusic()
        else:
            flag = False
