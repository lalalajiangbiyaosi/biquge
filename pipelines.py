# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from biquge.items import BiqugeItem,Book_content_Item
import pymysql
class BiqugePipeline(object):

    def process_item(self, item, spider):
        if isinstance(item,BiqugeItem):
            try:
                try:
                    db = pymysql.connect("39.106.36.143","root","root","biquge_book",use_unicode=True, charset="utf8")
                except:
                    print('连接数据库错误！')
                finally:
                    cursor = db.cursor()
                    try:
                        cursor.execute('insert into book_index(name,author,brief,update_chapter) values(%s, %s, %s, %s)' , (item['name'],item['author'],item['brief'],item['update_chapter']))
                    except:
                        pass
            except Exception as e:
                print("输出数据库错误！",e)
            finally:
               db.commit()
               db.close()
            # with open(item['name']+'.txt','w',encoding='utf-8') as f :
            #     f.write(item['author'])
            #     f.write(item['brief'])
        elif isinstance(item,Book_content_Item):
            try:
                db = pymysql.connect("39.106.36.143", "root", "root", "biquge_book", use_unicode=True, charset="utf8")
                try:
                    cursor = db.cursor()
                    cursor.execute('insert into book_chapter_content(book_name,chapter_name,chapter_content) values(%s, %s, %s)' , (item['book_name'],item['chapter_name'],item['content']))
                except Exception as e :
                    print('输出数据库错误！',e)
                finally:
                    db.commit()
                    db.close()
            except Exception as e:
                print("连接数据库失败",e)
        return item

