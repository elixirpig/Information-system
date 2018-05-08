from django import forms
from .models import Catalog

class CatalogForm(forms.ModelForm):

    class Meta:
        model = Catalog
        fields = ('name_product', 'manufacturer', 'price',  'groups_products')

