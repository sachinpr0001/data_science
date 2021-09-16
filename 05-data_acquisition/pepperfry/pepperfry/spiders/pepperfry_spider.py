import scrapy
import re
import os
import requests
import json

# USER_AGENT = 'Chrome/77.0.3865.90' in settings.py

class PepperFry(scrapy.Spider):
    name = "pepperfry_spider"
    BASE_DIR = "./pepperfry_data/"
    MAX_CNT = 20

    def start_requests(self):
        # base url of the website
        BASE_URL = "https://www.pepperfry.com/site_product/search?q="

        # used to search a specific item
        items = ["two seater sofa", "bench", "book cases", "coffee table", "dining set", "queen beds", "arm chairs", "chest drawers", "garden seating", "bean bags", "king beds"]

        urls = []
        dir_names = []

        for item in items:
            query_string = '+'.join(item.split(' '))
            dir_name = '-'.join(item.split(' '))
            dir_names.append(dir_name)
            urls.append(BASE_URL + query_string)
            # store directory names and urls the items

            dir_path = self.BASE_DIR + dir_name
            # name the directory

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            # if the directory does not exist, then create it
            

        #print(self.urls)
        # traverse all the urls
        for i in range(len(urls)):
            d = {
                "dir_name": dir_names[i]
            }
            # d gets the directory where current url things need to be saved

            resp = scrapy.Request(url = urls[i], callback = self.parse, dont_filter = True)
            resp.meta['dir_name'] = dir_names[i]
            yield resp
    
    def parse(self, response, **meta):
        product_urls = response.xpath('//div/div/div/a[@p=0]/@href').extract()
        # get the url of the specific item of the product searched above

        counter = 0

        #print(product_urls)

        for url in product_urls:
            resp = scrapy.Request(url = url, callback = self.parse_item, dont_filter = True)
            resp.meta['dir_name'] = response.meta['dir_name']

            if counter == self.MAX_CNT:
                break

            if not resp == None:
                counter += 1

            yield resp

    def parse_item(self, response, **meta):
        item_title = response.xpath('//div/div/div/h1/text()').extract()[0]
        item_price = response.xpath('//div/div/div/p/b[@class="pf-orange-color pf-large font-20 pf-primary-color"]/text()').extract()[0].strip()
        item_savings = response.xpath('//p[@class="pf-margin-0 pf-bold-txt font-13"]/text()').extract()[0].strip()
        item_description = response.xpath('//div[@itemprop="description"]/div/p/text()').extract()
        item_detail_keys = response.xpath('//div[@id="itemDetail"]/p/b/text()').extract()

        item_detail_values = response.xpath('//div[@id="itemDetail"]/p/text()').extract()

        brand = response.xpath('//span[@itemprop="brand"]/text()').extract()
        item_detail_values[0] = brand[0]
        stop_words = ["(all dimensions in inches)","(all dimensions in inches","(all dimensions in inches"]
        item_detail_values = [word.strip() for word in item_detail_values if word not in stop_words] 
        
        a = len(item_detail_keys)
        b = len(item_detail_values)
        idetail = {}

        for i in range(min(a,b)):
            idetail[item_detail_keys[i]] = item_detail_values[i]

        stop_items = ["pepperfry.com", "We also offer you a","So go ahead and buy with confidence.","Brand will upfront contact you for assembly"]
        item_description = filter(lambda x: all([not y.lower() in x.lower()
        for y in stop_items]), item_description)
        item_description = '\n'.join(item_description)
        image_url_list = response.xpath('//li[@class="vip-options-slideeach"]/a@data-img').extract()

        if(len(image_url_list)>3):
            d = {
            'Item Title': item_title,
            'description': item_description,
            'Item Price': item_price,
            'Savings': item_savings,
            'Details': idetail
            }


            # create another directory for a particular type of searched product
            CATEGORY_NAME = response.meta['dir_name']
            ITEM_DIR_URL = os.path.join(self.BASE_DIR, os.path.join(CATEGORY_NAME, item_title))


            if not os.path.exists(ITEM_DIR_URL):
                os.makedirs(ITEM_DIR_URL)

            # save directory in json format as metadata.txt
            with open(os.path.join(ITEM_DIR_URL, 'metadata.txt'), "w") as f:
                json.dump(d, f)

            # travel all the image urls and save the images as jpg
            for i, img_url in enumerate(img_url_list):
                r = requests.get(img_url)
                with open(os.path.join(ITEM_DIR_URL, 'image_{}.jpg'.format(i)), 'wb') as f:
                    f.write(r.content)

            print("--> Successfully saved \""+item_title+"\" data at :"+ITEM_DIR_URL)    
            yield d
        yield None
