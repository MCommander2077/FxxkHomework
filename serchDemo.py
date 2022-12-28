# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import base64
import hashlib
import reload
import time

reload.reload(sys)

YOUDAO_URL = 'https://openapi.youdao.com/ocrquestionapi'
APP_KEY = '00707d0b58ba61ea'
APP_SECRET = 'MGkrD3LmqVpAr0yevvK4WNepCTvoOGgC'


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def connect():
    f = open(r'C:\Users\MadYang\PycharmProjects\pythonProject2\搜题\第二个小题题.png', 'rb')  # 二进制方式打开图文件
    q = base64.b64encode(f.read()).decode('utf-8')  # 读取文件内容，转换为base64编码
    f.close()

    data = {}
    data['q'] = q
    data['signType'] = 'v2'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['salt'] = salt
    data['sign'] = sign

    response = do_request(data)
    print(response.content)


if __name__ == '__main__':
    connect()