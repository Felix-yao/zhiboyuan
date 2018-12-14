#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# sys.path.append("/Users/felix/PycharmProjects/zhiboyuan/com/felix/service")
import datetime
import time
# from com.felix.service.AikanqiuService import AikanqiuService
import AikanqiuService


if __name__ == '__main__':

    h = 0
    m = 25

    while True:
        now = datetime.datetime.now()

        print(now.hour, now.minute)

        # print(now.hour, now.minute, now.second)

        if now.hour == h and now.minute == m:

            print("开始获取数据")

            # 获取爱看球直播源
            url = "https://www.aikanqiu.com/business.html"

            aikanqiuService = AikanqiuService();

            aikanqiuService.getInfo(url)

            # doSth()


        # 每隔60秒检测一次
        time.sleep(60)



