from django.shortcuts import render
from .models import Catalog


def catalog_list(request):
    catalogs = Catalog.objects.all()
    return render(request, "system/base.html", locals())

# Create your views here.
