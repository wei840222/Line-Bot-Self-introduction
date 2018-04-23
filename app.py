from datetime import datetime
import pytz
from linebot.models import *


class Time():
    def __init__(self):
        self.tpeTimeZone = pytz.timezone('Asia/Taipei')

    def getTime(self):
        tpeTime = self.tpeTimeZone.fromutc(datetime.utcnow())
        date = tpeTime.split(' ')[0].split('-')
        time = tpeTime.split(' ')[1].split('.')[0].split(':')
        return TextSendMessage(text=('台北時間：' + date[0] + '年' + date[1] + '月' + date[2] + '日' + time[0] + '時' + time[1] + '分'))