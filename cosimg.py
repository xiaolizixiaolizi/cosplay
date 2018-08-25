# -*- coding: utf-8 -*-
import scrapy
import  re
from ..items import  CoserItem
class CosimgSpider(scrapy.Spider):
    name = 'cosimg'
    allowed_domains = ['bcy.net']
    start_urls = ['https://bcy.net/coser']

    def start_requests(self):
        base_url='https://bcy.net/circle/timeline/showtag?since=25881.{}&grid_type=flow&sort=hot&tag_id=399'
        num_list=[515,558,469,427]
        urls=list(map(lambda x:base_url.format(str(x)),num_list))
        for url in urls:
            request=scrapy.Request(
                url=url,
                callback=self.parse_list,
            )
            yield  request
            # break


    def parse_list(self, response):
        lis=response.xpath('//li[@class="js-smallCards _box"]')
        for  li in lis:
            img_link=li.xpath('./a/@href').get()
            img_link=response.urljoin(img_link)
            title=li.xpath('./a/@title').get()
            title=re.sub(r"[_ˉ-]",'',title)
            request=scrapy.Request(
                url=img_link,
                callback=self.parse_detail,
                meta={"info":(title)}

            )
            yield  request
            # break
    def parse_detail(self,response):
        title=response.meta.get('info')
        image_urls=response.xpath('//img[contains(@class,"detail_clickable")]/@src').getall()
        image_urls=list(map(lambda x:re.sub(r"/w650",'',x),image_urls))
        item=CoserItem(title=title,image_urls=image_urls)
        yield  item





