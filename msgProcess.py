from linebot.models import *

aboutMe = '''
我的名字叫 萬俊瑋
性別是男生
興趣是聽音樂、跳舞、看Youtube
'''

def getTemplte():
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://example.com/image.jpg',
            title='Menu',
            text='Please select',
            actions=[
                PostbackTemplateAction(
                    label='postback',
                    text='postback text',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='message',
                    text='message text'
                ),
                URITemplateAction(
                    label='uri',
                    uri='http://example.com/'
                )
            ]
        )
    )
    return message

def msgIdentify(msg):
    msgDict = {'@關於我':aboutMe}
    reMsg = msgDict[msg]
    if reMsg is not None:
        return TextSendMessage(text=reMsg)
    else:
        return TextSendMessage(text='你說什麼？')