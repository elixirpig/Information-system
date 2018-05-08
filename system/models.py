from django.utils import timezone

from django.db import models

# Create your models here.
class Provider(models.Model):
    class Meta:
        db_table = "provider"
    name_provider = models.CharField(max_length= 200)
    phone = models.IntegerField()
    street = models.CharField(max_length= 64)
    number_street = models.IntegerField()

    def __str__(self):
        return self.name_provider


class Groups(models.Model):
    class Meta:
        db_table = "groups_products"
    groups_products = models.CharField(max_length= 200)

    def __str__(self):
        return self.groups_products

class Manufacturer(models.Model):
    class Meta:
        db_table = "manufacturer"
    name_manufacturer = models.CharField(max_length= 200)
    country = models.CharField(max_length= 64)

    def __str__(self):
        return self.name_manufacturer

class Catalog(models.Model):
    class Meta:
        db_table = "catalog"
    name_product = models.CharField(max_length= 200)
    manufacturer = models.ForeignKey(Manufacturer)
    price = models.FloatField()
    groups_products = models.ForeignKey(Groups)

    def __str__(self):
        return self.name_product


class Supply(models.Model):
    class Meta:
        db_table = "supply"
    date_of_supply = models.DateTimeField(default= timezone.now)
    quantity = models.IntegerField()
    price = models.FloatField()
    provider = models.ForeignKey(Provider)
    products = models.ForeignKey(Catalog)

