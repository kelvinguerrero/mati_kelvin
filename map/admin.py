from django.contrib import admin

# Register your models here.
from.models import Pensum

class PensumAdmin(admin.ModelAdmin):
    class Meta:
        model = Pensum

admin.site.register(Pensum,PensumAdmin)