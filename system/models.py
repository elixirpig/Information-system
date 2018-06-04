from django.utils import timezone
from django.db import models


class Provider(models.Model):
    class Meta:
        db_table = "provider"
    name_provider = models.CharField('Поставщик',max_length= 200)
    phone = models.IntegerField('Телефон')
    street = models.CharField('Улица', max_length= 64)
    number_street = models.IntegerField('Номер')

    def __str__(self):
        return self.name_provider


class Groups(models.Model):
    class Meta:
        db_table = "groups_products"
    groups_products = models.CharField('Группа товара', max_length= 200)

    def __str__(self):
        return self.groups_products

class Manufacturer(models.Model):
    class Meta:
        db_table = "manufacturer"
    name_manufacturer = models.CharField('Производитель', max_length= 200)
    country = models.CharField('Страна', max_length= 64)

    def __str__(self):
        return self.name_manufacturer

class Supply(models.Model):
    class Meta:
        db_table = "supply"
    date_of_supply = models.DateTimeField('Дата', default= timezone.now)
    quantity = models.IntegerField('Количество')
    price = models.FloatField('Цена')
    provider = models.ForeignKey(Provider, verbose_name='Поставщик')
    products = models.CharField('Продукт', max_length=200)


class Catalog(models.Model):
    class Meta:
        db_table = "catalog"
    name_product = models.CharField('Название', max_length= 200)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name='Производитель')
    price = models.FloatField('Цена')
    groups_products = models.ForeignKey(Groups, verbose_name='Группа товара')

    def __str__(self):
        return self.name_product






