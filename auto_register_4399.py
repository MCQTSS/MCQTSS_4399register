import threading
import time
import requests
import random
import linecache
import re
import ddddocr


class gethttpproxies:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/17D50 UCBrowser/12.8.2.1268 Mobile AliApp(TUnionSDK/0.1.20.3)'
        }

    def main(self):
        for i in range(5):
            html = requests.get('https://ip.jiangxianli.com/?page={}&country=%E4%B8%AD%E5%9B%BD'.format(i)).text
            list_ip = re.findall('<td>(.*?)</td>', html)
            for j in range(len(list_ip)):
                if re.match(
                        '^([1-9]|([1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))(\.([0-9]|([1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))){3}$',
                        list_ip[j]):
                    print("获取代理IP " + list_ip[j] + ':' + list_ip[j + 1])
                    fh = open("IP.txt", "a+")
                    fh.write(list_ip[j] + ':' + list_ip[j + 1] + '\n')
                    fh.close()


def random_ip(file):
    txt = open(file, 'rb')
    data = txt.read().decode('utf-8')
    txt.close()
    n = data.count('\n')
    i = random.randint(1, (n + 1))
    line = linecache.getline(file, i)
    return line


def MCQTSS_qzjwb(text, start_str, end):
    start = text.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = text.find(end, start)
        if end >= 0:
            return text[start:end].strip()


def register_4399(username, password, yzm=False):
    try:
        sfz = random_ip('sfz.txt')
        sessionId = 'captchaReq' + ''.join(random.sample(alphabet, 19))
        proxies = {
            'http': 'http://' + random_ip("IP.txt")
        }
        if yzm is True:
            ocr = ddddocr.DdddOcr(use_gpu=True, device_id=0)
            yzm_data = ocr.classification(
                requests.get(url='http://ptlogin.4399.com/ptlogin/captcha.do?captchaId={}'.format(sessionId),
                             proxies=proxies, headers=IP.headers).content)
            if len(yzm_data) != 4:
                yzm_data = yzm_data + ''.join(random.sample(alphabet, 4 - len(yzm_data)))
        else:
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
                'sessionId': sessionId,
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
                'email': '{}@qq.com'.format('mcqtss' + ''.join(random.sample(alphabet, 5))),
                'inputCaptcha': yzm_data,
                'reg_eula_agree': 'on',
                'realname': MCQTSS_qzjwb(sfz, '', '----'),
                'idcard': MCQTSS_qzjwb(sfz + ':qtss', '----', ':qtss')}
        html = requests.post(url='http://ptlogin.4399.com/ptlogin/register.do',
                             data=post,
                             proxies=proxies,
                             timeout=5,
                             headers=IP.headers).text
        if html.find('身份证实名帐号数量超过限制') != -1:
            print('身份证实名帐号数量超过限制  ', sfz)
            return '身份证实名帐号数量超过限制'
        elif html.find('验证码错误') != -1:
            register_4399(username, password, True)
            return '验证码错误'
        elif html.find('注册成功') != -1:
            print('注册成功 {}----{}'.format(username, password))
            fh = open('4399.txt', 'a+')
            fh.write('{}----{}\n'.format(username, password))
            fh.close()
            return '注册成功 {}----{}'.format(username, password)
        else:
            return html
    except:
        return 'Error'


if __name__ == "__main__":
    alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'
    yzm = False
    IP = gethttpproxies()
    # IP.main()
    # print(register_4399('MCQTSS_' + ''.join(random.sample(alphabet, 5)), ''.join(random.sample(alphabet, 8))))
    while True:
        for i in range(3000):
            threading.Thread(target=register_4399,
                             kwargs={'username': 'MCQTSS_' + ''.join(random.sample(alphabet, 5)),
                                     'password': ''.join(random.sample(alphabet, 8))}).start()
            # threading.Thread(target=reg).start()
        print('开始休眠600秒后继续发起')
        time.sleep(600)
