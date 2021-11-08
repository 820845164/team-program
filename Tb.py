import json
from encodings import unicode_escape

import requests
import re
import urllib.request
import time

import xlrd
from bs4 import BeautifulSoup
import bs4
# requests获取url的html代码信息
import requests
import random


# 爬取的是淘宝网的书包，爬取价格和商品名称
# headers是登录搜索书包后复制了search文件中的user-agent和cookie
def getHtml(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
        'cookie': '_samesite_flag_=true; cookie2=1b808fb9524c70b2bd8f4d145a1ee4b6; t=bb63505d365ff069865cb7b9573b5e7a; _tb_token_=0e438f03e37e; cna=NrTRGWvx/UQCAXWIS/SNmCDB; xlly_s=1; sgcookie=E100OmZDhbxpQ0O6EniyA/ltXMtOSo3ySDf/6S7pbiPdXk+FxmTqLKn2csnSktuvSzLg6xVKd1k80K59GdX3j9l0p8QGd22XQpzcO5NJjL1DIB0=; unb=2206746303967; uc3=id2=UUphzOV1+duyw2pjaw==&lg2=UtASsssmOIJ0bQ==&nk2=F5RCYrtyy7Pc4w==&vt3=F8dCujdyOKg/swzriRA=; csg=db280683; lgc=tb77180794; cancelledSubSites=empty; cookie17=UUphzOV1+duyw2pjaw==; dnk=tb77180794; skt=6e6e317909008c2f; existShop=MTYzMjI5MDM5MQ==; uc4=nk4=0@FY4JjC8oJA7zDSZZlSbcPAT/jm5h&id4=0@U2grF866Yrx7jBvupg7yFxSgqAnc385D; tracknick=tb77180794; _cc_=U+GCWk/7og==; _l_g_=Ug==; sg=474; _nk_=tb77180794; cookie1=BdXcAWnRzxrn5g2f7DHA2UDsk8+8YP8cNNbWKu+1ncs=; enc=vP4gxYVvdXtoe6QPN4ExL8t0Sbdr1SHpclpnKktYvBpksn6j+j7r3HsZJocA8vDNZwO52Mmd1tur9oIi5rssG2tKpRBoUHrvxjWzj0nS7+E=; hng=CN|zh-CN|CNY|156; thw=cn; mt=ci=5_1; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA==&existShop=false&cookie21=V32FPkk/gPzW&cookie14=Uoe3dYNQ1AK3Nw==&pas=0&cookie15=UIHiLt3xD8xYTw==; JSESSIONID=9B02DC25A3E39CB391CE53DA594DEF26; isg=BAsLXoqn7phFyzLMqw8bTpegmq_1oB8iYwOwQH0I58qhnCv-BXCvcqk-dpxyp3ca; l=eBESH6LqgRojJEO9BOfanurza77OSIRYYuPzaNbMiOCPOwfB5rAfW6FNai86C3GVh6AvR35okuQ6BeYBqQAonxv92j-la_kmn; tfstk=cDj5BwNHdbc7ok4E4TwqT6sb8IxdwiP6nPdRFwixOVY6oC1DWcR1JMCqiFeHh', }

    # print(ua.random)
    r = requests.get(url, headers=header, timeout=120)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text


