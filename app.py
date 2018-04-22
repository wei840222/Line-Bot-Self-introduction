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
WEATHERAPIKEY = os.environ.get('WEATHER_API_KEY')

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

    # search key word in msgDict
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

    # weather app
    if('天氣' in event.message.text):
        # find the location users ask in the string of user input
        if event.message.text.find('市') > 0:
            locationIndex = event.message.text.find('市')
        elif event.message.text.find('縣') > 0:
            locationIndex = event.message.text.find('縣')
        else:
            line_bot_api.push_message(profile.user_id, TextSendMessage(text='請直接輸入XX市/縣天氣，查詢天氣。'))
            return None

        locationIndexStart = locationIndex - 2
        locationIndexEnd = locationIndex + 1
        location = event.message.text[locationIndexStart:locationIndexEnd]
        print(location)
        url = "http://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?locationName=" + \
            location+"&elementName=Wx"
        header = {"Authorization": WEATHERAPIKEY}
        origin = requests.get(url, headers=header)
        body = json.loads(origin.content)
        # Determind which prediction of time interval for the weather of the location.
        try:
            timeIntervalPredict = body['records']['location'][0]['weatherElement'][0]['time']
            for possibleTime in timeIntervalPredict:
                # type of time info: string -> datetime
                timeInterval = datetime.strptime(
                    possibleTime['startTime'], "%Y-%m-%d %H:%M:%S")
                if(datetime > timeInterval):
                    discription = possibleTime['parameter']['paramterName']
            reply = location + '的天氣為' + discription
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=reply))
            return None
        except:
            line_bot_api.reply_message(event.reply_token, TextMessage(
                text="yo~台灣沒這個地方～\n或是請愛用繁體「臺」ex「臺南市」"))
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
