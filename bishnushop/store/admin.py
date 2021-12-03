from django.contrib import admin
from django.db import models
from django.db.models import fields
from .models import Category,Product,Payment,UserProduct
from math import floor
from django.db.models import F
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model  = Product
    list_display = ['name','category','get_price','get_descount','get_sale_price' , 'active']
    list_editable = ['active']
    list_filter = ['active','category']
    actions = ['make_active','make_inactive','set_descount_25_percantage','set_descount_50_percantage','increase_descount_bt_5_percantage']



    def get_price(self, product):
        return f'Rs. {product.price}'

    def get_descount(self, product):
        return f'Rs. {product.descount} %'

    def get_sale_price(self, product):
        sale_price =  floor(product.price - (product.price * product.descount * 0.01))
        return f'Rs . {sale_price}'

   
    fieldsets = (
        (
            "General Information", {
                "fields" : ('name','slug')
            }
        ), (
            "Description" ,{
                "fields" : ('description','category')
            }
        ) ,
        (
            "Pricing Information" ,{
                "fields" : ('price','descount')
            }
        ),
        (
            "Files" ,{
                "fields" : ('thumbnail','file','file_size')
            }
        ),
        (
            None, {
                'fields' : ('active',)
            }
        )

       
    )

#actions
    def make_active(self, request,queryset):
        queryset.update(active=True)

#actions
    def make_inactive(self, request,queryset):
        queryset.update(active=False)

    def set_descount_50_percantage(self, request,queryset):
        queryset.update(descount=50)

    def set_descount_25_percantage(self, request,queryset):
        queryset.update(descount=25)

    def increase_descount_bt_5_percantage(self, request,queryset):
        queryset = queryset.filter(descount__lte = 95)
        queryset.update(descount = F('descount')+5)


    get_price.short_description = 'Price'
    get_descount.short_description = 'Discount'
    get_sale_price.short_description = 'Sale Price'
    set_descount_25_percantage.short_description = 'set 25%% Discount'
    set_descount_50_percantage.short_description = 'set 50%% Discount'


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Payment)
admin.site.register(UserProduct)