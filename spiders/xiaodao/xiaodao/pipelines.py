# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class XiaodaoPipeline:
    def process_item(self, item, spider):
        return item
class CVSPipeline:
    index = 0
    file = None

    def open_spider(self,spider):
        print('打开文件')
        self.file = open('home.csv', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        print('打开文件出路数据')
        if self.index == 0:
            column_name = 'title, tag, url, baidu, baidu_code, tianyi, tianyi_code\n'
            self.file.write(column_name)
            self.index = 1

        home_str = item['title'] + "," +\
                    item['tag']+", " +\
                    item['url']+", " +\
                    item['baidu']+", " +\
                    item['baidu_code']+", " +\
                    item['tianyi']+", " +\
                    item['tianyi_code']+"\n"    
        self.file.write(home_str)
        return item
    def close_spider(self, spider):
        self.file.close()

