from linebot.models import *

aboutMe = '''
我的名字叫 萬俊瑋
性別是男生
興趣是聽音樂、跳舞、看Youtube
'''

def education():
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://www.ntut.edu.tw/ezfiles/21/1021/img/2152/logo.jpg',
            title='學歷',
            text='在學中...',
            actions=[
                URITemplateAction(
                    label='碩士班：國立臺北科技大學 資訊工程學系',
                    uri='http://csie.ntut.edu.tw/csie/index_i.htm'
                ),
                URITemplateAction(
                    label='大學：國立嘉義大學 電機工程學系',
                    uri='http://www.ncyu.edu.tw/ee/'
                )
            ]
        )
    )
    return message

def msgIdentify(msg):
    if msg == '關於我':
        return TextSendMessage(text=aboutMe)
    elif msg == '學歷':
        return TextSendMessage(text='我的名字叫 萬俊瑋\n性別是男生\n興趣是聽音樂、跳舞、看Youtube')
    else:
        return TextSendMessage(text='你說什麼？')