#scrapy crawl amazon_spider
#

import scrapy
from ..items import AmazonscraperItem

class AmazonSpiderSpider(scrapy.Spider):
	name = 'amazon_spider'
	page_num = 2
	start_urls = ['https://www.amazon.in/s?k=timer+switch&rh=n%3A3704992031%2Cp_36%3A3444811031&dc&crid=1VCS8PRYH0CSK&qid=1600783091&rnid=3444809031&sprefix=timer+switch%2Cstripbooks%2C572&ref=sr_nr_p_36_2']

	def parse(self, response):
		items = AmazonscraperItem()
		product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
		product_price = response.css('.a-price-whole').css('::text').extract()
		product_geton = response.css('.s-align-children-center .a-text-bold').css('::text').extract()
		product_imglink = response.css('.s-image-fixed-height .s-image::attr(src)').extract()
		for item in items:
		items['product_name']= product_name
		items['product_price'] = product_price
		items['product_imglink'] = product_imglink
		items['product_geton'] = product_geton

		yield items
		next_page = 'https://www.amazon.in/s?k=timer+switch&i=home-improvement&rh=n%3A3704992031%2Cp_36%3A3444811031&dc&page='+ str(AmazonSpiderSpider.page_num)+'&crid=1VCS8PRYH0CSK&qid=1600842298&rnid=3444809031&sprefix=timer+switch%2Cstripbooks%2C572&ref=sr_pg_2'

		if AmazonSpiderSpider.page_num <= 10:
			AmazonSpiderSpider.page_num +=1
			yield response.follow(next_page,callback = self.parse)