from django.core.management.base import BaseCommand
from parser_app.scraper.spiders.krysha import KryshaBot
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class Command(BaseCommand):
	help = 'Parsing Krysha'
	
	def handle(self, *args, **options):
		process = CrawlerProcess(get_project_settings())
		process.crawl(KryshaBot)
		process.start()