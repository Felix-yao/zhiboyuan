#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import time
from com.felix.dao.DidiaokanDao import DidiaokanDao
from com.felix.service.AikanqiuService import AikanqiuService


if __name__ == '__main__':

    h = 0
    m = 25

    while True:
        now = datetime.datetime.now()

        # print(now.hour, now.minute)

        # print(now.hour, now.minute, now.second)

        if now.hour == h and now.minute == m:

            # print("开始执行")


            # 获取爱看球直播源
            url = "https://www.aikanqiu.com/business.html"

            aikanqiuService = AikanqiuService();

            aikanqiuService.getInfo(url)

            # doSth()


        # 每隔60秒检测一次
        time.sleep(60)



