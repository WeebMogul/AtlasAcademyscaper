# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst

class AtlasacademyscaperItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
   # jp_name = scrapy.Field(output_processor=TakeFirst())
    svt_class = scrapy.Field(output_processor=TakeFirst())
    rarity = scrapy.Field(output_processor=TakeFirst())
    cost = scrapy.Field(output_processor=TakeFirst())
    lvlMax = scrapy.Field(output_processor=TakeFirst())
    
