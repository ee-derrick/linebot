from flask import Flask, request, abort


from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *




#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

#
import shioaji as sj

api = sj.Shioaji()
v = api.login(
    person_id="R124279806", 
    passwd="jindeyf00", 
    contracts_cb=lambda security_type: print(f"{repr(security_type)} fetch done.")
)



#
app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')



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
    listall = api.list_positions(api.stock_account)
    sum=0
    #
    for i in listall:
        #print(i['pnl'])
        sum+=i['pnl']

        if(i['code']=='8044'):
            v8044=i
            vd8044=str(v8044['price'])
            vdc8044=str(v8044['pnl'])
        if(i['code']=='2492'):
            v2492=i
            vd2492=str(v2492['price'])
            vdc2492=str(v2492['pnl'])
        if(i['code']=='3669'):
            v3669=i
            vd3669=str(v3669['price'])
            vdc3669=str(v3669['pnl'])

    #
    contracts = [api.Contracts.Stocks['8044']]
    v8044ingL = api.snapshots(contracts)
    v8044ing=str(v8044ingL[0]['buy_price'])
    #print(v8044ing)

    contracts = [api.Contracts.Stocks['2492']]
    v2492ingL = api.snapshots(contracts)
    v2492ing=str(v2492ingL[0]['buy_price'])
    #print(v2492ing)

    contracts = [api.Contracts.Stocks['3669']]
    v3669ingL = api.snapshots(contracts)
    v3669ing=str(v3669ingL[0]['buy_price'])
    #print(v3669ing)

    #
    str1='網家:8044 成本= '+vd8044+"現價= "+v8044ing+'損益: '+vdc8044
    str2='圓展:3669 成本= '+vd3669+"現價= "+v3669ing+'損益: '+vdc3669
    str3='華新科:2492 成本= '+vd2492+"現價= "+v2492ing+'損益: '+vdc2492
    
    print(str1)
    print(str2)
    print(str3)
    
    print('總損益 ',sum)
    


    ###
    if '1' in msg:
        message = TextSendMessage(text=str1)
        line_bot_api.reply_message(event.reply_token, message)

    elif '2' in msg:
        message = TextSendMessage(text=str2)
        line_bot_api.reply_message(event.reply_token, message)

    elif '3' in msg:
        message = TextSendMessage(text=str3)
        line_bot_api.reply_message(event.reply_token, message)

    ###
    elif '最新合作廠商' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)



    ###
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)







import os
import requests

if __name__ == "__main__":

    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    
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
