from django import forms
from .models import Catalog, Supply, Provider, Manufacturer, Groups


class CatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ('name_product', 'manufacturer', 'price', 'groups_products')


class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ('quantity', 'price', 'provider', 'products')

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ('name_provider', 'phone', 'street', 'number_street')

class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ('name_manufacturer', 'country')

class GroupsForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ('groups_products',)