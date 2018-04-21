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
                thumbnail_image_url='',
                title='智慧型電動助力單車暨行車資訊顯示系統之實現',
                text='大三專題',
                actions=[
                    URITemplateAction(label='企劃書', uri='https://drive.google.com/open?id=1XTiU8S3ngquCqHZ4q1sZBdrfIYaJlws8'),
                    URITemplateAction(label='GitHub', uri='https://github.com/wei840222/NCYU-EE-Autobike-2015')
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='',
                title='田間自走機器人',
                text='大四專題',
                actions=[
                    URITemplateAction(label='企劃書', uri='https://drive.google.com/open?id=1u17Cp5ssgcn4TktN3-nV0S_nUAnIRd3f'),
                    URITemplateAction(label='影片', uri='https://www.youtube.com/watch?v=MTnS6NO3fM4&t=147s'),
                    URITemplateAction(label='GitHub', uri='https://github.com/wei840222/Farm-Self-Propelled-Robot')
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='',
                title='8051俄羅斯方塊',
                text='大二課程專案',
                actions=[
                    URITemplateAction(label='影片', uri='https://www.youtube.com/watch?v=B3hKuGS1lDE')
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='',
                title='Fuzzy倒車入庫圖形介面',
                text='大三課外專案',
                actions=[
                    URITemplateAction(label='影片', uri='https://www.youtube.com/watch?v=MJCkf-ytCRo'),
                    URITemplateAction(label='GitHub', uri='https://github.com/wei840222/Fuzzy-OpenGL-GUI')
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='',
                title='106年扎根高中職資訊科學教育計劃網站',
                text='研一計畫網站',
                actions=[
                    URITemplateAction(label='網址', uri='http://acl.csie.ntut.edu.tw/seniorhigh/index.html'),
                    URITemplateAction(label='GitHub', uri='https://github.com/wei840222/106-High-School-Website')
                ]
            ),
        ]
    )
)
