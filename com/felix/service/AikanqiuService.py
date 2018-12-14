#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from com.felix.util.RequestGet import RequestGet
import RequestGet
import datetime
import requests


class AikanqiuService:



    def getInfo(self,url):

        rsq = RequestGet()

        bs = rsq.getBs4(url)

        nowData = datetime.datetime.now().strftime('%Y年%m月%d日')

        isSkillYear = 0

        for i, gameTemp in enumerate(bs.find_all('tr')):

            try:

                dateTemp  = self.getGameDate(gameTemp);


                #用当前时间来判断爬取的开始时间内容
                if nowData in dateTemp:

                    print("开始获取:")

                    isSkillYear = 1


                #当爬取的下个时间与当前系统时间不同则判断是下一天的时间，则结束当前爬取
                if not (nowData in dateTemp) and dateTemp != '':

                    print("获取结束")

                    break



                if isSkillYear == 1:

                    gameType = gameTemp.find('p').text

                    gameName = gameTemp.find_all('td')[1].text

                    gameTime = gameTemp.find_all('td')[2].text

                    guestTeamName = gameTemp.find_all('td')[3].text

                    homeTeamName = gameTemp.find_all('td')[7].text

                    gameUrl = gameTemp.find('input').get('value')

                    gameNameNba = 'NBA'

                    if gameNameNba in gameName:

                        print("主队:" + homeTeamName + "--" + "客队:" + guestTeamName + "时间:" + gameTime)

                        url = 'http://localhost:8081/live/saveGame'

                        data = {"gameName": gameName, "gameTime": gameTime, "homeTeamName": homeTeamName,
                                "guestTeamName": guestTeamName, "iframeUrl": gameUrl}

                        rs = requests.post(url, data)

                        print("返回结果:")
                        print(rs)


            except Exception as e:

                print("")



    def getGameDate(self, gameInfoTemp):

        try:

            # 用'年'来判断是否是时间
            if '年' in gameInfoTemp.find('th').text:

                gameInfoTemp = gameInfoTemp.find('th').text

                return gameInfoTemp

        except Exception as e:

             return ''







if __name__ == '__main__':

    aikanqiuService = AikanqiuService()

    url = "https://www.aikanqiu.com/business.html"

    aikanqiuService.getInfo(url)
