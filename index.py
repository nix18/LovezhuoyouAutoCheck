# coding = utf-8
import requests
import sys
import io
import logging
from user import user
from urllib import request
from urllib.parse import quote

logger = logging.getLogger()
logger.setLevel(logging.INFO)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

usr0 = user(cookie_str="", plus_key="")

def pushMsg(url):
    req = request.Request(url)
    # 设置请求头
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 '
                   'Safari/537.36')
    resp = request.urlopen(req)
    print("推送消息请求已发出")
    logger.info("推送消息请求已发出")


def main_handler(event, context):
    host = "https://www.lovezhuoyou.com"
    endpoint = r"/wp-admin/admin-ajax.php"

    url = ''.join([host, endpoint])
    headers = \
        {
            "Host": "www.lovezhuoyou.com",
            "Connection": "keep-alive",
            "Content-Length": "19",
            "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"97\", \"Chromium\";v=\"97\"",
            "DNT": "1",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept": "*/*",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-platform": "\"Windows\"",
            "Origin": "https://www.lovezhuoyou.com/",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://www.lovezhuoyou.com/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6,de;q=0.5",
            "Cookie": usr0.cookie_str
        }
    body = "action=user_qiandao"
    r = requests.post(url, headers=headers, data=body)

    pushUrl = "http://www.pushplus.plus/send/" + usr0.plus_key + "?title=" + quote("爱桌游自动签到", 'utf-8') + "&content="
    msg = "【{}】 {}".format(r.json()["status"],r.json()["msg"])
    logger.info(msg)
    print(msg)
    msg = quote(msg, 'utf-8')
    pushMsg(pushUrl + msg)

    logger.info("签到完成" if r.status_code == 200 else "签到失败，HTTP错误码：" + str(r.status_code))
    print("签到完成" if r.status_code == 200 else "签到失败，HTTP错误码：" + str(r.status_code))
