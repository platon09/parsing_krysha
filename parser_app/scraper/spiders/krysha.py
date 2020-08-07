import scrapy

from parsing_krysha.parser_app.models import Apartments

class KryshaBot(scrapy.Spider):
	name = "krysha"

	start_urls = ['https://krisha.kz/prodazha/kvartiry/karaganda/?das[live.rooms]=5.100']

	def parse(self, response):
		temp = "https://krisha.kz"
		item = Apartments()

		for apartment in response.css("div.a-card__header"):
			
			item['name'] = apartment.css("a.a-card__title::text").get(),
			item['price'] = apartment.css("div.a-card__price::text").get(),
			item['location'] = apartment.css("div.a-card__subtitle::text").get(),
			item['url'] = temp + apartment.css("div.a-card__header-left a::attr(href)").get()

			yield item

		for href in response.css("a.paginator__btn--next::attr(href)"):
			yield response.follow(href, callback=self.parse)
