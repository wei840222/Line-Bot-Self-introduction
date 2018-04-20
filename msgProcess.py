import linebot
from linebot.models import *


class profileMenu():
    def __init__(self, profile, line_bot_api):
        self.displayName = profile.display_name
        self.userId = profile.user_id
        self.pictureUrl = profile.picture_url
        self.statusMessage = profile.status_message
        self.lineBotApi = line_bot_api
        self.menuOption = ['關於我', '學歷', '工作經驗', '專長', '作品', '聯繫方式', '個性', '你好', '您好', '名字', '稱呼']

    def isMenuOption(self, msg):
        for mo in self.menuOption:
            if mo in msg:
                return True
        return False

    def chooseMenuOption(self, msg):
        for mo in self.menuOption:
            if mo in msg:
                option = mo
        if option == '名字' or option == '稱呼':
            self.__name()
        if option == '關於我' or option == '你好' or option == '您好':
            self.__aboutMe()
        if option == '學歷':
            self.__education()
        if option == '個性':
            self.__personality()

    def __name(self):
        try:
            self.lineBotApi.push_message(self.userId, TextSendMessage(
                text='你可以叫我 wei'))
        except linebot.exceptions.LineBotApiError as e:
            print(e.status_code)
            print(e.error.message)
            print(e.error.details)

    def __aboutMe(self):
        try:
            self.lineBotApi.push_message(self.userId, TextSendMessage(
                text='您好！ 我是wei-bot\n性別是男生\n喜歡聽音樂、跳舞、看youtube'))
        except linebot.exceptions.LineBotApiError as e:
            print(e.status_code)
            print(e.error.message)
            print(e.error.details)

    def __personality(self):
        try:
            self.lineBotApi.push_message(self.userId, TextSendMessage(
                text='個性樂觀,可以有條理的安排事情,學習能力高,擅長與人合作執行專案。'))
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
                text='碩士班(在學中)\n國立臺北科技大學 資訊工程學系\n\n大學(畢業)\n國立嘉義大學 電機工程學系',
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
