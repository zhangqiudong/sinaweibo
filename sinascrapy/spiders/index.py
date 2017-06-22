import scrapy
import json
from sinascrapy.settings import USERNAME, PASSWORD
import requests

class WeiboSpider(scrapy.Spider):

    name = 'weibo'
    start_urls = [
        'https://passport.weibo.cn/signin/login',
    ]

    def parse(self, response):
        return scrapy.FormRequest.from_response(response,
                                                formdata={'username':USERNAME,'password':PASSWORD},
                                                callback=self.after_login,
                                                method='post',
                                                url='https://passport.weibo.cn/signin/login')

    def after_login(self, response):
        for i in range(5):
            print requests.get("https://m.weibo.cn/feed/friends?version=v4&next_cursor=4121474463650326&page=1").content
             # yield scrapy.Request('https://m.weibo.cn/feed/friends?version=v4&next_cursor=4121474463650326&page=%s' % (i + 1), self.home)

    def home(self, response):
        objs = json.loads(response.body)
        obj = objs[0]
        for item in obj["card_group"]:
            print(item['mblog']["text"])