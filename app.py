import os
from datetime import datetime
import pytz
import requests
import simplejson as json
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
    if event.message.text.find('時間') >= 0:
        tpe = pytz.timezone('Asia/Taipei')
        tpeTime = str(tpe.fromutc(datetime.utcnow()))
        date = tpeTime.split(' ')[0].split('-')
        time = tpeTime.split(' ')[1].split('.')[0].split(':')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=(
            '台北時間：' + date[0] + '年' + date[1] + '月' + date[2] + '日' + time[0] + '時' + time[1] + '分')))
        return None

    # weather app
    if('天氣' in event.message.text):
        # find the location users ask in the string of user input
        if event.message.text.find('市') > 0:
            locationIndex = event.message.text.find('市')
        elif event.message.text.find('縣') > 0:
            locationIndex = event.message.text.find('縣')
        else:
            line_bot_api.push_message(profile.user_id, TextSendMessage(text='請輸入XX市/縣天氣，查詢天氣。'))
            return None

        locationIndexStart = locationIndex - 2
        locationIndexEnd = locationIndex + 1
        location = event.message.text[locationIndexStart:locationIndexEnd]
        url = 'http://opendata.cwb.gov.tw/opendataapi?dataid=F-C0032-009&authorizationkey=' + WEATHER_API_KEY
        data = requests.get(url).text
        weatherComment = data.split('<parameterValue>')[1].split('</parameterValue>')[0]
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=weatherComment))
        return None
    
    line_bot_api.push_message(profile.user_id, TextSendMessage(text='我不了解「' + event.message.text + '」是什麼意思。'))


@handler.add(PostbackEvent)
def handle_postback(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    if event.postback.data == 'works-intro1':
        message.worksIntro1(line_bot_api, profile.user_id)
    if event.postback.data == 'works-intro2':
        message.worksIntro2(line_bot_api, profile.user_id)
    if event.postback.data == 'works-intro3':
        message.worksIntro3(line_bot_api, profile.user_id)
    if event.postback.data == 'works-intro4':
        message.worksIntro4(line_bot_api, profile.user_id)
    if event.postback.data == 'works-intro5':
        message.worksIntro5(line_bot_api, profile.user_id)


if __name__ == "__main__":
    app.run()
