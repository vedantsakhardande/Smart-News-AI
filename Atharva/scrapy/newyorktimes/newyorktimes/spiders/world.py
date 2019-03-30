# -*- coding: utf-8 -*-
import scrapy


class WorldSpider(scrapy.Spider):
    name = 'world'
    allowed_domains = ['https://www.nytimes.com/']
    start_urls = ['http://https://www.nytimes.com//']

    def parse(self, response):
        pass

import scrapy


class WorldSpider(scrapy.Spider):
    name = 'world'
    allowed_domains = ['https://www.nytimes.com']
    start_urls = ['https://www.nytimes.com/section/world']


    def parse(self, response):

        print("procesing:"+response.url)
        #Extract data using css selectors
        product_name=response.css('.product::text').extract()
        price_range=response.css('.value::text').extract()
        #Extract data using xpath
        orders=response.xpath("//em[@title='Total Orders']/text()").extract()
        company_name=response.xpath("//a[@class='store $p4pLog']/text()").extract()

        row_data=zip(product_name,price_range,orders,company_name)

        #Making extracted data row wise
        for item in row_data:
            #create a dictionary to store the scraped info
            scraped_info = {
                #key:value
                'page':response.url,
                'product_name' : item[0], #item[0] means product in the list and so on, index tells what value to assign
                'price_range' : item[1],
                'orders' : item[2],
                'company_name' : item[3],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info