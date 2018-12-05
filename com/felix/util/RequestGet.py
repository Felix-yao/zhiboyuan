#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

class RequestGet:

    def getHtmlTextEncode(url,encode):
        try:
            html = requests.get(url)

            html.encoding = encode

            return html.text
        except:
            print('except:获取'+html+'文本失败')


    def getHtmlText(url):

        try:
            html = requests.get(url);

            return html.text;

        except:
            print('获取'+url+"文本失败")

            return "";


