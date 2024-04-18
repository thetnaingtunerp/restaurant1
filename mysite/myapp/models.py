from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class tablename(models.Model):
    table_name = models.CharField(max_length=100)
    occupy = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.table_name

class kitchen_counter(models.Model):
    counter_name = models.CharField(max_length=100)

    def __str__(self):
        return self.counter_name
class item(models.Model):
    item_name = models.CharField(max_length=200)
    sale_price = models.PositiveIntegerField(default=0)
    kitchen = models.ForeignKey(kitchen_counter, on_delete=models.CASCADE, blank=True, null=True)
    out_of_order = models.BooleanField(default=False)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.item_name