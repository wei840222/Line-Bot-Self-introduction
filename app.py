import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from msgProcess import *
import message


def richMenuTest(line_bot_api, user_id):
    rich_menu_to_create = RichMenu(
        size=RichMenuBound(
            width=2500,
            height=1686
        ),
        selected=False,
        name="nice richmenu",
        chatBarText="touch me",
        areas=[
            RichMenuArea(
                RichMenuBound(
                    x=0,
                    y=0,
                    width=2500,
                    height=1686
                ),
                URITemplateAction(
                    uri='line://nv/location'
                )
            )
        ]
    )
    rich_menu_id = line_bot_api.create_rich_menu(data=rich_menu_to_create)
    print(rich_menu_id)
    line_bot_api.link_rich_menu_to_user(user_id, rich_menu_id)


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

    msg = event.message.text
    pp = profileProblem(profile, line_bot_api)
    if pp.isMenuOption(msg):
        pp.chooseMenuOption(msg)
    elif msg == 'richMenuTest':
        richMenuTest(line_bot_api, profile.user_id)
    else:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='我不了解「' + msg + '」是什麼意思。'))
    try:
        line_bot_api.push_message(profile.user_id, message.aboutMe)
        line_bot_api.push_message(profile.user_id, message.personality)
        line_bot_api.push_message(profile.user_id, message.interesting)
        line_bot_api.push_message(profile.user_id, message.education)
        line_bot_api.push_message(profile.user_id, message.expertise)
    except LineBotApiError as e:
        print(e.status_code)
        print(e.error.message)
        print(e.error.details)


if __name__ == "__main__":
    app.run()
