from django.contrib import admin
from .models import Groups, Catalog,Manufacturer, Supply, Provider
# Register your models here.
admin.site.register(Groups)
admin.site.register(Catalog)
admin.site.register(Manufacturer)
admin.site.register(Supply)
admin.site.register(Provider)
