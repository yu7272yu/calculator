[toc]

# 服务
## 启动服务：
python3 manage.py runserver 0.0.0.0:8000

## 测试微信账号

### 小程序和公众号账号
````
测试小程序：
https://developers.weixin.qq.com/sandbox?tab=miniprogram&hl=zh
小程序测试号信息
AppID wxe811980bab3d2a89
AppSecret c8fef74bc890fd8fb50ddf88e47b1c1b

测试公众号：
http://mp.weixin.qq.com/debug/cgi-bin/sandboxinfo?action=showinfo&t=sandbox/index
测试号信息
appID wxa93029123ef08e87
appsecret 8c86aad83e423dc3db51029fda540a2e

````

### 小程序配置
> 内网床头映射域名
````
花生壳搭建内网穿透：
https://console.oray.com/domain/others/?type=others

docker run -d --name mynginx -p 80:80 -p 443:443 nginx 
docker cp default.conf mynginx:/etc/nginx/conf.d/default.conf
docker restart mynginx

将域名配置到测试小程序中的可信域名中
配置 request 合法域名：     https://631u981e15.goho.co
````

### 微信公众号配置
> 安装包
````
pip install python-weixin
````
> 配置微信公众号
````
填写接口配置信息（测试账户中）
1.token
2.在服务端写入微信配置URL回调接口

URL https://631u981e15.goho.co/callback
Token 1234321
````
> 服务端回调get接口
````python
在urls中配置接口：
url('callback', views.callback)

方法：
def callback(request):
    from weixin.client import WeixinMpAPI
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
````

> 服务端获取公众号用户信息openID
````python
def login(request):
    from weixin.client import WeixinMpAPI
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
    "page": "mp.weixin.qq.com",
    "data": {
        "name1": {
            "value": "111"
        } }
    }
    api = WeixinMpAPI(access_token=token)
    api.template_message_send(json_body=par)

````

> 服务端接收小程序发送的用户code,获取用户手机号
````python
def login(request):
    
def login_small(request):
    # 小程序
    from weixin import WXAPPAPI
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
    session_info = api.exchange_code_for_session_key(code=code)
    session_key = session_info.get('session_key')
    crypt = WXBizDataCrypt(APP_ID, session_key)
    user_info = crypt.decrypt(encrypted_data, iv)
    import json
    return HttpResponse(json.dumps(user_info))


````

