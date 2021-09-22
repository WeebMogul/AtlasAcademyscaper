import scrapy
import json

from scrapy import loader
from AtlasAcademyscaper.items import AtlasacademyscaperItem
from scrapy.loader import ItemLoader

class FgoatlascademySpider(scrapy.Spider):
    name = 'fgoatlasacademy'
    allowed_domains = ['atlasacademy.io']
    start_urls = [f'https://api.atlasacademy.io/nice/NA/servant/{i}?lore=true&lang=en' for i in range(1,268)]

    def parse(self, response):
        
        l = ItemLoader(item=AtlasacademyscaperItem())
        data = json.loads(response.body)
        
        l.add_value('id',data['collectionNo'])
        l.add_value('name',data['name'])
       # l.add_value('jp_name',data['ruby'])
        l.add_value('svt_class',data['className'])
        l.add_value('rarity',data['rarity'])
        l.add_value('cost',data['cost'])
        l.add_value('lvlMax',data['lvMax'])

        yield l.load_item()


        