# def getHTMLTextUrllib(url):
#     try:
#         header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
#                    'cookie':'_samesite_flag_=true; cookie2=1b808fb9524c70b2bd8f4d145a1ee4b6; t=bb63505d365ff069865cb7b9573b5e7a; _tb_token_=0e438f03e37e; cna=NrTRGWvx/UQCAXWIS/SNmCDB; xlly_s=1; sgcookie=E100OmZDhbxpQ0O6EniyA/ltXMtOSo3ySDf/6S7pbiPdXk+FxmTqLKn2csnSktuvSzLg6xVKd1k80K59GdX3j9l0p8QGd22XQpzcO5NJjL1DIB0=; unb=2206746303967; uc3=id2=UUphzOV1+duyw2pjaw==&lg2=UtASsssmOIJ0bQ==&nk2=F5RCYrtyy7Pc4w==&vt3=F8dCujdyOKg/swzriRA=; csg=db280683; lgc=tb77180794; cancelledSubSites=empty; cookie17=UUphzOV1+duyw2pjaw==; dnk=tb77180794; skt=6e6e317909008c2f; existShop=MTYzMjI5MDM5MQ==; uc4=nk4=0@FY4JjC8oJA7zDSZZlSbcPAT/jm5h&id4=0@U2grF866Yrx7jBvupg7yFxSgqAnc385D; tracknick=tb77180794; _cc_=U+GCWk/7og==; _l_g_=Ug==; sg=474; _nk_=tb77180794; cookie1=BdXcAWnRzxrn5g2f7DHA2UDsk8+8YP8cNNbWKu+1ncs=; enc=vP4gxYVvdXtoe6QPN4ExL8t0Sbdr1SHpclpnKktYvBpksn6j+j7r3HsZJocA8vDNZwO52Mmd1tur9oIi5rssG2tKpRBoUHrvxjWzj0nS7+E=; hng=CN|zh-CN|CNY|156; thw=cn; mt=ci=5_1; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA==&existShop=false&cookie21=V32FPkk/gPzW&cookie14=Uoe3dYNQ1AK3Nw==&pas=0&cookie15=UIHiLt3xD8xYTw==; JSESSIONID=9B02DC25A3E39CB391CE53DA594DEF26; isg=BAsLXoqn7phFyzLMqw8bTpegmq_1oB8iYwOwQH0I58qhnCv-BXCvcqk-dpxyp3ca; l=eBESH6LqgRojJEO9BOfanurza77OSIRYYuPzaNbMiOCPOwfB5rAfW6FNai86C3GVh6AvR35okuQ6BeYBqQAonxv92j-la_kmn; tfstk=cDj5BwNHdbc7ok4E4TwqT6sb8IxdwiP6nPdRFwixOVY6oC1DWcR1JMCqiFeHh',}
#         req=urllib.request.Request(url,headers=header)
#         resp=urllib.request.urlopen(req)
#         data =resp.read()
#         unicodeData =data.decode()
#         #dammit = UnicodeDammit(data,["utf-8","gbk"])
#         #unicodeData= dammit.unicode_markup
#         return unicodeData
#     except:
#         return ""[\d\.]*
def getdata(html):
    # print("{:4}\t{:8}\t{:16}\t{:4}\t{:16}\t{:16}".format("序号","价格","商品名称","商店","商品链接","图片链接"))
    price = re.findall('"view_price":"([\d\.]*)"', html)  # [\d\.]匹配数字或小数点
    title = re.findall('"raw_title":"(.*?)"', html)  # 加问号懒惰匹配，匹配到第一个"就结束了
    shop = re.findall('"nick":"(.*?)"', html)
    link = re.findall('"detail_url":"(.*?)"', html)
    pic = re.findall('"pic_url":"(.*?)"', html)
    b = []
    # print(link)
    for i in link:
        a = "https:" + str(i)
        s = a.replace("\\u003d", "=").replace("\\u0026", "&")
        b.append(s)
    #
    for i in range(len(pic)):
        if pic[i].startswith('http'):
            pic[i] = pic[i].split('\\u')[0]
        else:
            pic[i] = "http:" + str(pic[i])
    # print(pic)
    # price2 =price.strip()
    # print(len(price))
    # print(price)
    # print(title)
    # print(len(title))
    # print(shop)
    # print(len(shop))
    # print(link)
    # print((len(link)))
    # print(pic)
    # print(len(pic))

    pic2 = []
    pic3 = []
    for i in range(len(price)):
        print(price[i])
        print(title[i])
        print(shop[i])
        print(b[i])
        print(pic[i])

        dict = {'type': '淘宝', 'drugTitle': title[i], 'price': price[i], 'originUrl': b[i], 'seller': shop[i],
                'cover': pic[i], 'specification': 'null'}
        with open('tb.txt', 'a', encoding='utf-8') as f:
            json.dump(dict, f, ensure_ascii=False, indent=1)
        # print(pic[i].split('\\u')[0])


if __name__ == '__main__':
    w = 9295
    num = 2
    wb = xlrd.open_workbook('C:/Users/ChenBenYuan/Desktop/yao.xlsx')  # 打开Excel文件
    sheet = wb.sheet_by_name('Sheet1')  # 通过excel表格名称(rank)获取工作表
    dat = []  # 创建空list
    for a in range(sheet.nrows):  # 循环读取表格内容（每次读取一行数据）
        cells = sheet.row_values(a)  # 每行数据赋值给cells
        data = cells[0]  # 因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
        dat.append(data)  # 把每次循环读取的数据插入到list
    for j in range(len(dat)):
        print(w)
        url = "https://s.taobao.com/search?q=" + dat[w] + "&page=1"
        w += 1
        # if num < 4:
        #     # print(i)
        #     link_nextpage = "https://s.taobao.com/search?q="+dat[i]+"&page=" + str(num)
        #     num += 2
        #     url = response.urljoin(link_nextpage)
        #     yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
        # else:
        #     i += 1
        #     num = 1
        #     link_nextpage = "https://s.taobao.com/search?q="+dat[i]+"&page=" + str(num)
        #     num += 2
        #     print(i)
        #     url = response.urljoin(link_nextpage)
        #     yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
        # with open(r'C:/Users/ChenBenYuan/Desktop/taobao.txt',encoding='utf-8') as f:
        #     html = f.read()
        # print(html)
        html = getHtml(url)
        # time.sleep(3)
        # print(html)
        getdata(html)