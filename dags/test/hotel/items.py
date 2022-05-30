import scrapy
from scrapy.loader.processors import  TakeFirst

class QuotesSpiderItem(scrapy.Item):
    hotel_name = scrapy.Field(output_processor=TakeFirst())
    hotel_rating = scrapy.Field(output_processor=TakeFirst())
    hotel_address = scrapy.Field(output_processor=TakeFirst())
    hotel_point_review = scrapy.Field(output_processor=TakeFirst())
    hotel_sum_review = scrapy.Field(output_processor=TakeFirst())
    hotel_url = scrapy.Field(output_processor=TakeFirst())
