#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from com.felix.util.RequestGet import RequestGet
from bs4 import BeautifulSoup

class didiaokan:

    def getGameList(url):
        try:
            text = RequestGet.getHtmlTextEncode(url,"UTF-8");

            bs = BeautifulSoup(text,"lxml");

            list_js = bs.find("script").get("src");  #获取当天的直播列表的js地址

            text_js = RequestGet.getHtmlText(list_js);

            # print(text_js)

            bs_js = BeautifulSoup(text_js.replace("\\",""), "lxml");


            for li in bs_js.find_all("a"):

                # print(li)

                font = li.find("font").text  # name

                time = li.find('div', class_='time').text.replace("\t", "")

                homeName = li.find('div', class_='team').text

                guestName = li.find('div',class_='team right has-hover1').text

                videoPageUrlTemp = li.get("href")

                videoPageUrl = videoPageUrlTemp.replace("\\\"", "")

                print("比赛名称---- "+font+"||时间---- "+time+"||主队---- "+homeName+"||客队---- "+guestName+"||视频地址--"+videoPageUrl)

                # print("时间---- "+time)
                #
                # print("主队---- "+homeName)
                #
                # print("客队---- "+guestName)



                # print()

                print(videoPageUrl)

        except:

            print("报错");





if __name__ == '__main__':


    url = "http://m.didiaokan.com/body.html";

    didiaokan.getGameList(url);



