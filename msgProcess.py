import linebot
from linebot.models import *


class profileMenu():
    def __init__(self, profile, line_bot_api):
        self.displayName = profile.display_name
        self.userId = profile.user_id
        self.pictureUrl = profile.picture_url
        self.statusMessage = profile.status_message
        self.lineBotApi = line_bot_api
        self.menuOption = ['關於我', '學歷', '工作經驗', '專長', '作品集', '聯繫方式', '個性']

    def isMenuOption(self, msg):
        for mo in self.menuOption:
            if mo in msg:
                return True
        return False

    def chooseMenuOption(self, msg):
        for mo in self.menuOption:
            if mo in msg:
                option = mo
        if option == '關於我':
            self.__aboutMe()
        if option == '學歷':
            self.__education()
        if option == '個性':
            self.__personality()

    def __aboutMe(self):
        aboutMe = TemplateSendMessage(
            alt_text='關於我',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='http://dl.profile.line-cdn.net/0m0141d2787251505f7b256e319a705112ad315105a5f8',
                        title='萬俊瑋',
                        text='我的名字',
                        actions=[
                            MessageTemplateAction(
                                label='個性',
                                text='個性'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='http://www.people.com.cn/mediafile/pic/20160428/1/13513915896936444957.jpg',
                        title='興趣',
                        text='喜歡聽音樂',
                        actions=[
                            URITemplateAction(
                                label='[EXID(이엑스아이디)] 덜덜덜(DDD) 뮤직 비디오',
                                uri='https://www.youtube.com/watch?v=axVvZrDz60k&list=PL7f6_T4y_Sv8Dsr04sRBJX95PqDtkK2Ea&index=1&t=0s'
                            ),
                            URITemplateAction(
                                label='閻奕格 Janice Yan [ 也可以 ] (電影「追婚日記」插曲) 片花版',
                                uri='https://www.youtube.com/watch?v=PZGwZwGQTlk&index=1&list=PL7f6_T4y_Sv9dHswKWWx34OAbzp_mzCUR&t=0s'
                            ),
                            URITemplateAction(
                                label='DJ Cassidy - Make the World Go Round ft. R. Kelly',
                                uri='https://www.youtube.com/watch?v=HeC-Hj97eak&index=1&list=PL7f6_T4y_Sv_gSrrvL5Q_8vunJxq8aaxO&t=0s'
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
