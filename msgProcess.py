import linebot
from linebot.models import *


class profileProblem():
    def __init__(self, profile, line_bot_api):
        self.displayName = profile.display_name
        self.userId = profile.user_id
        self.pictureUrl = profile.picture_url
        self.statusMessage = profile.status_message
        self.lineBotApi = line_bot_api
        self.menuDict = {
            '名字': 'name', '稱呼': 'name',
            '關於我': 'aboutMe', '你好': 'aboutMe', '您好': 'aboutMe',
            '個性': 'personality',
            '學歷': 'education', '畢業': 'education',
        }

    def isMenuOption(self, msg):
        for key in self.menuDict.keys():
            if key in msg:
                return True
        return False

    def chooseMenuOption(self, msg):
        for key in self.menuDict.keys():
            if key in msg:
                option = self.menuDict[key]
        if option == 'name':
            self.__name()
        if option == 'aboutMe':
            self.__aboutMe()
        if option == 'education':
            self.__education()
        if option == 'personality':
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
                text='碩士班(在學中):國立臺北科技大學 資訊工程學系\n大學(畢業):國立嘉義大學 電機工程學系',
                actions=[
                    URITemplateAction(
                        label='北科大 資工系',
                        uri='http://csie.ntut.edu.tw/csie/index_i.htm'
                    ),
                    URITemplateAction(
                        label='嘉義大學 電機系',
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