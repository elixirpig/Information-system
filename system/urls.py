from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^catalog_list$', views.catalog_list, name='catalog_list'),
    url(r'^supply_list/$', views.supply_list, name='supply_list'),
    url(r'^provider_list$', views.provider_list, name='provider_list'),
    url(r'^manufacturer_list$', views.manufacturer_list, name='manufacturer_list'),
    url(r'^groups_list$', views.groups_list, name='groups_list'),
    url(r'^new_product$', views.new_product, name='new_product'),
    url(r'^new_supply$', views.new_supply, name='new_supply'),
    url(r'^new_provider$', views.new_provider, name='new_provider'),
    url(r'^new_manufacturer$', views.new_manufacturer, name='new_manufacturer'),
    url(r'^new_group$', views.new_group, name='new_group'),
    url(r'^about$', views.about_system, name='about_system'),

]
