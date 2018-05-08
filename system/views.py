from django.shortcuts import render
from .models import Catalog, Supply, Provider


def catalog_list(request):
    catalogs = Catalog.objects.all()
    return render(request, "catalog_list.html", locals())

# Create your views here.
def supply_list(request):
    supplys = Supply.objects.all()
    return render(request, "supply_list.html", locals())

def provider_list(request):
    providers = Provider.objects.all()
    return render(request, "provider_list.html", locals())