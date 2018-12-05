#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

class PymysqlUtil():

    #初始化方法
    def __init__(self):
        self.host = "localhost"
        self.port = 3306
        self.user = "root"
        self.passwd = "root"
        self.dbName = "test"
        self.charsets = "utf8"

    #链接数据库
    def getCon(self):

        self.db = pymysql.connect(

            host=self.host,
            user=self.user,
            password=self.passwd,
            db="live",
            port=self.port,
            charset=self.charsets
        )
        self.cursor = self.db.cursor()

    #关闭链接
    def close(self):
        self.cursor.close()
        self.db.close()

    #查询单行记录
    def get_one(self, sql):
        res = None
        try:
            self.getCon()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
        except Exception as e:
            print(e)
            print("查询失败!")
        return res

    #查询列表数据
    def get_all(self, sql):
        res = None
        try:
            self.getCon()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except Exception as e:

            print(e)
            print("查询失败！")
        return res

    #插入数据
    def __insert(self, sql):
        count = 0
        try:
            self.getCon()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print("操作失败！")
            self.db.rollback()
        return count

    #修改数据
    def __edit(self, sql):
        return self.__insert(sql)

    #删除数据
    def __delete(self, sql):
        return self.__insert(sql)

    #更新数据
    def __update(self, sql):
        return self.__insert(sql)


    def testselect(self):

        db = pymysql.connect(host="localhost", user="root",
                             password="root", db="live", port=3306)
        cur = db.cursor()

        sql = "select * from test"

        cur.execute(sql)

        results = cur.fetchall()

        print(results)

        db.close()

