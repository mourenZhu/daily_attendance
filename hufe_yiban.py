from attendance import Attendance
import time
import requests

import os
from bs4 import BeautifulSoup as bs

username = os.getenv('HUFE_USERNAME')
password = os.getenv('HUFE_PASSWORD')
phone = os.getenv('PHONE')

data = {
    'dkdz': "湖南省长沙市岳麓区咸嘉湖街道学仕路湖南财政经济学院",
    "dkdzZb": "112.939,28.2287",
    'dkly': "lbs",
    "zzdk_token": "",
    "dkd": "湖南省长沙市",
    "jzdValue": "430000,430100,430104",
    "jzdSheng.dm": "430000",
    'jzdShi.dm': '430100',
    'jzdXian.dm': '430104',
    'jzdDz': "湖南财政经济学院",
    'jzdDz2': "湖南财政经济学院",
    'lxdh': phone,
    'sfzx': '1',
    'sfzx1': "在校",
    'twM.dm': "01",
    'tw1': "[35.0~37.2]正常",
    'yczk.dm': "01",
    'yczk1': "无症状",
    'fbrq': '',
    'jzInd': '0',
    'jzYy': "",
    'zdjg': "",
    'fxrq': "",
    'brStzk.dm': "01",
    'brStzk1': "身体健康、无异常",
    'brJccry.dm': "01",
    'brJccry1': "未接触传染源",
    'jrStzk.dm': "01",
    'jrStzk1': "身体健康、无异常",
    'jrJccry.dm': '01',
    'jrJccry1': "未接触传染源",
    'jkm': "1",
    'jkm1': "绿色",
    'xcm': "1",
    'xcm1': "绿色",
    'xgym': "",
    'xgym1': "",
    'hsjc': "",
    'hsjc1': '',
    'bz': '',
    'operationType': "Create",
    'dm': ""
}

cookies = {}

base_url = "https://xsgz.hufe.edu.cn"
login_url = base_url + "/website/login"
post_url = base_url + "/content/student/temp/zzdk?_t_s_="
token_url = base_url + "/wap/menu/student/temp/zzdk/_child_/edit"
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
    "Origin": "https://xsgz.hufe.edu.cn",
    'Host': 'xsgz.hufe.edu.cn',
    'sec-ch-ua-platform': "Android",
    'sec-ch-ua-mobile': '?1',
    'Sec-Fetch-Mode': 'cors',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}


def get_ts():
    now = time.time()
    return str(int(round(now * 1000)))


def get_md5_pw(pw):
    import hashlib
    md5 = hashlib.md5()
    md5.update(pw.encode('latin1'))
    pw_md5 = md5.hexdigest()
    if len(pw_md5) > 5:
        pw_md5 = pw_md5[0:5] + "a" + pw_md5[5:len(pw_md5)]
    if len(pw_md5) > 10:
        pw_md5 = pw_md5[0:10] + "b" + pw_md5[10:len(pw_md5)]
    pw_md5 = pw_md5[0:len(pw_md5) - 2]
    return pw_md5


def set_data_token():
    url = token_url + "?_t_s=" + get_ts()
    # print("token url = " + url)
    res = requests.get(url, headers=headers, cookies=cookies)
    html = res.text
    html = bs(html, 'html.parser')
    data['zzdk_token'] = html.find('input', id='zzdk_token')["value"]


def login():
    print("开始获取token")
    print("username = " + username + " password = " + password)
    up_data = {
        "uname": username,
        "pd_mm": get_md5_pw(password)
    }
    print(up_data)
    res = requests.post(login_url, data=up_data, headers=headers)
    if res.json().get('error'):
        print(res.json()['msg'])
        exit(401)
    jsession_id = res.cookies.get('JSESSIONID')
    # print(jsession_id)
    # print(res.text)
    cookies['JSESSIONID'] = jsession_id
    # 这个不加也没事
    # headers['Set-Cookie'] = 'JSESSIONID=' + jsession_id
    set_data_token()


def start():
    login()
    url = post_url + get_ts()
    # print("url = " + url)
    res = requests.post(url, cookies=cookies, data=data, headers=headers)
    print(res.text)


class HufeYiban(Attendance):
    def attendance(self):
        pass
        # is_time_out = True
        # attendance_num = 0
        # while is_time_out:
        #     attendance_num = attendance_num + 1
        #     print("开始第" + str(attendance_num) + "次打卡！")
        #     try:
        #         start()
        #         cookies.clear()
        #         is_time_out = False
        #     except (BaseException, ConnectionError, TimeoutError):
        #         print("连接超时超时，等待10s")
        #         time.sleep(10)
