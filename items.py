# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqugeItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    author = scrapy.Field()
    brief = scrapy.Field()
    update_chapter = scrapy.Field()
    pass
class Book_content_Item(scrapy.Item):
    book_name = scrapy.Field()
    chapter_name= scrapy.Field()
    content = scrapy.Field()
    pass

