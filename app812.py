from flask import Flask, request, abort, url_for, send_from_directory
from flask.helpers import make_response

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========


#
app = Flask(__name__)


#
# ngrok_code='a204aebc94b9'
Channel_Access_Token='YcqixOuILYduL5xwR20RHFRW8q9Wgf+Zxd+DjxC2zj2NG5kNEHJTBlODaBZOCsP3R1ilmm8XF3FCLbpIis/TqaPhou0Eh2kzcd7HBdmABY9yRtrq2k46yZm+vdFTTG6npTPANjzQzlT8sgzaHFoSkgdB04t89/1O/w1cDnyilFU='

## RB JOK
# Channel Access Token
line_bot_api = LineBotApi(Channel_Access_Token)
# Channel Secret
handler = WebhookHandler('21fead04f5a568736230dd83e25ca8cf')



# RB DDD
# Channel Access Token
#line_bot_api = LineBotApi('UTA0U6Wsg0el+sPXHDYAzgC0vndoBg1+Ai53hGEnM6xs1f5eh/NNf0TcQKVUqwgdjF2UcHRLSMr7bY/Hjl74L8RocS7uYtD27Z7pbOQ5E1PkJ29qQSmYgFluhMzyBchuTJHqXHdQsqJUf49Aa1gJbQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
#handler = WebhookHandler('afe0107e68034bbd7d4fd768ff9447f1')



# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    
    print("我被post了")

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("body= ",body)

    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    

    ###
    if '1' in msg:
        #message = TextSendMessage(text=str1)
        message = test3(texts="123")
        line_bot_api.reply_message(event.reply_token, message)

    elif '2' in msg:
        #message = TextSendMessage(text=str2)
        message = test3(texts="223")
        line_bot_api.reply_message(event.reply_token, message)

    elif '3' in msg:
        message = TextSendMessage(text="323")
        line_bot_api.reply_message(event.reply_token, message)

    ###
    
    # elif '最新合作廠商' in msg:
    #     message = imagemap_message()
    #     line_bot_api.reply_message(event.reply_token, message)
    # elif '最新活動訊息' in msg:
    #     message = buttons_message()
    #     line_bot_api.reply_message(event.reply_token, message)
    # elif '註冊會員' in msg:
    #     message = Confirm_Template()
    #     line_bot_api.reply_message(event.reply_token, message)



    ###
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)

    ###
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        #message = function_list()
        message = test2()
        line_bot_api.reply_message(event.reply_token, message)

    
    # ### 未定義
    # else:
    #     message = TextSendMessage(text="未定義")
    #     line_bot_api.reply_message(event.reply_token, message)
    


### 
@app.route("/")
def index():
    return "<h1>Jinde 首頁</h1>"

###
@app.route('/files/<string:filename>', methods=['GET'])
def show_photo(filename):
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            #logger.debug('filename is %s' % filename)
            image_data = open(os.path.join('D:/line_bot/linebot/imgdata/'+filename), "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/jpg'
            return response



import os

if __name__ == "__main__":

    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)




#-------------
'''
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

#
line_bot_api = LineBotApi(Channel_Access_Token)
try:
    line_bot_api.push_message('<to>', TextSendMessage(text='Hello World!'))
except LineBotApiError as e:
    # error handle
    print("error")
'''



#-------------

'''
import requests
auth_token=Channel_Access_Token
hed = {'Authorization': 'Bearer ' + auth_token}
data = {
    "messages":[
        {
            "type":"text",
            "text":"Hello, world1"
        },
        {
            "type":"text",
            "text":"Hello, world2"
        }
    ]
}

url = 'https://api.line.me/v2/bot/message/broadcast'
response = requests.post(url, json=data, headers=hed)
print(response)
print(response.json())
'''
