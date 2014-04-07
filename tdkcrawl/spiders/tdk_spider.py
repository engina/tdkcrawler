# -*- coding: utf8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from urlparse import urlparse, parse_qs, urlunparse
from urllib import quote_plus, unquote_plus
from lxml import html
import string

class TdkSpider(Spider):
    name = "tdk"
    allowed_domains = ["tdk.gov.tr"]
    alphabet        = string.lowercase
    start_urls      = []

    '''
    ı : %C4%B1
    ç : %C3%A7
    ö : %C3%B6
    ü : %C3%BC
    ş : %C5%9F
   '''
    for i in range(len(alphabet)):
    	start_urls.append('http://tdk.gov.tr/index.php?option=com_seslissozluk&view=seslissozluk&kelime1='+alphabet[i]+'&kategori1=yazim_listeli&ayn1=bas&konts=0')

    for l in ['ı', 'ç', 'ö', 'ü', 'ş']:
    	start_urls.append('http://tdk.gov.tr/index.php?option=com_seslissozluk&view=seslissozluk&kelime1='+quote_plus(l)+'&kategori1=yazim_listeli&ayn1=bas&konts=0')

    def parsePages(self, response):
    	url_base = response.url[0:-1]
    	sel      = Selector(response)
    	pages    = sel.xpath("//select[@name='konts']/option[last()]/text()").extract()[0]
    	self.parseWords(response)
    	for i in range(1, int(pages)):
    		url = url_base + str(i*60)
    		yield Request(url, callback=self.parseWords)

    def parseWords(self, response):
    	url      = urlparse(response.url)
    	query    = parse_qs(url.query)
    	ch       = unquote_plus(query['kelime1'][0])
    	offset   = query['konts'][0]
    	sel      = Selector(response)
    	words    = sel.xpath('//p[@class="thomicb"]/a[last()]').extract()

    	filename = 'd/' + ch + '_' + offset.zfill(4) + '.txt'
    	file     = open(filename, 'wb+')

    	for w in words:
    		a = html.fromstring(w)
    		file.write(a.text_content().encode('utf_8'))
    		file.write('\n')
    	file.close()

    def parse(self, response):
    	return self.parsePages(response)