#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from com.felix.util.PyMysqlUtil import PymysqlUtil

class DidiaokanDao:

    def saveLive(self):

        pymysqlUtil = PymysqlUtil()

        pymysqlUtil.insert(

            "insert into game ( `NAME`, `TIME`, `HOME_TEAM_ID`, `GUEST_TEAM_ID`, `LIVE_LIST_ID`) values ( 'test2', '8:00', '1', '1', '1')"

        )


    def saveGameInfo(self):

        pymysqlUtil = PymysqlUtil()

        pymysqlUtil.insert()

