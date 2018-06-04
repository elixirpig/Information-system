from django.contrib import admin
from .models import Groups, Catalog, Manufacturer, Supply, Provider

admin.site.register(Groups)

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'manufacturer', 'price', 'groups_products')
    list_per_page = 10
    list_filter = ("name_product",)
    preserve_filters = False
    search_fields = ('name_product',)
admin.site.register(Catalog, CatalogAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name_manufacturer', 'country')
    list_per_page = 10
    list_filter = ("name_manufacturer",)
    search_fields = ('name_manufacturer', 'country')
    preserve_filters = False
admin.site.register(Manufacturer, ManufacturerAdmin)

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name_provider', 'phone', 'street', 'number_street')
    list_per_page = 10
    list_filter = ("name_provider",)
    search_fields = ('name_provider', )
    preserve_filters = False
admin.site.register(Provider, ProviderAdmin)

class SupplyAdmin(admin.ModelAdmin):
    list_display = ('date_of_supply', 'provider', 'products', 'quantity', 'price')
    list_per_page = 10
    list_filter = ("date_of_supply", "provider")
    search_fields = ('products', )
    preserve_filters = False
admin.site.register(Supply, SupplyAdmin)