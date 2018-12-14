#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from com.felix.util.RequestGet import RequestGet
from bs4 import BeautifulSoup
import js2xml
from lxml import etree
import random
import requests
from com.felix.bean.GameBean import GameBean



class DidiaokanService:

    def getGameList(self, url):

        try:

            didiaokanService = DidiaokanService()

            requestGet = RequestGet();

            text = requestGet.getHtmlTextEncode(url,"UTF-8");

            bs = BeautifulSoup(text,"lxml");

            list_js = bs.find("script").get("src");  #获取当天的直播列表的js地址

            text_js = requestGet.getHtmlText(list_js);

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

                homeNameTemp = '备用网址'

                # print("比赛名称---- " + font + "||时间---- " + time + "||主队---- " + homeName + "||客队---- " + guestName + "||视频地址--" + videoPageUrl)

                if not (homeNameTemp in font): #判断后除去第一条

                    gameName = 'NBA'

                    if gameName in font:    #判断是不是nba的比赛


                        gameBean = GameBean(font, videoPageUrl, homeName, guestName, time)

                        didiaokanService.getLiveList(gameBean)

                    else:

                        # print("other game")
                        didiaokanService.getOtherIframeUrl(videoPageUrl)


        except Exception as e:

            print(e);




    def getLiveList(self, gameBean):


        print("didiaokanBean-----"+ gameBean.homeTeam)

        url = gameBean.url;

        try:

            aTemp = 'a'

            indexRs = aTemp in url

            urlTemp = ''

            if(indexRs):

                t = '?'

                index = url.find(t)

                urlTemp = url[0:index]+"/p.html"

            else:

                urlTemp;

            requestGet = RequestGet();

            bs = requestGet.getBs4Encode(urlTemp, "UTF8")

            hrefs = bs.find_all('a', class_='mv_action_btn3')

            for href in hrefs:

                textTemp = '本站'

                isIn = textTemp in href.text

                if not (isIn):

                    liveUrl = href.get('href')

                    # print(liveUrl)

                    didiaokan = DidiaokanService()

                    didiaokan.getNbaVideoIframeUrl(liveUrl, gameBean)

        except Exception as e:

            print(e)


    def getNbaVideoIframeUrl(self, url, gameBean):

        # print(url)

        didiaokan = DidiaokanService()

        rsq = RequestGet()

        rsBs = rsq.getBs4Encode(url, 'utf8')

        src = rsBs.select('body script')[0].string

        src_text = js2xml.parse(src, encoding='utf-8', debug=False)

        src_tree = js2xml.pretty_print(src_text)

        selector = etree.HTML(src_tree)

        content = selector.xpath('//left/binaryoperation/left/string')

        iframeTemp = content[0].text+"\">"

        iframeBs = BeautifulSoup(iframeTemp, "lxml")

        iframeUrl = iframeBs.find('iframe').get('src')+didiaokan.getJsonx1(url)

        # print("aaaaa"+iframeBs.find('iframe').get('src')+didiaokan.getJsonx1(url))

        print("比赛名:"+gameBean.gameName+"主队:"+gameBean.homeTeam+"客队:"+gameBean.guestTeam+"时间:"+gameBean.time)

        print("iframe地址:"+iframeUrl)

    def getJsonx1(self,homeUrl):

        randomTemp = str(random.random())

        html = '.html'

        php = '.php'

        isHtml = html in homeUrl

        isPhp = php in homeUrl

        url = ''

        if isHtml:

            url = homeUrl.replace(".html", "b.html") + "?id=" + randomTemp + ""

        elif isPhp:

            url = homeUrl.replace(".php", "b.php") + "?id=" + randomTemp + ""


        rs = requests.get(url)

        rsJson = rs.json()

        return rsJson['x1']


    def getOtherIframeUrl(self, videoUrl):

        req = RequestGet()

        bs4 = req.getBs4Encode(videoUrl, 'utf8')

        iframeUrl = bs4.find('iframe').get('src')

        print(iframeUrl)







if __name__ == '__main__':

    didiaokan = DidiaokanService()

    #
    # url = 'http://www.sportstream1231.com/5.html'
    #
    # didiaokan = DidiaokanService()
    #
    # print(didiaokan.getJsonx1(url));


    url = "http://m.didiaokan.com/body.html";

    didiaokan.getGameList(url);


    # url = "http://www.didiaokan.com//a/100209800?classid=1&id=8242";
    #
    # DidiaokanService.getLiveList(url)


    # http: // www.didiaokan.com // a / 100204100?classid = 1 & id = 8176
    #
    # http: // www.didiaokan.com // le / pptvf.php?url = 300605 &?classid = 3 & id = 23664








