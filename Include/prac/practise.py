
import urllib
import  urllib.request
from bs4 import BeautifulSoup




#repose=urllib.request.urlopen("http://www.baidu.com")
# try:
#   response=urllib.request.urlopen("http://httpbin.org/get",)
# except urllib.error.URLError as  e:
#     print("timeout")
# response=urllib.request.urlopen("http://www.baidu.com/")
# print(response.getheaders())  #状态码
#print(repose.read().decode('utf-8'))

headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"   #修改请求头文件



}

# url3="https://www.bilibili.com"
url="https://movie.douban.com/top250?start="
# url2="http://httpnom.org/post"
# req=urllib.request.Request(url=url3, headers=headers, )                   #修改请求头
# response=urllib.request.urlopen(req);  #将请求返回相应
# print(response.read().decode('utf-8'))


requset=urllib.request.Request(url,headers=headers)
html =""
try:
    response=urllib.request.urlopen(requset)
    html=response.read().decode("utf-8")
    print(html)
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
