from django.shortcuts import render
from weixin.client import WeixinMpAPI
from weixin import WXAPPAPI
import json

# Create your views here.
from django.http import HttpResponse
 
def calculate(request):
    formula = request.GET['formula']
    try:
        result = eval(formula, {})
    except:
        result = 'Error formula'
    return HttpResponse(result)

def test(request):
    return HttpResponse('1111')

def callback(request):
    signature = request.GET.get("signature")  # 先获取加密签名
    timestamp = request.GET.get('timestamp')  # 获取时间戳
    nonce = request.GET.get("nonce")  # 获取随机数
    echostr = request.GET.get("echostr") 
    #自己的token
    
    token="1234321" #这里改写你在微信公众平台里输入的token
    weixin_mpapi = WeixinMpAPI(mp_token=token,
        timestamp = timestamp,
        nonce = nonce,
        signature = signature,
        echostr = echostr)
    res = weixin_mpapi.validate_signature()
    if res:
        return HttpResponse(echostr)
    else:
        return HttpResponse('error')
def login(request):
    # import pdb; pdb.set_trace();
    # 公众号
    APP_ID = 'wxa93029123ef08e87'
    APP_SECRET ='8c86aad83e423dc3db51029fda540a2e'
    template_id ='ZAHkVP5O8kxlaz6YP8Jhe3oRJ8zcxWl7d5L1keezGCo'
    # TOKEN = '1234321'
    # openid:  oETC86S05vMthgRaI9val3LzefIs
    api = WeixinMpAPI(appid=APP_ID,app_secret=APP_SECRET,grant_type="client_credential")
    token = api.client_credential_for_access_token().get("access_token")
    par =  {
    "touser": "oETC86S05vMthgRaI9val3LzefIs",
    "template_id": template_id,
    "url":"http://weixin.qq.com/download",
    "page": "mp.weixin.qq.com",
    "data": {
        "name1": {
            "value": "111"
        } }
    }
    api = WeixinMpAPI(access_token=token)
    api.template_message_send(json_body=par)
    return HttpResponse("success")

def login_small(request):
    try:
        # 小程序
        from weixin.lib.wxcrypt import WXBizDataCrypt
        APP_ID = 'wxe811980bab3d2a89'
        APP_SECRET ='c8fef74bc890fd8fb50ddf88e47b1c1b'
        code = request.GET.get('code')
        iv = request.GET.get('iv')
        encrypted_data = request.GET.get('encrypted_data')
        print(f'code: {code}')
        print(f'iv: {iv}')
        print(f'encrypted_data: {encrypted_data}')
        api = WXAPPAPI(appid=APP_ID,
                        app_secret=APP_SECRET)
        import pdb; pdb.set_trace();
        session_info = api.exchange_code_for_session_key(code=code)
        session_key = session_info.get('session_key')
        # import pdb; pdb.set_trace();
        crypt = WXBizDataCrypt(APP_ID, session_key)
        # iv = 'PHrja/axkBl6xDFuVcZEZg=='
        # encrypted_data = 'uD6qKMhwjJ9Uu4EKqJ+OOn+Ce5JKkIG4HL3E4QG/afB5JnccDRu03RgFvg3TbiB2ehgNRZN94ZsX7PReDGM8ZuzXC8qt4jsbG6HI9wFBV4/sCd3STysf03AtrGu7Kj9HY+yi+U/tTd/p4UAnpyCWB/6BQIAsVmQk7UJ52MKmuy5l8gp3415zTARG6IzOn/oUs68/wKC0SnHHJ38QLr1W3Q=='
        user_info = crypt.decrypt(encrypted_data, iv)
        # print(f'user_info: {user_info}')
        # return HttpResponse(user_info,safe=False)
        import json
        return HttpResponse(json.dumps(user_info))
    except Exception as e:
        return HttpResponse(e.description)


def create_menu(request):
    try:
        # 公众号
        APP_ID = 'wxa93029123ef08e87'
        APP_SECRET ='8c86aad83e423dc3db51029fda540a2e'
        params = {
            "button": [
                {
                    "name": "菜单".encode('utf-8').decode("latin1"), 
                    "sub_button": [
                        {
                            "type": "view",  #菜单的响应动作类型，view表示网页类型，click表示点击类型，miniprogram表示小程序类型
                            "name": "搜索".encode('utf-8').decode("latin1"), 
                            "url": "http://www.soso.com/"
                        },
                        # {
                        #     "type":"miniprogram",
                        #     "name":"wxa",
                        #     "url":"http://mp.weixin.qq.com",
                        #     "appid":"wx286b93c14bbf93aa", #小程序的appid（仅认证公众号可配置）
                        #     "pagepath":"pages/lunar/index" #小程序的页面路径
                        # },
                    ]
                }
            ]
        }
        api = WeixinMpAPI(appid=APP_ID,app_secret=APP_SECRET,grant_type="client_credential")
        token = api.client_credential_for_access_token().get("access_token")
        api = WeixinMpAPI(access_token=token)
        res = api.create_menu(json_body=params)
        return HttpResponse(res["errmsg"])
    except Exception as e:
        return HttpResponse(e.description)
        

def callback_user(request):
    # import pdb; pdb.set_trace();
    # 公众号
    APP_ID = 'wxa93029123ef08e87'
    APP_SECRET ='8c86aad83e423dc3db51029fda540a2e'
    template_id ='ZAHkVP5O8kxlaz6YP8Jhe3oRJ8zcxWl7d5L1keezGCo'
    # TODO 
    # TOKEN = '1234321'
    # openid:  oETC86S05vMthgRaI9val3LzefIs
    REDIRECT_URI  = "http://"
    api = WeixinMpAPI(appid=APP_ID,app_secret=APP_SECRET,grant_type="client_credential",redirect_uri=REDIRECT_URI)
    token = api.client_credential_for_access_token().get("access_token")
    par =  {
    "touser": "oETC86S05vMthgRaI9val3LzefIs",
    "template_id": template_id,
    "url":"http://weixin.qq.com/download",
    "page": "mp.weixin.qq.com",
    "data": {
        "name1": {
            "value": "111"
        } }
    }
    api = WeixinMpAPI(access_token=token)
    api.template_message_send(json_body=par)
    return HttpResponse("success")
