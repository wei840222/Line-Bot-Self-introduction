from linebot.models import *

hi = TextSendMessage(text='您好！ 我是wei-bot')

name = TextSendMessage(text='你可以叫我 wei')

aboutMe = TemplateSendMessage(
    alt_text='About Me',
    template=ButtonsTemplate(
        thumbnail_image_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t1.0-9/16114195_1303190386409212_9033059278762952732_n.jpg?_nc_cat=0&oh=80dae332df231e48592642b8588e3707&oe=5B6AE316',
        title='關於我',
        text='您好，我叫萬俊瑋，點擊下面可以了解更多資訊...',
        actions=[
            MessageTemplateAction(label='個性', text='個性'),
            MessageTemplateAction(label='興趣', text='興趣'),
            MessageTemplateAction(label='學歷', text='學歷'),
            MessageTemplateAction(label='專長', text='專長')
        ]
    )
)

personality = TextSendMessage(text='個性樂觀,可以有條理的安排事情,學習能力高,擅長與人合作執行專案。')

interesting = TextSendMessage(text='我喜歡聽音樂、跳舞、看youtube')

education = TemplateSendMessage(
    alt_text='Education',
    template=ButtonsTemplate(
        thumbnail_image_url='https://www.ntut.edu.tw/ezfiles/21/1021/img/2152/logo.jpg',
        title='學歷',
        text='碩士班(在學中):國立臺北科技大學 資訊工程學系\n大學(畢業):國立嘉義大學 電機工程學系',
        actions=[
            URITemplateAction(
                label='北科大 資工系', uri='http://csie.ntut.edu.tw/csie/index_i.htm'),
            URITemplateAction(label='嘉義大學 電機系',
                              uri='http://www.ncyu.edu.tw/ee/')
        ]
    )
)

expertise = TextSendMessage(text='C/C++, Python, Linux, Embedded System')

