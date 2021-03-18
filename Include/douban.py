# coding=utf-8
import  urllib
import urllib.request

from bs4 import  BeautifulSoup  #网页解析
import re
import xlwt
import  sqlite3
#bs.attrs   获取所有标签
def main():

      baseurl="https://movie.douban.com/top250?start="#基本的网页链接 爬取用、
      getData(baseurl)

                        # datalist=getData(baseurl)
                        # savepath=".\\豆瓣电影250.xls"
                         # saveData(savepath)


findLink=re.compile(r'<a href="(.*?)">')       #创建正则表达式对象 表示规则 字符串的模式  r忽略特殊符号  这里是匹配链接
findImgSrc=re.compile(r'<img.*src="(.*?)"',re.S) #忽略换行符
findTittle=re.compile(r'<span class="title">(.*)</span>')
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJuddge=re.compile(r'<span>(\d*)人评价</span>')
findInq=re.compile(r'<span class="inq">(.*)</span>')
findBd=re.compile(r'<p class="">(.*)</p>',re.S)

def getData(baseurl):
    datalist=[]  #用列表存放爬取到的数据
      #反复调用页面函数
    for i in range(0,1):
     url=baseurl+str(i*25)
     html=askURL(url)  #保存获取到的网页源码
     #print(html)
     soup=BeautifulSoup(html,"html.parser")
    for item in soup.find_all('div',class_="item"):
            #print(item)
            data=[]  #保存一部电影
            item=str(item)

            #link=re.findall(findLink,item)[0]
            imgsrc=re.findall(findImgSrc,item)[0]
            #print(link)
            print(imgsrc)




    return datalist
    #得到一个指定url的网页内容

def askURL(url):  #用户代理 告诉豆瓣服务器，是什么类型的机器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
        # 修改请求头文件

    }
    request=urllib.request.Request(url,headers=headers)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode('utf-8')
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html



def saveData(savepath):
    print()

if __name__ =="__main__":
    main()
    # getData("https://movie.douban.com/top250?start=")
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    #     # 修改请求头文件
    #
    # }
    # url3 = "https://www.bilibili.com"
    # url = "https://www.douban.com"
    # url2 = "http://httpnom.org/post"
    # req = urllib.request.Request(url=url3, headers=headers, )  # 修改请求头
    # response = urllib.request.urlopen(req);  # 将请求返回相应
    # print(response.read().decode('utf-8'))