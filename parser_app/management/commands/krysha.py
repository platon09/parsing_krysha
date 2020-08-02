import scrapy
from django.core.management.base import BaseCommand
#from parser_app.models import Apartments


class KryshaBot(scrapy.Spider):
	name = "krysha"

	start_urls = ['https://krisha.kz/prodazha/kvartiry/karaganda/?das[live.rooms]=5.100']

	def parse(self, response):
		temp = "https://krisha.kz"

		for apartment in response.css("div.a-card__header"):
			yield {
			'name': apartment.css("a.a-card__title::text").get(),
			'price': apartment.css("div.a-card__price::text").get(),
			'location': apartment.css("div.a-card__subtitle::text").get(),
			'link':	temp + apartment.css("div.a-card__header-left a::attr(href)").get()
			}
		for href in response.css("a.paginator__btn--next::attr(href)"):
			yield response.follow(href, callback=self.parse)

def main():
    p = KryshaBot()
    p.parse()


if __name__ == '__main__':
    main()