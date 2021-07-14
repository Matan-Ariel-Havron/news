# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ArticleItem(Item):
    # define the fields for your item here like:
    article_title = Field()
    article_sub_title = Field()
    article_author = Field()
    article_datetime = Field()
    article_link = Field()
    article_image_link = Field()
    article_image_alt = Field()
    article_spider_name = Field()
