from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.catalog_list, name='catalog_list'),
    url(r'^supply_list/$', views.supply_list, name='supply_list'),
    url(r'^provider_list$', views.provider_list, name='provider_list'),
    url(r'^new_product$', views.new_product, name='new_product'),
]
