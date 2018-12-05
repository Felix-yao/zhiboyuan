#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import time


if __name__ == '__main__':
    # 定时任务
    # 设定一个标签 确保是运行完定时任务后 再修改时间
    flag = 0
    # 获取当前时间
    now = datetime.datetime.now()
    # 启动时间
    # 启动时间为当前时间 加5秒
    sched_timer = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute,
                                    now.second) + datetime.timedelta(seconds=5)
    # 启动时间也可自行手动设置
    # sched_timer = datetime.datetime(2017,12,13,9,30,10)
    while (True):
        # 当前时间
        now = datetime.datetime.now()
        # print(type(now))
        # 本想用当前时间 == 启动时间作为判断标准，但是测试的时候 毫秒级的时间相等成功率很低 而且存在启动时间秒级与当前时间毫秒级比较的问题
        # 后来换成了以下方式，允许1秒之差
        print(now)
        print(sched_timer)

        if sched_timer < now < sched_timer + datetime.timedelta(seconds=1):
            time.sleep(1)
            print(now)
            # 运行程序
            # main(sched_timer)
            # 将标签设为 1
            flag = 1
        else:
            # 标签控制 表示主程序已运行，才修改定时任务时间
            if flag == 1:
                # 修改定时任务时间 时间间隔为2分钟
                sched_timer = sched_timer + datetime.timedelta(minutes=2)
                flag = 0