works = TemplateSendMessage(
    alt_text='Works',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://goo.gl/TSHPoY',
                title='智慧型電動助力單車暨行車資訊顯示系統之實現',
                text='大三專題',
                actions=[
                    PostbackTemplateAction(label='簡介', data='works-intro1'),
                    URITemplateAction(label='企劃書', uri='https://drive.google.com/open?id=1XTiU8S3ngquCqHZ4q1sZBdrfIYaJlws8'),
                    URITemplateAction(label='GitHub', uri='https://github.com/wei840222/NCYU-EE-Autobike-2015')
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://goo.gl/2MxPDu',
                title='田間自走機器人',
                text='大四專題',
                actions=[
                    PostbackTemplateAction(label='簡介', data='works-intro2'),
                    URITemplateAction(label='影片', uri='https://youtu.be/MTnS6NO3fM4'),
                    URITemplateAction(label='GitHub', uri='https://github.com/wei840222/Farm-Self-Propelled-Robot')
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t1.0-9/12009638_963539677040953_6771453829148070682_n.jpg?_nc_cat=0&oh=4ec5cd60367d47d3d70c1653e5c1ae7f&oe=5B5B8C1B',
                title='8051俄羅斯方塊',
                text='大二課程專案',
                actions=[
                    PostbackTemplateAction(label='簡介', data='works-intro3'),
                    URITemplateAction(label='影片', uri='https://youtu.be/B3hKuGS1lDE'),
                    URITemplateAction(label='GitHub', uri='https://github.com/wei840222/8051-Tetris')
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t31.0-8/30806226_1772336019494644_441235318761401904_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeEprbZornWvxRBZfWJ5JmaL3pR_F_6P8hPqu4tVVzBYfUIPCIaAbeMQPGXncwRVh-JWhNN0J-SyTnjTKlk-ELpop1cEBvRjjsaHnYU0GKpTYw&oh=d67e5b3958b60c398c80a1a120078e4f&oe=5B50C6E3',
                title='Fuzzy倒車入庫圖形介面',
                text='大三課外專案',
                actions=[
                    PostbackTemplateAction(label='簡介', data='works-intro4'),
                    URITemplateAction(label='影片', uri='https://youtu.be/MJCkf-ytCRo'),
                    URITemplateAction(label='GitHub', uri='https://github.com/wei840222/Fuzzy-OpenGL-GUI')
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t31.0-8/30171866_1772331252828454_6163523175446030911_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeERbMugA9iJGTieZM7h6tmBAkG8pUEVGlBd2eUO1hGr2_P-nx-m7A8NcldbRSb3_vtH2RsNwXEHpZpSFw9dr5648f7CIvuyn98CZWnMGgP0ow&oh=9cd64d8b408b515b85c515d26187d0dc&oe=5B56E453',
                title='106年扎根高中職資訊科學教育計劃網站',
                text='研一計畫網站',
                actions=[
                    PostbackTemplateAction(label='簡介', data='works-intro5'),
                    URITemplateAction(label='網站', uri='http://acl.csie.ntut.edu.tw/seniorhigh/index.html'),
                    URITemplateAction(label='GitHub', uri='https://github.com/wei840222/106-High-School-Website')
                ]
            )
        ]
    )
)

def worksIntro1(line_bot_api, user_id):
    line_bot_api.push_message(user_id, TextSendMessage(text='大三修習專題課程時,我與一位同學隨我們系主任進行:「智慧型電動單車助力暨資訊顯示系統」開發。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='在專題進行的過程中,我負責硬體驅動撰寫,如:加速計、藍芽模組與馬達輸出。'))
    line_bot_api.push_message(user_id, ImageSendMessage(original_content_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t31.0-8/30420598_1772746002786979_2578228845209619962_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeEhIPUf7C4U3Ddl1U9aa8bhIXnm7ACoHp6_0wAjDI8G3Y2WF-iW-zK9eQi8gnPotzqNmv44zL53KXEp-bD2zZtSxXrcD40QeZQqCxH4NEAXBQ&oh=abf908c57635184d8acec348600bbf09&oe=5B52CB3B', preview_image_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t31.0-8/30420598_1772746002786979_2578228845209619962_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeEhIPUf7C4U3Ddl1U9aa8bhIXnm7ACoHp6_0wAjDI8G3Y2WF-iW-zK9eQi8gnPotzqNmv44zL53KXEp-bD2zZtSxXrcD40QeZQqCxH4NEAXBQ&oh=abf908c57635184d8acec348600bbf09&oe=5B52CB3B'))
    line_bot_api.push_message(user_id, ImageSendMessage(original_content_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t1.0-9/31065581_1772747192786860_3199231543925185086_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeG9Rk21x2hE_YLI9V_tTyRYMIihs1ssRtxNyHbUGeAFxbZce6cVaEFXElsul2D7WAS4zlO4-D4G0_7S2I7jWD5ddNxErthdkdJfQoQM1fjuJw&oh=1491ea8694b13b391f1c433beeffd8d9&oe=5B5C6ED8', preview_image_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t1.0-9/31065581_1772747192786860_3199231543925185086_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeG9Rk21x2hE_YLI9V_tTyRYMIihs1ssRtxNyHbUGeAFxbZce6cVaEFXElsul2D7WAS4zlO4-D4G0_7S2I7jWD5ddNxErthdkdJfQoQM1fjuJw&oh=1491ea8694b13b391f1c433beeffd8d9&oe=5B5C6ED8'))
    line_bot_api.push_message(user_id, ImageSendMessage(original_content_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t31.0-8/30052413_1772745286120384_8713726014044494444_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGPy0cqBjLlrY7Rxx-MFTgkSxfW6KMjRFwnKAz8GbVZZebGjXd8SH6EGSOI3ntZI2U6lyPBB58lOLB4Jk7HwfelXq6gitt05aKLz3TDogAuCg&oh=8e125fc97c7d201b2dddf336886cbcb7&oe=5B5F3FB2', preview_image_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t31.0-8/30052413_1772745286120384_8713726014044494444_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGPy0cqBjLlrY7Rxx-MFTgkSxfW6KMjRFwnKAz8GbVZZebGjXd8SH6EGSOI3ntZI2U6lyPBB58lOLB4Jk7HwfelXq6gitt05aKLz3TDogAuCg&oh=8e125fc97c7d201b2dddf336886cbcb7&oe=5B5F3FB2'))
    line_bot_api.push_message(user_id, TextSendMessage(text='雖然第一次做大型專題,難免有困難,但我發現要與組員有效溝通,不是靠口頭表述,而是藉著圖表整理的實驗結果,更有說服力也能轉達想要表達的意思,並透過 GitHub 管理程式碼,可以更好的掌握進度與協力開發,避免時間拖延。。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='專題競賽海報:'))
    line_bot_api.push_message(user_id, TextSendMessage(text='https://drive.google.com/open?id=1ckI6pIbABZSvs8wmloe2cYNLg8kLM3Pv'))
    line_bot_api.push_message(user_id, TextSendMessage(text='競賽得獎紀錄:'))
    line_bot_api.push_message(user_id, ImageSendMessage(original_content_url='https://goo.gl/bwQi94', preview_image_url='https://goo.gl/bwQi94'))
    line_bot_api.push_message(user_id, ImageSendMessage(original_content_url='https://goo.gl/fkW5mM', preview_image_url='https://goo.gl/fkW5mM'))
    line_bot_api.push_message(user_id, ImageSendMessage(original_content_url='https://goo.gl/UPjXx1', preview_image_url='https://goo.gl/UPjXx1'))

def worksIntro2(line_bot_api, user_id):
    line_bot_api.push_message(user_id, TextSendMessage(text='大四上學期,我就讀生物機電工程的室友參加田間機器人競賽,請我協助機器人開發。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='有了大三專題的經驗,在既有的硬體上,我規劃出易於維護的軟體架構,針對細部的功能進行演算法開發。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='如:控制機器人硬體之 API、維持行走於賽道上的演算法、執行特定動作之函數。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='競賽得獎紀錄:'))
    line_bot_api.push_message(user_id, ImageSendMessage(original_content_url='https://goo.gl/ByL1hL', preview_image_url='https://goo.gl/ByL1hL'))
    line_bot_api.push_message(user_id, ImageSendMessage(original_content_url='https://goo.gl/pyhyBW', preview_image_url='https://goo.gl/pyhyBW'))

def worksIntro3(line_bot_api, user_id):
    line_bot_api.push_message(user_id, TextSendMessage(text='大二上學期,我修習一門微處理機應用的課程，所製作的專題。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='當時我在網路上看到一支影片，覺得很有趣，於是決定開發這個小專題。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='https://youtu.be/zpVccKRZgJA'))
    line_bot_api.push_message(user_id, TextSendMessage(text='這是我第一個，有別於以往，開始有在規劃架構的程式。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='那時也沒有學過軟體架構，我就照著我對這個專題的需求規劃了下圖的架構。'))
    line_bot_api.push_message(user_id, ImageSendMessage(original_content_url='https://goo.gl/AZ4yf5', preview_image_url='https://goo.gl/AZ4yf5'))
    line_bot_api.push_message(user_id, TextSendMessage(text='系統主要由控制硬體的函數，還有進行遊戲的函數所構成，由於是C語言，就沒有特別包成物件了。'))

def worksIntro4(line_bot_api, user_id):
    line_bot_api.push_message(user_id, TextSendMessage(text='大三上學期,我的同學專題製作Fuzzy倒車入庫的模擬，需要一個圖形界面，所以我就幫他們做了。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='代價是請我吃燒肉XD。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='剛好那學期，有修了一門遊戲程式設計的課。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='那門課教我們用OpenGL去實做一些畫面繪製的效果。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='https://github.com/wei840222/My-OpenGL-Game-Engine'))
    line_bot_api.push_message(user_id, TextSendMessage(text='於是呢，我就現學現賣的做的這個展示介面，還能跟使用者互動。'))

def worksIntro5(line_bot_api, user_id):
    line_bot_api.push_message(user_id, TextSendMessage(text='剛近來研究所時，我接了一個教育部的計畫。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='主要內容是教高中生寫程式做專題。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='由於計畫需要一個網站，去公告事情。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='但是我不會做網站阿QQ'))
    line_bot_api.push_message(user_id, TextSendMessage(text='於是呢，我就去Udemy上買了一門做網頁的課，並去搜尋一些如何架站的文章。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='一邊看影片一邊做出這個網站，然後又覺的實驗室的網站伺服器太慢。'))
    line_bot_api.push_message(user_id, TextSendMessage(text='就又把所有實驗室網頁一起搬到新主機上XD。'))

tools = TemplateSendMessage(
    alt_text='Tools',
    template=ButtonsTemplate(
        thumbnail_image_url='https://goo.gl/RnbH5y',
        title='小工具',
        text='對於這次的聊天機器人開發，我做了幾個小工具試試...',
        actions=[
            PostbackTemplateAction(label='時間', data='time'),
            PostbackTemplateAction(label='天氣', data='weather'),
            PostbackTemplateAction(label='蘋果新聞', data='news')
        ]
    )
)

contact = TextSendMessage(text='wei840222@gmail.com')