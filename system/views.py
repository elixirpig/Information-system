from django.shortcuts import render, redirect
from .models import Catalog, Supply, Provider
from .forms import CatalogForm


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

def new_product(request):
    if request.method == "POST":
        form = CatalogForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('catalog_list')
    else:
        form = CatalogForm()
    return render(request, 'new_product.html', {'form': form})