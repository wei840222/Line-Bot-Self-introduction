import linebot
from linebot.models import *


class profileMenu():
    def __init__(self, profile, line_bot_api):
        self.displayName = profile.display_name
        self.userId = profile.user_id
        self.pictureUrl = profile.picture_url
        self.statusMessage = profile.status_message
        self.lineBotApi = line_bot_api
        self.menuOption = ['關於我', '學歷', '工作經驗', '專長', '作品集', '聯繫方式']

    def isMenuOption(self, msg):
        return msg in self.menuOption

    def chooseMenuOption(self, msg):
        if msg == '關於我':
            self.__aboutMe()
        if msg == '學歷':
            self.__education()

    def __aboutMe(self):
        aboutMe = TemplateSendMessage(
            alt_text='關於我',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://example.com/item1.jpg',
                        title='萬俊瑋',
                        text='description1',
                        actions=[
                            PostbackTemplateAction(
                                label='postback1',
                                text='postback text1',
                                data='action=buy&itemid=1'
                            ),
                            MessageTemplateAction(
                                label='message1',
                                text='message text1'
                            ),
                            URITemplateAction(
                                label='uri1',
                                uri='http://example.com/1'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://example.com/item2.jpg',
                        title='this is menu2',
                        text='description2',
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='uri2',
                                uri='http://example.com/2'
                            )
                        ]
                    )
                ]
            )
        )
        try:
            self.lineBotApi.push_message(self.userId, TextSendMessage(
                text='您好！ 我叫是萬俊瑋，下面這些小卡片可以幫助您了解我。'))
            self.lineBotApi.push_message(self.userId, aboutMe)
        except linebot.exceptions.LineBotApiError as e:
            print(e.status_code)
            print(e.error.message)
            print(e.error.details)

    def __education(self):
        education = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://www.ntut.edu.tw/ezfiles/21/1021/img/2152/logo.jpg',
                title='學歷',
                text='碩士班(在學中)：國立臺北科技大學 資訊工程學系\n大學(畢業)：國立嘉義大學 電機工程學系',
                actions=[
                    URITemplateAction(
                        label='國立臺北科技大學 資訊工程學系',
                        uri='http://csie.ntut.edu.tw/csie/index_i.htm'
                    ),
                    URITemplateAction(
                        label='國立嘉義大學 電機工程學系',
                        uri='http://www.ncyu.edu.tw/ee/'
                    )
                ]
            )
        )
        try:
            self.lineBotApi.push_message(self.userId, education)
        except linebot.exceptions.LineBotApiError as e:
            print(e.status_code)
            print(e.error.message)
            print(e.error.details)
