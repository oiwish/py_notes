# -*- encoding: utf-8 -*-
import json

import scrapy as scrapy


class essaySpider(scrapy.Spider):

    name = 'essay'
    # allow_domain = 'acfun.cn'
    start_url = 'http://www.acfun.cn/list/getlist?channelId=197&sort=0&pageSize=20&pageNo=%s'

    def start_requests(self):
        i = 1
        for i in range(1, 10):
            url = self.start_url % i
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        file = open('test.txt' + response.url.split('=')[-1], 'wb')
        data = json.loads(response.body)

        for d in data['data']['data']:
            a = d['videoId']+d['title']
            print(a)
            file.write(self, a)
