# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime


NEWS_ITEM_DATETIME_FIELDNAME = 'article_datetime'
NEWS_ITEM_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


class NewsPipeline:
    def process_item(self, item, spider):
        # clean string values if the items
        for key, value in item.items():
            if isinstance(value, str):
                item[key] = value.strip()
        # cast datetime string to object
        if item[NEWS_ITEM_DATETIME_FIELDNAME]:
            datetime_str = item[NEWS_ITEM_DATETIME_FIELDNAME]
            datetime_obj = datetime.strptime(
                datetime_str, NEWS_ITEM_DATETIME_FORMAT)
            item[NEWS_ITEM_DATETIME_FIELDNAME] = datetime_obj
        return item
