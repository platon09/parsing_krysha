import scrapy

from parser_app.models import Apartments

class KryshaBot(scrapy.Spider):
	name = "krysha"

	start_urls = ['https://krisha.kz/prodazha/kvartiry/karaganda/?das[live.rooms]=5.100']

	def parse(self, response) -> item:
		temp = "https://krisha.kz"

		for apartment in response.css("div.a-card__header"):
			
			item = Apartments.objects.create(name=apartment.css("a.a-card__title::text").get(),
				price=apartment.css("div.a-card__price::text").get(),
				location=apartment.css("div.a-card__subtitle::text").get(),
				url=temp + apartment.css("div.a-card__header-left a.a-card__title::attr(href)").get())
			
			yield item

		for href in response.css("a.paginator__btn--next::attr(href)"):
			yield response.follow(href, callback=self.parse)
