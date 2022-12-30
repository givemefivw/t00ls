import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def pushplus(text, msg):
    url = 'http://www.pushplus.plus/send'
    data = {
        "token":'',
        "title":text,
        "content":msg,
        "template": "markdown"
        }
    body=json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type':'application/json'}
    requests.post(url,data=body,headers=headers)


header = {
    'Host': 'www.t00ls.com',
    'Cookie': '',
    'Content-Length': '34',
    'Sec-Ch-Ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4433.0 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Origin': 'https://www.t00ls.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'close',
}

data = ''
try:
    res = requests.post(url='https://www.t00ls.com/ajax-sign.json',headers=header,data=data,verify=False)
    if 'success' in res.text:
        print('签到成功!',res.text)
        pushplus(text='T00ls签到程序提醒!',msg=res.text)
    if 'alreadysign' in res.text:
        print('今日已签到!',res.text)
        pushplus(text='T00ls签到程序提醒!',msg=res.text)
except Exception as e:
    print('签到失败,错误原因: ',e)
    pushplus(text='T00ls签到异常提醒!',msg=e)
