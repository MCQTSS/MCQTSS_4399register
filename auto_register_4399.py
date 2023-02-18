import time
import traceback

import requests
import random
import linecache
import re
import ddddocr


class gethttpproxies:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 ('
                          'KHTML, like Gecko) Mobile/17D50 UCBrowser/12.8.2.1268 Mobile AliApp(TUnionSDK/0.1.20.3) '
        }

    def main(self):
        for i in range(5):
            html = requests.get('https://ip.jiangxianli.com/?page={}&country=%E4%B8%AD%E5%9B%BD'.format(i),
                                verify=False).text
            list_ip = re.findall('<td>(.*?)</td>', html)  # 匹配所有IP,端口,地区延迟之类的
            for j in range(len(list_ip)):
                if re.match(
                        '^([1-9]|([1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))(\.([0-9]|([1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))){3}$',
                        list_ip[j]):  # 匹配是不是IP
                    print("获取代理IP " + list_ip[j] + ':' + list_ip[j + 1])
                    fh = open("IP.txt", "a+")
                    fh.write(list_ip[j] + ':' + list_ip[j + 1] + '\n')
                    fh.close()


def random_ip(file):  # 在一个文本中取随机一行
    txt = open(file, 'rb')
    data = txt.read().decode('utf-8')
    txt.close()
    n = data.count('\n')
    i = random.randint(1, (n + 1))
    line = linecache.getline(file, i)
    return line.replace('\n', '')


def MCQTSS_qzjwb(text, start_str, end):  # 取出字符串中间文本
    start = text.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = text.find(end, start)
        if end >= 0:
            return text[start:end].strip()


def register_4399(username, password, yzm_4399=False):  # 4399注册
    try:
        while True:
            sfz = random_ip('sfz.txt')  # 随机身份证
            if len(sfz.split('----')[1]) == 18 and len(sfz.split('----')[0]) in [2, 3]:
                break
            else:
                print('身份证:{}异常'.format(sfz))
        sessionId = 'captchaReq' + ''.join(random.sample(alphabet, 19))  # 获取一个随机的sessionId
        proxies = {
            'http': 'http://' + random_ip("IP.txt")
        }  # 获取一个随机代理,如果你注册的很慢可以检查一下自己代理的质量
        if proxies['http'] == 'http://':
            proxies = {}
        print("代理:{}".format(proxies))
        if yzm_4399 is True:  # 判断是否需要验证码
            # 如果需要本地识别(容易炸内存,发起3k个线程32g直接跑满)
            ocr = ddddocr.DdddOcr(use_gpu=True, device_id=0, show_ad=False)
            yzm_data = ocr.classification(
                requests.get(url='https://ptlogin.4399.com/ptlogin/captcha.do?captchaId={}'.format(sessionId),
                             headers=IP.headers, proxies=proxies).content)  # 获取sessionId对应的验证码图片
            if len(yzm_data) < 4:
                yzm_data = yzm_data + ''.join(random.sample(alphabet, 4 - len(yzm_data)))
        else:
            # 如果不需要验证码识别直接给4个随机数
            yzm_data = ''.join(random.sample(alphabet, 4))
        post = {'postLoginHandler': 'default',
                'displayMode': 'popup',
                'appId': 'www_home',
                'gameId': '',
                'cid': '',
                'externalLogin': 'qq',
                'aid': '',
                'ref': '',
                'css': '',
                'redirectUrl': '',
                'regMode': 'reg_normal',
                'sessionId': sessionId,  # 上面给的验证码ID部分
                'regIdcard': 'true',
                'noEmail': 'false',
                'crossDomainIFrame': '',
                'crossDomainUrl': '',
                'mainDivId': 'popup_reg_div',
                'showRegInfo': 'true',
                'includeFcmInfo': 'false',
                'expandFcmInput': 'false',
                'fcmFakeValidate': 'true',
                'username': username,
                'password': password,
                'passwordveri': password,
                'email': '{}@qq.com'.format('mcqtss' + ''.join(random.sample(alphabet, 5))),  # 邮箱,可以随便写
                'inputCaptcha': yzm_data,  # 验证码填写处
                'reg_eula_agree': 'on',
                'realname': sfz.split('----')[0],  # 身份证姓名
                'idcard': sfz.split('----')[1]}  # 身份证号码
        html = requests.post(url='https://ptlogin.4399.com/ptlogin/register.do',
                             data=post,
                             proxies=proxies,
                             timeout=5,
                             headers=IP.headers).text
        # print(MCQTSS_qzjwb(html, '<div id="Msg" class="login_hor login_err_tip">', '</div>'))
        # 去掉上面这行注释打印全部错误信息
        if html.find('身份证实名帐号数量超过限制') != -1:
            print('身份证实名帐号数量超过限制')
            return '身份证实名帐号数量超过限制'
        elif html.find('身份证实名过于频繁') != -1:
            print('身份证实名过于频繁')
            return '身份证实名过于频繁'
        elif html.find('该姓名身份证提交验证过于频繁') != -1:
            print('该姓名身份证提交验证过于频繁')
            return '该姓名身份证提交验证过于频繁'
        elif html.find('验证码错误') != -1:
            register_4399(username, password, True)
            return '验证码错误'
        elif html.find('用户名已被注册') != -1:
            print('用户名已被注册')
            return '用户名已被注册'
        elif html.find('HTTP ERROR 500') != -1:
            print('HTTP ERROR 500')
            return 'HTTP ERROR 500'
        elif html.find('注册成功') != -1:
            print('注册成功 {}----{}'.format(username, password))
            fh = open('4399.txt', 'a+')
            fh.write('{}----{}\n'.format(username, password))
            fh.close()
            print("身份证:{}".format(sfz))
            return '注册成功 {}----{}'.format(username, password)
        elif html.find("503 Service Temporarily Unavailable") != -1:
            print('503 Service Temporarily Unavailable')
        else:
            print(html)
            return html
    except:
        traceback.print_exc()
        return 'Error'


if __name__ == "__main__":
    alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'  # 随机字符串包含的字符
    yzm = False
    IP = gethttpproxies()
    IP.main()
    # 如果有代理IP去掉这个注释
    while True:
        register_4399(''.join(random.sample(alphabet, 7)), ''.join(random.sample(alphabet, 10)))
        time.sleep(0.5)
