from django.contrib import admin

from .forms import ApartmentsForm
from .models import Apartments


class ApartmentsAdmin(admin.ModelAdmin):
	list_display = {'name', 'price', 'location', 'url'} 
	form = ApartmentsForm

admin.site.register(Apartments)