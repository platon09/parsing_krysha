from django.db import models

# Create your models here.
class Apartments(models.Model):
	name = models.CharField(
		max_length=64,
		verbose_name = "Заголовок",
		)
	price = models.CharField(
		max_length=128,
		verbose_name='Цена'
		)
	location = models.CharField(
		max_length=64,
		verbose_name='Адрес'
		)
	url = models.URLField(
		verbose_name='Ссылка на объявление'
		)

	class Meta:
		verbose_name = 'Квартира'
		verbose_name_plural = 'Квартиры'