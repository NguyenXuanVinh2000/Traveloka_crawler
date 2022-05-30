# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy import Spider
from scrapy.loader import ItemLoader
from hotel.items import QuotesSpiderItem
import scrapy
from hotel.check_DB import *
import logging

class QuotesSpider(Spider):


    global domain
    domain = 'https://www.traveloka.com'

    name = 'hotel'
    start_urls = ['https://www.traveloka.com/vi-vn/hotel/']

    def parse(self, response):

        for item_url in response.xpath('//*[@id="__next"]/div[10]/div/div[2]/a/@href').extract():
            url = domain+item_url
            yield scrapy.Request(url, callback=self.parse_urls) 

    def parse_urls(self, response):
        for item_url in response.xpath('//*[@id="__next"]/div[4]/div[5]/div/div[1]/div/div[3]/div/div[1]/div/div/a/@href').extract():
            url = domain + item_url
            yield scrapy.Request(url, callback=self.parse_hotel) 

    def parse_hotel(self, response):
        lst_hotel_name = response.xpath('//*[@id="__next"]/div[4]/div[5]/div/div[3]/div/div/div/div/div/div/div[1]/h3/text()').extract()
        lst_hotel_address = response.xpath('//*[@id="__next"]/div[4]/div[5]/div/div[3]/div/div/div/div/div/div/div[1]/div[4]/div[2]/text()').extract()
        lst_hotel_rating = response.xpath('//*[@id="__next"]/div[4]/div[5]/div/div[3]/div/div/div/div/div/div/div[1]/div[2]/div[3]/meta/@content').extract()
        lst_hotel_sum_review = []
        
        for sum_review in response.xpath('//*[@id="__next"]/div[4]/div[5]/div/div[3]/div/div/div/div/div/div/div[1]/div[6]/div[4]/text()').extract():
            if sum_review!=' ':
                sum_review = str(sum_review)
                sum_review = sum_review.replace('(','')
                sum_review = sum_review.replace(')','')
                lst_hotel_sum_review.append(sum_review)
        
        
        lst_hotel_point_review = []
        for point in response.xpath('//*[@id="__next"]/div[4]/div[5]/div/div[3]/div/div/div/div/div/div/div[1]/div[6]/div[3]/text()').extract():
            if point!=' ':
                lst_hotel_point_review.append(point)

        lst_hotel_urls = response.xpath('//*[@id="__next"]/div[4]/div[5]/div/div[3]/div/div/div/div/div/div/div[2]/div/div/a/@href').extract()

        for name, address, url, point_review, sum_reviews, rating in zip(lst_hotel_name, lst_hotel_address, lst_hotel_urls, lst_hotel_point_review, lst_hotel_sum_review, lst_hotel_rating):
            if check_data(name):
                logging.info("[!] DATA already exists !!")
            else:
                item = ItemLoader(QuotesSpiderItem())
                item.add_value('hotel_name', name)
                item.add_value('hotel_rating', rating)
                item.add_value('hotel_address', address)
                item.add_value('hotel_point_review', point_review)
                item.add_value('hotel_sum_review', sum_reviews)
                item.add_value('hotel_url', domain+url)
                yield item.load_item()
                