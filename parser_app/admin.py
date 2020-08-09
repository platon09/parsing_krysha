from django.contrib import admin

from .forms import ApartmentsForm
from .models import Apartments


class ApartmentsAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Apartments._meta.fields]
	form = ApartmentsForm

admin.site.register(Apartments, ApartmentsAdmin)