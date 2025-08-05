from django.db import models

# Create your models here.

class Service(models.Model):
    nr = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=100, unique=True)
    feature1 = models.CharField(max_length=100)
    feature1_range = models.CharField(max_length=100)
    feature2 = models.CharField(max_length=100)
    feature2_range = models.CharField(max_length=100)
    demand = models.CharField(max_length=50)
    demand_coeff = models.DecimalField(max_digits=4, decimal_places=2)
    local_supply = models.CharField(max_length=50)
    supply_coeff = models.DecimalField(max_digits=4, decimal_places=2)
    market_price = models.CharField(max_length=50)
    price_coeff = models.DecimalField(max_digits=4, decimal_places=2)
    price_min = models.DecimalField(max_digits=10, decimal_places=2)
    price_max = models.DecimalField(max_digits=10, decimal_places=2)
    local_price_min = models.DecimalField(max_digits=10, decimal_places=2)
    local_price_max = models.DecimalField(max_digits=10, decimal_places=2)
    market_relation = models.CharField(max_length=100)
    range_num1 = models.PositiveSmallIntegerField(null=True, blank=True)
    range_num2 = models.PositiveSmallIntegerField(null=True, blank=True)
    valuation_coeff = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    valuation = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.nr}. {self.name}"
