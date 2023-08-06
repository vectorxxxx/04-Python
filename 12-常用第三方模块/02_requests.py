import requests

# get请求
r = requests.get('https://www.douban.com/search', headers={
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'
}, params={'q': 'python', 'cat': '1001'})
print(r.url, r.encoding)
print(r.content)

URL = 'https://restapi.amap.com/v3/weather/weatherInfo?key=a4238a61f892a6692453252cef687735&city=320582&extensions=all&output=json'
r = requests.get(URL)
print(r.json())

r = requests.get("https://www.douban.com/", headers={
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'
})
print(r.status_code, r.text, r.headers)

# post
r = requests.post('https://accounts.douban.com/login', data= {
    'form_email': 'abc@example.com',
    'form_password': '123456'
})
print(r.status_code, r.text)