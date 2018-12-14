#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

class RequestGet:

    def getHtmlTextEncode(self, url, encode):
        try:
            html = requests.get(url)

            html.encoding = encode

            return html.text
        except:
            print('except:获取'+html+'文本失败')


    def getHtmlText(self, url):

        try:
            html = requests.get(url);

            return html.text;

        except:
            print('获取'+url+"文本失败")

            return ""


    def getBs4(self,url):

        try:

            return BeautifulSoup(self.getHtmlText(url), "lxml")

        except Exception as e:

            print(e)

            print("转bs4异常---"+e)


    def getBs4Encode(self, url, code):

        try:

            return BeautifulSoup(self.getHtmlTextEncode(url, code), "lxml")

        except:

            print("转bs4异常");





