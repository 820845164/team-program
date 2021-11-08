import csv
import re
import sqlite3
import urllib

import bs4
from fake_useragent import UserAgent
from lxml import etree
import requests
import random
import scrapy
from demo.items import DemoItem
from bs4 import UnicodeDammit

import xlrd
count = 1
num = 2

wb = xlrd.open_workbook('C:/Users/ChenBenYuan/Desktop/yao.xlsx')  # 打开Excel文件
sheet = wb.sheet_by_name('Sheet1')  # 通过excel表格名称(rank)获取工作表
dat = []  # 创建空list
for a in range(sheet.nrows):  # 循环读取表格内容（每次读取一行数据）
    cells = sheet.row_values(a)  # 每行数据赋值给cells
    data = cells[0]  # 因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
    dat.append(data)  # 把每次循环读取的数据插入到list
# print(len(dat))
i = 13000
print(dat[13000])
# allow = input("请输入一个参数")
class myspides(scrapy.Spider):
    # 设定基础参数

    name = 'myspiders'
    # 爬虫名

    start_urls = ["http://www.china-yao.com/?act=search&typeid=1&keyword="+dat[i]+"&page=1"]

    # 泌尿系统类的药 cid3为一种类型的药的编号

    def parse(self, response):
            global i
            global dat
            global num
            global number
            global allow
            try:

                dammit = UnicodeDammit(response.body, ["utf-8", "gbk"])
                data = dammit.unicode_markup
                selector = scrapy.Selector(text=data)
                # 解析，xpath提取
                lis = selector.xpath("//tbody/tr")
                # print(lis)
                for li in lis:
                    # global count
                    # if count > allow:
                    #     break;

                    # else:
                        title = li.xpath("./td[position()=1]/text()").extract_first()
                        type = li.xpath("./td[position()=2]/text()").extract_first()
                        specification = li.xpath("./td[position()=3]/text()").extract_first()
                        supplyPrice = li.xpath("./td[position()=4]/text()").extract_first()
                        retailPrice = li.xpath("./td[position()=5]/text()").extract_first()
                        manufactures = li.xpath("./td[position()=6]/text()").extract_first()
                        item = DemoItem()
                        # print(count)
                        item["title"] = title if title != '暂无数据' else ""
                        item["type"] = type if type else ""
                        item["specification"] = specification if specification else ""
                        item["supplyPrice"] = supplyPrice.strip() if supplyPrice else ""
                        item["retailPrice"] = retailPrice.strip() if retailPrice else ""
                        item["manufactures"] = manufactures if manufactures else ""

                        yield item
                        # count +=1



                if num < 4 :
                    # print(i)
                    link_nextpage = "http://www.china-yao.com/?act=search&typeid=1&keyword="+dat[i]+"&page="+str(num)
                    num += 1
                    url = response.urljoin(link_nextpage)
                    yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
                else:
                    i += 1
                    num = 1
                    link_nextpage = "http://www.china-yao.com/?act=search&typeid=1&keyword=" + dat[i] + "&page=" + str(num)
                    num +=1
                    print(i)
                    url = response.urljoin(link_nextpage)
                    yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

            except Exception as err:
                    print(err)





