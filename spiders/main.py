import scrapy
import time
import json
import pymysql
import re
from biquge.items import BiqugeItem,Book_content_Item
headers = {
    'Host':'www.qu.la',
    'Referer':'http:/www.qu.la/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}
class biquge_spider(scrapy.Spider):
    name = "biquge"
    start_urls = ["http://www.qu.la"]

    def parse(self,response):
        book_url = "http://www.qu.la/book/{}/"
        book_id = 4567
        # for book_id in range(3952,3953):
        # for book_id in range(0,47900):
            # print("第---%d---页" % book_id)
        yield scrapy.http.Request(url=book_url.format(book_id),headers=headers,callback=self.parse_book_index)
    def parse_book_index(self,response):
        # print(response.body.decode('utf-8'))
        item = BiqugeItem()
        item['name'] = response.css('div#info h1::text')[0].extract()
        print(item['name'])
        item['author'] = response.css('div#info p::text')[0].extract()
        item['brief'] = ''.join(response.css('div#intro::text').extract())
        item['update_chapter'] = response.css('div#info p a::text')[-1].extract()
        # print(type(item['brief']))
        # with open('1111.txt','w',encoding='utf-8') as f:
        #     f.write(item['brief'])
        # print(item)
        book_chapter_url_list = response.css('div#list dd a::attr(href)').extract()
        for book_chapter_url in book_chapter_url_list :
    #         if book_chapter_url.startswith('//'):
    #             print(book_chapter_url)
    #             print('http:www.qu.la'+book_chapter_url)
    #             re.sub(r'//','/',book_chapter_url)
            yield scrapy.http.Request(url=''.join(['http://www.qu.la',book_chapter_url]),headers=headers,callback=self.parse_book_content)
        return item
    def parse_book_content(self,response):
    #     print('成功')
        content_item = Book_content_Item()
        content_item['book_name'] = response.css('div.con_top a::attr(title)')[-1].extract()
        content_item['chapter_name'] = response.css('div.bookname h1::text')[0].extract()
        content_item['content'] = ''.join(response.css('div#content::text')[0:-2].extract())
        print(type(content_item['content']))
        return content_item

