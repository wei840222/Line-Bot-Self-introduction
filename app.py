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
        '連江縣': 'F-C0032-030',
        '台北': 'F-C0032-009', '新北': 'F-C0032-010', '基隆': 'F-C0032-011', '花蓮': 'F-C0032-012', '宜蘭': 'F-C0032-013', '金門': 'F-C0032-014', '澎湖': 'F-C0032-015',
        '台南': 'F-C0032-016', '高雄': 'F-C0032-017', '嘉義': 'F-C0032-019', '苗栗': 'F-C0032-020', '台中': 'F-C0032-021', '桃園': 'F-C0032-022', '新竹': 'F-C0032-024',
        '屏東': 'F-C0032-025', '南投': 'F-C0032-026', '台東': 'F-C0032-027', '彰化': 'F-C0032-028', '雲林': 'F-C0032-029', '連江': 'F-C0032-030'
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
        for key in self.locationDict.keys():
            if key in queryText.replace('臺', '台'):
                location = key
        msgList = list()
        if location is not None:
            xmlData = self.__getWeatherData(location)
            weatherForecast = self.__getXmlValueFromTag(xmlData, 'parameterValue')
            for text in weatherForecast:
                msgList.append(TextSendMessage(text=text))
        else:
            msgList.append(TextSendMessage(text='請輸入XX(市/縣)天氣，查詢天氣。\nex:台北市天氣 or 高雄天氣'))
        return msgList