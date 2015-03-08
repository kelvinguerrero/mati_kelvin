from django.contrib import admin

# Register your models here.
from.models import Pensum, Map


class PensumAdmin(admin.ModelAdmin):
    class Meta:
        model = Pensum


class MapAdmin(admin.ModelAdmin):
    class Meta:
        model = Map

admin.site.register(Pensum, PensumAdmin)
admin.site.register(Map, MapAdmin)