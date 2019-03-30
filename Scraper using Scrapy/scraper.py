import scrapy
import numpy as np
class BrickSetSpider(scrapy.Spider):

    name = "brickset_spider"
    start_urls = ['https://www.amazon.in/s?node=1968123031']
    def parse(self, response):
        SET_SELECTOR = '.aok-block'
        count1 = 0
        count2=0
        for brickset in response.css(SET_SELECTOR):
            tshirts1 = [];
            count1+=1
            NAME_SELECTOR = 'a ::attr(title)'
            HREF_SELECTOR = 'a ::attr(href)'
            SRC_SELECTOR = 'img ::attr(data-src)'
           
            tshirts1.append({
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'href':'https://www.amazon.in' +  brickset.css(HREF_SELECTOR).extract_first(),
                'src': brickset.css(SRC_SELECTOR).extract_first()

            })
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'href':'https://www.amazon.in' +  brickset.css(HREF_SELECTOR).extract_first(),
                'src': brickset.css(SRC_SELECTOR).extract_first()

            }
        SET_SELECTOR = '.acs_product-price__buying'
        for brickset in response.css(SET_SELECTOR):
            tshirts2 = []
            count2+=1
            PRICE_SELECTOR = 'span ::text'
           
            str = brickset.css(PRICE_SELECTOR).extract_first()
            tshirts2.append({
                
                'price': ' ' +  str[0] +   str[2] +  str[3] + str[4] + str[5] + str[6] + str[7]

            }
            )
            yield {
                
                'price': ' ' +  str[0] +   str[2] +  str[3] + str[4] + str[5] + str[6] + str[7]

            }
        result = np.concatenate((tshirts1,tshirts2), axis=0)
        print(result)
            
        