# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

import xlrd
from itemadapter import ItemAdapter

import csv





class DemoPipeline:

    def process_item(self, item, spider):
        dict = {"title":item['title'], "type":item['type'], "specification":item['specification'],"supplyPrice":item['supplyPrice'],"retailPrice":item['retailPrice'],"manufactures":item['manufactures']}
        global flag
        print(item["title"])
        print(item["type"])
        print(item["specification"])
        print(item["supplyPrice"])
        print(item["retailPrice"])
        print(item["manufactures"])
        with open('yao3.txt', 'a', encoding='utf-8') as f:
            if item['title'] != "":
                json.dump(dict, f, ensure_ascii=False,indent=1)
                f.close()


        return item
