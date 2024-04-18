from django.contrib import admin
from .models import *
# Register your models here.

class tablenameadmin(admin.ModelAdmin):
    list_display = ('id', 'table_name', 'occupy')
admin.site.register(tablename,tablenameadmin)

class kitchen_counter_admin(admin.ModelAdmin):
    list_display = ('id', 'counter_name')
admin.site.register(kitchen_counter,kitchen_counter_admin)

class item_admin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'sale_price', 'kitchen', 'out_of_order', 'active_status')
admin.site.register(item, item_admin)