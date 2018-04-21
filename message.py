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
                    PostbackTemplateAction(label='開發過程', text='助力車開發過程', data='exp1'),
                    MessageTemplateAction(label='影片', text='助力車影片'),
                    URITemplateAction(label='GitHub', uri='https://github.com/wei840222/NCYU-EE-Autobike-2015')
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://goo.gl/2MxPDu',
                title='田間自走機器人',
                text='大四專題',
                actions=[
                    PostbackTemplateAction(label='開發過程', text='田間機器人開發過程', data='exp2'),
                    MessageTemplateAction(label='影片', text='田間機器人影片'),
                    URITemplateAction(label='GitHub', uri='https://github.com/wei840222/Farm-Self-Propelled-Robot')
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t1.0-9/12009638_963539677040953_6771453829148070682_n.jpg?_nc_cat=0&oh=4ec5cd60367d47d3d70c1653e5c1ae7f&oe=5B5B8C1B',
                title='8051俄羅斯方塊',
                text='大二課程專案',
                actions=[
                    PostbackTemplateAction(label='開發過程', text='8051開發過程', data='exp3'),
                    MessageTemplateAction(label='影片', text='8051影片'),
                    URITemplateAction(label='GitHub', uri='https://www.youtube.com/watch?v=B3hKuGS1lDE')
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t31.0-8/30806226_1772336019494644_441235318761401904_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeEprbZornWvxRBZfWJ5JmaL3pR_F_6P8hPqu4tVVzBYfUIPCIaAbeMQPGXncwRVh-JWhNN0J-SyTnjTKlk-ELpop1cEBvRjjsaHnYU0GKpTYw&oh=d67e5b3958b60c398c80a1a120078e4f&oe=5B50C6E3',
                title='Fuzzy倒車入庫圖形介面',
                text='大三課外專案',
                actions=[
                    PostbackTemplateAction(label='開發過程', text='倒車入庫開發過程', data='exp4'),
                    MessageTemplateAction(label='影片', text='倒車入庫影片'),
                    URITemplateAction(label='GitHub', uri='https://github.com/wei840222/Fuzzy-OpenGL-GUI')
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://scontent.ftpe2-2.fna.fbcdn.net/v/t31.0-8/30171866_1772331252828454_6163523175446030911_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeERbMugA9iJGTieZM7h6tmBAkG8pUEVGlBd2eUO1hGr2_P-nx-m7A8NcldbRSb3_vtH2RsNwXEHpZpSFw9dr5648f7CIvuyn98CZWnMGgP0ow&oh=9cd64d8b408b515b85c515d26187d0dc&oe=5B56E453',
                title='106年扎根高中職資訊科學教育計劃網站',
                text='研一計畫網站',
                actions=[
                    PostbackTemplateAction(label='開發過程', text='扎根網站開發過程', data='exp5'),
                    MessageTemplateAction(label='影片', text='扎根影片'),
                    URITemplateAction(label='網站', uri='http://acl.csie.ntut.edu.tw/seniorhigh/index.html')
                ]
            )
        ]
    )
)

works1_video_message = TextSendMessage(text='抱歉這個專案沒有影片喔！ QQ')

works2_video_message = VideoSendMessage(
    original_content_url='http://140.124.181.76/farmrobot.mp4',
    preview_image_url='https://i.ytimg.com/vi/MTnS6NO3fM4/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIZCGAFwAQ==&rs=AOn4CLAisDYYI7xNTJQkLis6NdfEfnYOKg'
)

works3_video_message = VideoSendMessage(
    original_content_url='http://140.124.181.76/8051.mp4',
    preview_image_url='https://i.ytimg.com/vi/B3hKuGS1lDE/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIZCGAFwAQ==&rs=AOn4CLCmOe1W_jfs_v75Smu9tPtiiPPrWQ'
)

works4_video_message = VideoSendMessage(
    original_content_url='http://140.124.181.76/fuzzy.mp4',
    preview_image_url='https://i.ytimg.com/vi/MJCkf-ytCRo/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIZCGAFwAQ==&rs=AOn4CLBzcxJfEXdbiQt1xAIgTXH9AI_CeQ'
)

works5_video_message = works1_video_message