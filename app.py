import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import message


app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get('ACCESS_TOKEN'))
handler = WebhookHandler(os.environ.get('SECRET'))


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
        '助力車影片': message.works1_video_message, '田間機器人影片': message.works2_video_message, '8051影片': message.works3_video_message, '倒車入庫影片': message.works4_video_message, '扎根影片': message.works5_video_message, 
    }

    # search key word in msgDict
    for key in msgDict.keys():
        if key in event.message.text:
            line_bot_api.reply_message(event.reply_token, msgDict[key])
            return None
    
    # for test
    if event.message.text == 'test':
        try:
            line_bot_api.push_message(profile.user_id, message.works)
        except LineBotApiError as e:
            print(e.status_code)
            print(e.error.message)
            print(e.error.details)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='我不了解「' + event.message.text + '」是什麼意思。'))
    


if __name__ == "__main__":
    app.run()
