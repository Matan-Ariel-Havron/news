from ..items import ArticleItem
from scrapy import Spider


class YnetSpider(Spider):
    name = 'ynet'
    start_urls = ['https://www.ynet.co.il/home/0,7340,L-8,00.html']
    TITLE_MIN_LENGTH = 2

    def parse(self, response):
        item = ArticleItem()

        slot_views = response.css('.slotView')  # .getall()

        for slot_view in slot_views:
            item['article_spider_name'] = self.name
            item['article_title'] = slot_view.css('.slotTitle *::text').get()
            item['article_sub_title'] = slot_view.css(
                '.slotSubTitle *::text').get()
            item['article_author'] = slot_view.css(
                'span .authorInfo::text').get()
            item['article_image_link'] = slot_view.css('img::attr(src)').get()
            item['article_image_alt'] = slot_view.css('img::attr(alt)').get()
            item['article_link'] = slot_view.css('a::attr(href)').get()
            item['article_datetime'] = slot_view.css(
                'span.DateDisplay::attr(data-wcmdate)').get()
            if item['article_link'] and item['article_link'].find('ynet.co.il') != -1:
                yield item
