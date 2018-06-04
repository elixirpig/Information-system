from django.shortcuts import render, redirect
from .models import Catalog, Supply, Provider, Manufacturer, Groups
from .forms import CatalogForm, SupplyForm, ProviderForm, ManufacturerForm, GroupsForm


def home(request):
    return render(request, "home.html")

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

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, "manufacturer_list.html", locals())

def groups_list(request):
    groups = Groups.objects.all()
    return render(request, "groups_list.html", locals())

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

def new_supply(request):
    if request.method == "POST":
        form = SupplyForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('supply_list')
    else:
        form = SupplyForm()
    return render(request, "new_supply.html", {'form': form})

def new_provider(request):
    if request.method == "POST":
        form = ProviderForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('provider_list')
    else:
        form = ProviderForm()
    return render(request, "new_provider.html", {'form': form})

def new_manufacturer(request):
    if request.method == "POST":
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('manufacturer_list')

    else:
        form = ManufacturerForm()
    return render(request, "new_manufacturer.html", {'form': form})

def new_group(request):
    if request.method == "POST":
        form = GroupsForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('groups_list')

    else:
        form = GroupsForm()
    return render(request, "new_group.html", {'form': form})

def about_system(request):
    return render(request, 'about.html')


