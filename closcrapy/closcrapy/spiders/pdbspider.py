# -*- coding: utf-8 -*-
import scrapy
from scrapy import log
from closcrapy.items import PdbItem


class PdbspiderSpider(scrapy.Spider):
    name = "pdbspider"
    allowed_domains = ["17pdb.com"]
    start_urls = (
        'http://www.17pdb.com/',
    )

    def parse(self, response):
        sel = response.selector.xpath(
            '//div[@id="main"]/div[contains(@class,"poste")]')
        for index, item in enumerate(sel):
            title = item.xpath('.//h2/a/text()').extract()
            link = item.xpath('.//h2/a/@href').extract()
            catalog = item.xpath('.//p/a/text()').extract()
            pdbitem = PdbItem(title=title, link=link, catalog=catalog)
            yield pdbitem
