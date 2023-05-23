import requests
import socket

# auto login
url = 'xxx.xxx.edu.cn.php' # your school's web login site

data = {
    'action': 'login',
    'ac_id': '1',
    'username': 'your student id here...',
    'password': 'your password here...'
    
}

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'xxx.xxx.edu.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'
}

response = requests.post(url=url, data=data, headers=header)
print("status code:", response.status_code)

# test connection to Baidu
s = socket.socket()
s.settimeout(3)
status = s.connect_ex(('www.baidu.com', 443))
if status == 0:
    s.close()
    print('Successfully reached https://www.baidu.com')
else:
    print('Network Connection Error')
