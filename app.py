from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('UHx4krGjn312dEscSbJBzj/epUFsy5lCQUSlcqTYLYkUK8QnU+yr9d7oPfA/a7LAmfZe0pYkMWuwTiv4ocNsNeH9FRcyIS14ND5ZTgVOByLXcf+4AN2hzMsx5cZ4/RD9PI/gNn1e0L/eI73PCw5hPwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('5d2b3b485e228fc299ae89df9e34e36b')

# listen /callback Post Request
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
    message = TextSendMessage(text='hello wei!')
    line_bot_api.reply_message(
        event.reply_token,
        message)

if __name__ == "__main__":
    app.run()
