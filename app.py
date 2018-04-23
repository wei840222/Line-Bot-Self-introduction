from datetime import datetime
import pytz
import requests
from linebot.models import *


class Time():
    def __init__(self):
        self.tpeTimeZone = pytz.timezone('Asia/Taipei')

    def getTime(self):
        tpeTime = str(self.tpeTimeZone.fromutc(datetime.utcnow()))
        date = tpeTime.split(' ')[0].split('-')
        time = tpeTime.split(' ')[1].split('.')[0].split(':')
        return TextSendMessage(text=('台北時間：' + date[0] + '年' + date[1] + '月' + date[2] + '日' + time[0] + '時' + time[1] + '分'))


class Weather():
    locationDict = {
        '台北市': 'F-C0032-009', '新北市': 'F-C0032-010', '基隆市': 'F-C0032-011', '花蓮縣': 'F-C0032-012', '宜蘭縣': 'F-C0032-013', '金門縣': 'F-C0032-014', '澎湖縣': 'F-C0032-015',
        '台南市': 'F-C0032-016', '高雄市': 'F-C0032-017', '嘉義縣': 'F-C0032-018', '嘉義市': 'F-C0032-019', '苗栗縣': 'F-C0032-020', '台中市': 'F-C0032-021', '桃園市': 'F-C0032-022',
        '新竹縣': 'F-C0032-023', '新竹市': 'F-C0032-024', '屏東縣': 'F-C0032-025', '南投縣': 'F-C0032-026', '台東縣': 'F-C0032-027', '彰化縣': 'F-C0032-028', '雲林縣': 'F-C0032-029',
        '連江縣': 'F-C0032-030'
    }

    def __init__(self, WEATHER_API_KEY):
        self.WEATHER_API_KEY = WEATHER_API_KEY

    def __getWeatherData(self, location):
        # get data from gov weather restful api
        url = 'http://opendata.cwb.gov.tw/opendataapi?dataid=' + \
        self.locationDict[location] + '&authorizationkey=' + self.WEATHER_API_KEY
        return requests.get(url).text

    def __getXmlValueFromTag(self, xmlData, tag):
        result = list()
        for value in xmlData.split('<' + tag + '>')[1:]:
            result.append(value.split('</' + tag + '>')[0])
        return result

    def getWeather(self, queryText):
        # find the location users ask in the string of user input
        location = None
        print(self.locationDict.keys())
        print(queryText.replace('臺', '台'))
        for key in self.locationDict.keys():
            if key in queryText.replace('臺', '台'):
                location = key
        print(location)
        msgList = list()
        if location is not None:
            xmlData = self.__getWeatherData(location)
            weatherForecast = self.__getXmlValueFromTag(xmlData, 'parameterValue')
            for text in weatherForecast:
                msgList.append(TextSendMessage(text=text))
        else:
            msgList.append(TextSendMessage(text='請輸入XX市/縣天氣，查詢天氣。\nex:台北市天氣'))
        return msgList