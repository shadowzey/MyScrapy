#coding:utf-8

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import MovieItem

class LongbuluoSpider(CrawlSpider):
    name = 'LongBuLuo'
    allowed_domains = ['longbl.com']
    start_urls = [
        'http://www.longbl.com/tag/dzp/',
        'http://www.longbl.com/tag/xjp/',
        'http://www.longbl.com/tag/kbp/',
        'http://www.longbl.com/tag/khp/',
        'http://www.longbl.com/tag/aqp/',
        'http://www.longbl.com/tag/jqp/',
        'http://www.longbl.com/tag/zzp/',
        'http://www.longbl.com/tag/dhp/',
        'http://www.longbl.com/tag/mxp/',
        'http://www.longbl.com/tag/gfp/',
        'http://www.longbl.com/tag/xyp/',
        'http://www.longbl.com/tag/jsp/',
        'http://www.longbl.com/tag/lzp/',
        'http://www.longbl.com/tag/fzp/',
        'http://www.longbl.com/tag/lsp/',
        'http://www.longbl.com/tag/ssp/',
        'http://www.longbl.com/tag/zjp/',
        'http://www.longbl.com/tag/gzp/',
        'http://www.longbl.com/tag/qhp/',
        'http://www.longbl.com/tag/hxp/',
        'http://www.longbl.com/tag/gwp/',
        'http://www.longbl.com/tag/wxp/',
        'http://www.longbl.com/tag/znp/',
        'http://www.longbl.com/tag/smp/',
        'http://www.longbl.com/tag/xbp/',
        'http://www.longbl.com/tag/jfp/',
        'http://www.longbl.com/tag/jtp/',
        'http://www.longbl.com/tag/hsp/',
        'http://www.longbl.com/tag/ydp/',
        'http://www.longbl.com/tag/jlp/',
        'http://www.longbl.com/tag/yyp/',
        'http://www.longbl.com/tag/gfdy/',
    ]
    
    rules = (
        Rule(LinkExtractor(allow=('www.longbl.com/tag/.*/page/\d+/'), restrict_xpaths=('//div[@class="pagebar"]/a[last()]'))),
        Rule(LinkExtractor(allow=('www.longbl.com/(?:movie|television|dongman|video)/\d+\.html')), callback='parse_item')
    )

    def parse_item(self, response):
        item = MovieItem()
        item['website'] = u'龙部落'
        item['description'] = response.xpath('//div[@class="post"]/h2/text()').extract_first()
        item['link'] = repr(response.xpath('//a[contains(@href, "ed2k") or contains(@href, "thunder") or contains(@href, "ftp") or contains(@href, "magnet")]/@href').extract())
        return item
