import os
from datetime import datetime
import pytz
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import message


app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get('ACCESS_TOKEN'))
handler = WebhookHandler(os.environ.get('SECRET'))
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # log #
    print("Handle: userId: " + event.source.user_id + ", reply_token: " +
          event.reply_token + ", message: " + event.message.text)
    try:
        profile = line_bot_api.get_profile(event.source.user_id)
        print(profile.display_name)
        print(profile.user_id)
        print(profile.picture_url)
        print(profile.status_message)
    except LineBotApiError as e:
        print('can\'t get user profile')
    # log #

    msgDict = {
        '你好': message.hi, '您好': message.hi,
        '名字': message.name, '稱呼': message.name,
        '關於我': message.aboutMe,
        '個性': message.personality,
        '興趣': message.interesting, '愛好': message.interesting,
        '學歷': message.education, '畢業': message.education,
        '專長': message.expertise, '程式': message.expertise, '會什麼': message.expertise,
        '作品': message.works, '專題': message.works, '專案': message.works,
        '小工具': message.tools, '工具': message.tools,
        '聯繫方式': message.contact, '郵件': message.contact, 'mail': message.contact
    }

    # search key word in msgDict and reply
    for key in msgDict.keys():
        if key in event.message.text:
            line_bot_api.reply_message(event.reply_token, msgDict[key])
            return None

    # time app
    if '時間' in event.message.text:
        tpe = pytz.timezone('Asia/Taipei')
        tpeTime = str(tpe.fromutc(datetime.utcnow()))
        date = tpeTime.split(' ')[0].split('-')
        time = tpeTime.split(' ')[1].split('.')[0].split(':')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=(
            '台北時間：' + date[0] + '年' + date[1] + '月' + date[2] + '日' + time[0] + '時' + time[1] + '分')))
        return None

    # weather app
    locationDict = {
        '台北市': 'F-C0032-009', '新北市': 'F-C0032-010', '基隆市': 'F-C0032-011', '花蓮縣': 'F-C0032-012', '宜蘭縣': 'F-C0032-013', '金門縣': 'F-C0032-014', '澎湖縣': 'F-C0032-015',
        '台南市': 'F-C0032-016', '高雄市': 'F-C0032-017', '嘉義縣': 'F-C0032-018', '嘉義市': 'F-C0032-019', '苗栗縣': 'F-C0032-020', '台中市': 'F-C0032-021', '桃園市': 'F-C0032-022',
        '新竹縣': 'F-C0032-023', '新竹市': 'F-C0032-024', '屏東縣': 'F-C0032-025', '南投縣': 'F-C0032-026', '台東縣': 'F-C0032-027', '彰化縣': 'F-C0032-028', '雲林縣': 'F-C0032-029',
        '連江縣': 'F-C0032-030'
    }
    if '天氣' in event.message.text:
        # find the location users ask in the string of user input
        location = None
        for key in locationDict.keys():
            if key in event.message.text.replace('臺', '台'):
                location = key
        if location is None:
            line_bot_api.push_message(
                profile.user_id, TextSendMessage(text='請輸入XX市/縣天氣，查詢天氣。'))
            return None

        # get data from gov weather restful api
        url = 'http://opendata.cwb.gov.tw/opendataapi?dataid=' + \
            locationDict[location] + '&authorizationkey=' + WEATHER_API_KEY
        data = requests.get(url).text
        weatherComment = data.split('<parameterValue>')[
            1].split('</parameterValue>')[0]
        weatherToday = data.split('<parameterValue>')[
            2].split('</parameterValue>')[0]
        weatherTomorrow = data.split('<parameterValue>')[
            3].split('</parameterValue>')[0]
        line_bot_api.push_message(
            profile.user_id, TextSendMessage(text=location + weatherComment))
        line_bot_api.push_message(
            profile.user_id, TextSendMessage(text=weatherToday))
        line_bot_api.push_message(
            profile.user_id, TextSendMessage(text=weatherTomorrow))
        return None

    # Apple News
    if '新聞' in event.message.text:
        url = 'http://www.appledaily.com.tw/realtimenews/section/new/'
        rs = requests.session()
        res = rs.get(url, verify=False)
        soup = BeautifulSoup(res.text, 'html.parser')
        for index, data in enumerate(soup.select('.rtddt a'), 0):
            if index == 5:
                return None
            else:
                link = data['href']
                line_bot_api.push_message(profile.user_id, TextSendMessage(text=link))
    
    # can't find any msg to reply
    line_bot_api.push_message(profile.user_id, TextSendMessage(
        text='我不了解「' + event.message.text + '」是什麼意思。'))


@handler.add(PostbackEvent)
def handle_postback(event):
    msgStackDict = {'works-intro1':message.worksIntro1, 'works-intro2':message.worksIntro2, 'works-intro3':message.worksIntro3, 'works-intro4':message.worksIntro4, 'works-intro5':message.worksIntro5}
    profile = line_bot_api.get_profile(event.source.user_id)
    if event.postback.data in msgStackDict.keys():
        for msg in msgStackDict[event.postback.data]:
            line_bot_api.push_message(profile.user_id, msg)

if __name__ == "__main__":
    app.run()
